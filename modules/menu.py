print("Digite 1 para inserir um item de cada vez: ")
print("Digite 2 para inserir todas as arestas em uma única linha, no formato tal: ")
print("Digite 3 para inserir todas as arestas através de um arquivo, no formato tal: ")
opcao = int(input("Opção? "))

import req_1

if (opcao == 1):
    req_1.Requisito_1

elif (opcao == 2):
    print("Opcao 2")

elif(opcao == 3):
    print("Opcao 3")

