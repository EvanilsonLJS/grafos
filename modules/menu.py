from curses.ascii import isdigit
from pickle import UNICODE


v = [] # Lista de vertices
v1 = [] # Lista do primeiro vertice de cada aresta
v2 = [] # Lista do segundo vertice de cada aresta
value = [] # Lista dos valores das arestas

print('=> Criando um grafo <=')
print('Digite:')
print('0 - Para grafo não direcionado')
print('1 - Para grafo direcionado')
dir = int(input('Direção: ')) #(req3)
if dir == 0:
    print("Grafo não direcionado")
else:
    print("Grafo direcionado")

opcao = -1
while opcao != 0:
    print('\nDigite:')
    print("1 - Para inserir um item")
    print("2 - Para inserir vários itens em uma única linha")
    print("3 - Para inserir em lote por um arquivo")# ficou faltando
    print("4 - Para imprimir o grau do grafo")
    print("5 - Para imprimir a ordem do grafo")
    print("6 - Para imprimir grau e ordem do grafo")
    print("7 - Para listar os vértices adjacentes")
    print("8 - Para identificar se dois vértices são adjacentes")
    print("0 - Para encerrar")

    opcao = int(input("\n=> Opção: "))

    #Inserindo um de cada vez (req1)
    if opcao == 1:
        print('Digite:')
        print("1 - Para inserir um vértice")
        print("2 - Para inserir uma aresta")
        opcao2 = int(input("Opção: "))

        if opcao2 == 1:
            vertice = input('Digite o rótulo do vértice: ') #(req3)
            repeat_v = 0
            i = 0
            for i in range(len(v)):
                if (v[i] == vertice):
                    print('Um vértice com esse rótulo já foi adicionado')
                    repeat_v = 1
                    break

            if repeat_v == 0:
                v.append(vertice)


        if opcao2 == 2:
            vertice1 = input("digite o 1º vértice da aresta: ")
            vertice2 = input("digite o 2º vértice da aresta: ")
            repeat_a = 0
            valid_v1 = 0
            valid_v2 = 0

            #verificando se os vértices da aresta estão registrados na lista de vértices
            i = 0
            for i in range (len(v)):
                if vertice1 == v[i]:
                    valid_v1 += 1
                if vertice2 == v[i]:
                    valid_v2 += 1
            if valid_v1 == 0:
                print("O primeiro vértice ainda não está na lista de vértices")
            if valid_v2 == 0:
                print("O segundo vértice ainda não está na lista de vértices")

            #verificando se a aresta a ser adicionada é válida (não é laço, nem transforma em multigrafo)
            for j in range(len(v1)):
                if vertice1 == vertice2:
                    print('Laços não são permitidos!')
                    repeat_a = 1
                    break
                elif (v1[j] == vertice1 and v2[j] == vertice2):
                    print('Uma aresta com esses vértices já foi adicionada!')
                    repeat_a = 1
                    break
                elif (v1[j] == vertice2 and v2[j] == vertice1):
                    print('Uma aresta com esses vértices já foi adicionada!')
                    repeat_a = 1
                    break

            #caso seja válido e os vértices já estejam registrados, adiciona os vértices e pergunta-se o valor da aresta
            if (valid_v1 == 1 and valid_v2 == 1):
                if repeat_a == 0:
                    valor = input("digite o valor da aresta: ")
                    v1.append(vertice1)
                    v2.append(vertice2)
                    value.append(valor)

    
    #Inserindo em lote (req2)
    if opcao == 2:
        aux = []
        flag = True
        
       

        while flag == True:
            lote = str(input("Digite o grafo em lote:"))

            # Adiciona a string a um lista auxiliar chamada aux
            for i in range(len(lote)):
                lote[i].split()
                aux.append(lote[i])
            
            # Diferencia o que for alfabetico e numerico, alfabetico são vertices, numericos são arestas
            for j in range(len(aux)):
                if str(aux[j]).isalpha():
                    v.append(aux[j])

                if str(aux[j]).isnumeric():
                    value.append(aux[j])

            # Adiciona os vertices as listas v1 e v2 
            x = 0
            y = 0
            for i in range(len(v)):
                v1.append(v[x])
                v2.append(v[y + 1])
                x += 2
                y += 2
                if len(v1) + len(v2) == len(v):
                    break
            
            if len(lote) == len(aux):
                flag = False

    
        
        
    #Imprimindo o grau(req5)
    if opcao == 4:
        print("O grafo possui grau ",len(v))

    #Imprimindo a ordem (req5)
    if opcao == 5:
        print("O grafo possui ordem ", len(v1))

    # #imprimindo agrau e ordem (req5)
    if opcao == 6:
        print("O grafo possui grau ", len(v))
        print("O grafo possui ordem ", len(v1))

    # #Vértices adjacentes(req6)
    if opcao == 7:
        v_exist = 0
        vertice = input("Digite um vértice já inserido no grafo: ")
        j = 0
        for j in range (len(v)):
            #print(v[j], "|", vertice, "|")
            if v[j] == vertice:
                v_exist = 1
                break
        if v_exist == 0:
            print("Esse vértice ainda não foi inserido")
        else:
            adj_v1 = []
            adj_v2 = []
            i = 0
            for i in range (len(v1)):
                if vertice == v1[i]:
                    adj_v1.append(v2[i])
                elif vertice == v2[i]:
                    adj_v2.append(v1[i])
            
            for m in range (len(adj_v1)):
                if dir == 0:
                    print("Vértices adjacentes:", end = " ")
                if dir == 1:
                    print("Vértices de saída: ")
                print(adj_v1[m], end = " ")

            
            for n in range (len(adj_v2)):
                if dir == 1:
                    print("\nVértices de entrada: ")
                print(adj_v2[n], end = " ")
                
            print("\n")

    # #identificando se 2 vértices são adjacentes
    if opcao == 8:
        v_exist = 0
        vertice_1 = input("Digite um vértice: ")
        vertice_2 = input("Digite outro vértice: ")
        i = 0
        adj = 0

        for i in range (len(v1)):
            if vertice_1 == v1[i]:
                if vertice_2 == v2[i]:
                    adj = 1
                    print("Os vértices são adjacentes")
                    break
            elif vertice_2 == v1[i]:
                if vertice_1 == v2[i]:
                    adj = 1
                    print("Os vértices são adjacentes")
                    break

        if adj == 0:
            print("Os vértices não são adjacentes!")
