import xmlrpc.client

def show_menu():
    print("1. Pesquisa")
    print("2. Ver todos os trabalhos especificados pelo portal")
    print("3. Pesquisar por um trabalho em especifico")
    print("4. Ordenação")
    print("5. Intercambio")
    print("0. Exit")

def main():
    print("connecting to server...")
    server = xmlrpc.client.ServerProxy('http://is-rpc-server:9000')

    while True:
        show_menu()
        option = str(input("Select option: "))

        if option == '1':
            # Pesquisa logic
            print(f" > {server.select_xml_from_database()}")
            pass
        
        elif option == '2':
            # All jobPortals and respective jobs
            print(f" > {server.xpath_query_1()}")
            pass
        
        elif option == '3':
            # Search by job
            # Example XPath query
            xpath_jobTitle = str(input("Job Title: "))
            print(f" > {server.xpath_query_2(xpath_jobTitle)}")
            pass
        
        elif option == '4':
            # Ordenação logic
            pass
        
        elif option == '5':
            # Intercambio logic
            pass
        
        elif option == '0':
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()