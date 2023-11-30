import xmlrpc.client

print("connecting to server...")
server = xmlrpc.client.ServerProxy('http://is-rpc-server:9000')

# Example XPath query
xpath_query = '/Jobs/JobPortals/JobPortal/Jobs/Job/@jobTitle'

print(f" > {server.select_xml_from_database()}")
print(f" > {server.xpath_query_database(xpath_query)}")