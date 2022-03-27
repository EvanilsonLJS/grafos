from req_1 import principal

if __name__ == "__main__":
    

    print("Digite 1 para inserir um item de cada vez: ")
    print("Digite 2 para inserir todas as arestas em uma única linha, no formato tal: ")
    print("Digite 3 para inserir todas as arestas através de um arquivo, no formato tal: ")

    opcao = int(input("Opção? "))

    if (opcao == 1):
        principal()

    elif (opcao == 2):
        print("Opcao 2")

    elif(opcao == 3):
        print("Opcao 3")

    