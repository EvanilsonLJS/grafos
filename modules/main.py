from re import X


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
    print("3 - Para imprimir o grau do grafo")
    print("4 - Para imprimir a ordem do grafo")
    print("5 - Para imprimir grau e ordem do grafo")
    print("6 - Para listar os vértices adjacentes")
    print("7 - Para imprimir o Grau de Adjacência do vértice")
    print("8 - Para identificar se dois vértices são adjacentes")
    print("9 - Para Retornar o caminho mais curto entre dois vértices")
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
        flag = True
        
        file_name = str(input('Digite o nome do arquivo de vertices:'))
        file_name_a = str(input("Digite o nome do arquivo de arestas: "))

        with open(f'{file_name}', 'r', encoding='UTF-8') as file:

            for line in file.readlines():
                v.append(line)
               
        file.close()

        with open(f'{file_name_a}', 'r', encoding='UTF-8') as file_a:

            for line in file_a.readlines():
                value.append(int(line), end='')
        
        file_a.close()
               
        # Adiciona os vertices as listas v1 e v2 
        x = 0
        y = 1
        for i in range(len(v)):
            if (len(v1) + len(v2) == len(v)):
                break
            v1.append(v[x])
            if (len(v1) + len(v2) == len(v)):
                break
            v2.append(v[y])
            x += 2
            y += 2
            

        print(v1)
        print(v2)
    
        # #verificando se a aresta a ser adicionada é válida (não é laço, nem transforma em multigrafo)
        # for j in range(len(v1)):
        #     if v1[j] == v2[j]:
        #         print('Laços não são permitidos!')
        #         break
        #     if v1.count(v1[j]) > 1 and v2.count(v2[j]) > 1:
        #         print('Uma aresta com esses vértices já foi adicionada!')
        #         break
        #     if (v2.count(v1[j]) == 1 and v1.count(v2[j]) == 1) and (v2.index(v1[j]) == v1.index(v2[j])):
        #         print("Grafos com arestas paralelas não são validos")
        #         break
        
            # flag = False
            
    #Imprimindo o grau(req5)
    if opcao == 3:
        if (len(v) == 0):
            print("[Atenção] - Grafo ainda não foi criado")
        else:
            print("O grafo possui grau ",len(v))

    #Imprimindo a ordem (req5)
    if opcao == 4:
        if (len(v1) == 0):
            print("[Atenção] - Grafo ainda não foi criado")
        else:
            print("O grafo possui ordem ",len(v1))

    # #imprimindo agrau e ordem (req5)
    if opcao == 5:
        if (len(v) == 0):
            print("[Atenção] - Grafo ainda não foi criado")
        else:
            print("O grafo possui grau ", len(v))
            print("O grafo possui ordem ", len(v1))

    # #Vértices adjacentes(req6)
    if opcao == 6:
        if (len(v) == 0):
            print("[Atenção] - Grafo ainda não foi criado")
        else:
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

    #imprimindo grau do vértice (req7)
    if opcao == 7:
        if (len(v) == 0):
            print("[Atenção] - Grafo ainda não foi criado")
        else:
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
                adj_entrada = []
                adj_saida = []
                i = 0
                for i in range (len(v1)):
                    if vertice == v1[i]:
                        adj_saida.append(v2[i])
                    elif vertice == v2[i]:
                        adj_entrada.append(v1[i])

                if dir == 1:
                    print("Grau de adjacência de entrada: ", len(adj_entrada))
                    print("Grau de adjacência de saída: ", len(adj_saida))
                elif dir == 0:
                    sum_adj = len(adj_entrada) + len(adj_saida)
                    print("Grau de adjacência: ", sum_adj)
        
    # #identificando se 2 vértices são adjacentes (req8)
    if opcao == 8:
        if (len(v) == 0):
            print("[Atenção] - Grafo ainda não foi criado")
        else:
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

    if opcao == 9:
        vertice1 = input("digite o 1º vértice: ")
        vertice2 = input("digite o 2º vértice: ")