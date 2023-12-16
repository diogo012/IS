import xmlrpc.client

def show_menu():
    print("1. Inserir xml exemplo na BD")
    print("2. Eliminar xml")
    print("3. Ver todos os xml existentas")
    print("4. Ver todos os trabalhos especificados pelo portal")
    print("5. Pesquisar por um trabalho em especifico")
    print("6. Agrupar Roles por Referência de Companhia")
    print("7. Ordenar por Roles ASC")
    print("0. Exit")

def main():
    print("connecting to server...")
    server = xmlrpc.client.ServerProxy('http://is-rpc-server:9000')

    while True:
        show_menu()
        option = str(input("Select option: "))
        
        if option == '1':
            # Insert xml
            print("De momento nao está funcional")
            # print(f" > {server.insert_xml_to_database()}")
            pass
        
        elif option == '2':
            # Delete xml
            file_name = str(input("Nome do Ficheiro XML: "))
            print(f" > {server.delete_xml_from_database(file_name)}")
            pass

        elif option == '3':
            # All xml´s
            print(f" > {server.select_xml_from_database()}")
            pass
        
        elif option == '4':
            # All jobPortals and respective jobs
            print(f" > {server.xpath_query_1()}")
            pass
        
        elif option == '5':
            # Search by job
            xpath_jobTitle = str(input("Nome do Emprego: "))
            print(f" > {server.xpath_query_2(xpath_jobTitle)}")
            pass
        
        elif option == '6':
            # Group By Roles.Company_Ref and Order by Roles.Roles.Company_Ref
            print(f" > {server.xpath_query_3()}")
            pass
        
        elif option == '7':
            # Order By Roles ASC
            print(f" > {server.xpath_query_4()}")
            pass
        
        elif option == '0':
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()