import signal
import sys
import psycopg2
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Function to connect to the database
def connect_to_database():
    return psycopg2.connect(user="is", 
                            password="is", 
                            host="is-db", 
                            port="5432", 
                            database="is")

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
            
            
# Function to perform an XPath query on the database
def xpath_query_database(xpath_query):
    connection = connect_to_database()
    cursor = connection.cursor()

    try:
        cursor.execute(f"SELECT xpath('{xpath_query}', xml) AS result FROM public.imported_documents;")
        result = cursor.fetchall()

        return result

    except Exception as error:
        return f"Failed to fetch data: {error}"

    finally:
        if connection:
            cursor.close()
            connection.close()
            
            

# Set up the XML-RPC server
with SimpleXMLRPCServer(('0.0.0.0', 9000), requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    # Register functions
    server.register_function(select_xml_from_database)
    
    # Register the XPath query function
    server.register_function(xpath_query_database, 'xpath_query_database')

    

    # Start the server
    print("Starting the RPC Server...")
    server.serve_forever()
