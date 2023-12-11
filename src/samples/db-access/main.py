import psycopg2
from psycopg2.extras import execute_values
import xml.etree.ElementTree as ET

# Function to read XML file
def read_xml_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        xml_content = file.read()
    return xml_content

# Connect to the database
connection = psycopg2.connect(user="is", 
                              password="is", 
                              host="is-db", 
                              port="5432", 
                              database="is")
cursor = connection.cursor()

try:
    # Read XML file
    xml_content = read_xml_file('/data/jobdescriptions.xml')

    # Insert XML into the database
    cursor.execute("INSERT INTO public.imported_documents (file_name, xml) VALUES (%s, %s) RETURNING id;",
                   ('jobdescriptions.xml', xml_content))
    
    # Commit the transaction
    connection.commit()

    print("XML file added to the database.")


except (Exception, psycopg2.Error) as error:
    print("Failed to insert data", error)

finally:
    if connection:
        cursor.close()
        connection.close()