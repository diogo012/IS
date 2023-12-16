import signal
import sys
import psycopg2
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler


class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ("/RPC2",)


# Function to connect to the database
def connect_to_database():
    return psycopg2.connect(
        user="is", password="is", host="is-db", port="5432", database="is"
    )


# Function to insert XML data to the database
def insert_xml_to_database():
    try:
        # Connect to the database
        connection = connect_to_database()
        cursor = connection.cursor()

        try:
            # Assuming your table structure includes 'id', 'file_name', and 'xml' columns
            query = ("INSERT INTO public.imported_documents (file_name, xml) VALUES (%s, %s) RETURNING id;")
            cursor.execute(query, (os.path.basename('ExemploXML'), xml_data))
            new_document_id = cursor.fetchone()[0]
            connection.commit()

            return f"XML data inserted successfully with document ID: {new_document_id}"

        except Exception as error:
            connection.rollback()
            return f"Failed to insert data: {error}"

        finally:
            if connection:
                cursor.close()
                connection.close()

    except Exception as error:
        return f"Error: {error}"
            
# Function to delete XML data from the database
def delete_xml_from_database(file_name):
    file_name = str(file_name)

    connection = connect_to_database()
    cursor = connection.cursor()
    
    try:
        cursor.execute("DELETE FROM public.imported_documents WHERE file_name = %s;", (file_name,))
        connection.commit()  # Commit the changes after DELETE
        return "Deletion successful"

    except Exception as error:
        return f"Failed to delete data: {error}"

    finally:
        if connection:
            cursor.close()
            connection.close()

            
    # Function to select XML data from the database
def select_xml_from_database():
    connection = connect_to_database()
    cursor = connection.cursor()

    try:
        cursor.execute("SELECT id,file_name FROM public.imported_documents;")
        result = cursor.fetchall()
        return result

    except Exception as error:
        return f"Failed to fetch data: {error}"

    finally:
        if connection:
            cursor.close()
            connection.close()


# Function to execute querys
def execute_query(cursor, query):
    try:
        cursor.execute(query)
        result = cursor.fetchall()

        return result
    except Exception as error:
        raise f"Failed to execute query: {error}"


# Function to perform an XPath query on the database
# QUERY - All jobPortals and respective jobs
def xpath_query_1():
    connection = connect_to_database()
    cursor = connection.cursor()

    try:
        query = f"SELECT (xpath('/JobPortal/@id', jobportal))::text AS jobportal_id, (xpath('/JobPortal/@jobPortal', jobportal))::text AS jobportal_name, (xpath('/JobPortal/Jobs/Job/@jobTitle', jobportal)) AS job_titles FROM (SELECT unnest(xpath('/Jobs/JobPortals/JobPortal', xml)) AS jobportal FROM public.imported_documents) AS subquery;"
        result = execute_query(cursor, query)
        return result

    except Exception as error:
        raise f"Failed to fetch data: {error}"

    finally:
        if connection:
            cursor.close()
            connection.close()

# QUERY - Search by job
def xpath_query_2(xpath_jobTitle):
    connection = connect_to_database()
    cursor = connection.cursor()

    try:
        # First query
        first_query = f"SELECT unnest(xpath('/Jobs/JobPortals/JobPortal/Jobs/Job[@jobTitle=\"{xpath_jobTitle}\"]/@*', xml)) AS job_attributes FROM public.imported_documents;"
        result = execute_query(cursor, first_query)

        # Extract the numeric part (person id)
        result_numeric_part = result[7][0].replace(",", "")
        # Extract the numeric part (role id)
        result2_numeric_part = result[8][0].replace(",", "")

        # Second query
        second_query = f"SELECT unnest(xpath('/Jobs/Persons/Person[@id=\"{result_numeric_part}\"]/@*', xml)) AS Person_attributes FROM public.imported_documents;"
        result2 = execute_query(cursor, second_query)

        # Third query
        third_query = f"SELECT unnest(xpath('/Jobs/Roles/Role[@id=\"{result2_numeric_part}\"]/@*', xml)) AS Role_attributes FROM public.imported_documents;"
        result3 = execute_query(cursor, third_query)

        # Extract the numeric part (company id)
        result3_numeric_part = result3[3][0].replace(",", "")

        # Fourth query
        fourth_query = f"SELECT unnest(xpath('/Jobs/Companies/Company[@id=\"{result3_numeric_part}\"]/@*', xml)) AS Company_attributes FROM public.imported_documents;"
        result4 = execute_query(cursor, fourth_query)

        # Extract the numeric part (country id)
        result4_numeric_part = result4[3][0].replace(",", "")

        # Fifth query
        fifth_query = f"SELECT unnest(xpath('/Jobs/Countries/Country[@id=\"{result4_numeric_part}\"]/@*', xml)) AS Country_attributes FROM public.imported_documents;"
        result5 = execute_query(cursor, fifth_query)

        # Return the combined results or any specific result you need
        return f"\nJob Info:\n{result}\n\nPerson Info:\n{result2}\n\nRole Info:\n{result3}\n\nCompany Info:\n{result4}\n\nCountry Info:\n{result5}\n"

    finally:
        if connection:
            cursor.close()
            connection.close()
    
    # QUERY - Group By Roles.Company_Ref and Order by Roles.Roles.Company_Ref
def xpath_query_3():
    connection = connect_to_database()
    cursor = connection.cursor()

    try:
        query = f"SELECT x.company_ref AS Role_Company, y.company_name AS Company_Name, STRING_AGG(DISTINCT x.role_name, ', ') AS Role_Names FROM public.imported_documents, LATERAL xmltable('/Jobs/Roles/Role' PASSING xml COLUMNS company_ref text PATH '@company_ref', role_name text PATH '@role') AS x, LATERAL (SELECT company_name FROM xmltable('/Jobs/Companies/Company' PASSING xml COLUMNS company_name text PATH '@company', company_id text PATH '@id') AS y WHERE CAST(y.company_id AS INTEGER) = CAST(x.company_ref AS INTEGER) LIMIT 1) AS y GROUP BY Role_Company, Company_Name ORDER BY CAST(x.company_ref AS INTEGER) ASC;"
        result = execute_query(cursor, query)
        return result

    except Exception as error:
        raise f"Failed to fetch data: {error}"

    finally:
        if connection:
            cursor.close()
            connection.close()
            
    # QUERY - Order By Roles
def xpath_query_4():
    connection = connect_to_database()
    cursor = connection.cursor()

    try:
        query = f"SELECT unnest(xpath('/Jobs/Roles/Role/@role', xml))::text AS Role_Name, unnest(xpath('/Jobs/Roles/Role/@salaryRange', xml))::text AS Salary_Range FROM public.imported_documents ORDER BY Role_Name ASC;"
        result = execute_query(cursor, query)
        return result

    except Exception as error:
        raise f"Failed to fetch data: {error}"

    finally:
        if connection:
            cursor.close()
            connection.close()


# Set up the XML-RPC server
with SimpleXMLRPCServer(("0.0.0.0", 9000), requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    # Register functions
    server.register_function(insert_xml_to_database)
    server.register_function(delete_xml_from_database)
    server.register_function(select_xml_from_database)

    # Register the XPath query function
    server.register_function(xpath_query_1, "xpath_query_1")
    server.register_function(xpath_query_2, "xpath_query_2")
    server.register_function(xpath_query_3, "xpath_query_3")
    server.register_function(xpath_query_4, "xpath_query_4")

    # Start the server
    print("Starting the RPC Server...")
    server.serve_forever()
