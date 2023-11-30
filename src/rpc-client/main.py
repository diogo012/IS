import xmlrpc.client

def show_menu():
    print("1. Pesquisa")
    print("2. Filtros")
    print("3. Agrupamento")
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
            # Filtros logic
            # Example XPath query
            xpath_query = '/Jobs/JobPortals/JobPortal/Jobs/Job/@jobTitle'
            print(f" > {server.xpath_query_database(xpath_query)}")
            pass
        
        elif option == '3':
            # Agrupamento logic
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

""" import xmlrpc.client

print("connecting to server...")
server = xmlrpc.client.ServerProxy('http://rpc-server:9000')

while True:
    print("\n")
    print("**DESASTRES AÉREOS**")
    print("---------------------------------------")
    print(" 1-Transformar CSV em XML              ")
    print("---------------------------------------")
    print(" 2-Validar o XML e importar o ficheiro ")
    print("---------------------------------------")
    print(" 3-Queries                             ")
    print("---------------------------------------")
    print(" 4-Saída                               ")
    print("**")
    print("\n")
    opcao = str(input("Selecione Opcao: "))

    if (opcao == '1'):
        print(server.to_xml_str())
        xml_data = server.get_xml_data()

        xml_path = "arquivo.xml"
        with open(xml_path, 'w') as arquivo:
            arquivo.write(xml_data)

    elif (opcao == '2'):
        print("A VALIDAR")
        xml_path = "arquivo.xml"
        result = server.validate_xml(xml_path)

        nome = input("NOME DO FICHEIRO A GUARDAR: ")
        result_data= server.import_documents(nome, xml_path)
        print("\nSUCESSO\n")
        print(result_data)

        if result:
            print('Válido! :)')
        else:
            print('Não válido! :(')
    elif (opcao == '3'):
            print("\n")
            print("**QUERIES**")
            print("-----------------------------------")
            print(" 1-                ")
            print("-----------------------------------")
            print(" 2-             ")
            print("-----------------------------------")
            print(" 3-                ")
            print("-----------------------------------")
            print("***")
            print("\n")
            opcao2 = str(input("Selecione Opcao: "))

            if (opcao2 == '1'):
                for x in server.query1():
                    print(x)

            elif (opcao2 == '2'):
                for x in server.query2():
                    print(x)

            elif (opcao2 == '3'):
                #NAO DA
                nome_pais = input('Introduza o nome do pais a procurar: \n')
                for x in server.query3(nome_pais):
                    print(x)


            elif(opcao == '4'):
                print("ESPEREMOS QUE NÃO HAJA MAIS DESASTRES")
                pass

    else:
        print("OPÇÃO INVALIDA") """