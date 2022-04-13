import networkx as nx

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
    print("2 - Para inserir vários itens por um arquivo")
    print("3 - Para imprimir o ordem do grafo")
    print("4 - Para imprimir a grau do grafo")
    print("5 - Para imprimir grau e ordem do grafo")
    print("6 - Para listar os vértices adjacentes")
    print("7 - Para imprimir o grau de adjacência do vértice")
    print("8 - Para identificar se dois vértices são adjacentes")
    print("9 - Para Retornar o caminho mais curto entre dois vértices")
    print("10 - Pera imprimir a lista de adjacência do grafo ")
    print("11 - Para verificar se o vértice é pendente")
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

        arq_vert = input("Digite o nome do arquivo de vertices: ")
        arq_arest = input("Digite o nome do arquivo de arestas: ")

        with open(f'{arq_vert}', 'r') as file:
            for line in file.readlines():
                line = line.rstrip('\n')
                repeat_v = 0
                for i in range(len(v)):
                    if (v[i] == line):
                        print('Um vértice com esse rótulo já foi adicionado')
                        repeat_v = 1
                        break
                    
                if repeat_v == 0:
                    v.append(line)
        file.close()
        
        with open(f'{arq_arest}', 'r') as file:
            teste = []
            for line in file.readlines():
                line = line.rstrip('\n')
                teste.append(line)
                teste2 = teste[-1]
                final = teste2.split()
                v1.append(final[0])
                v2.append(final[1])
                value.append(int(final[2]))
                #print(v1[-1] + " " + v2[-1] + " " + value[-1])
        file.close()
       
    #Imprimindo o ordem(req5)
    if opcao == 3:
        print("O grafo possui ordem ",len(v))

    #Imprimindo a grau (req5)
    if opcao == 4:
        print("O grafo possui grau ",len(v1))

    # #imprimindo agrau e ordem (req5)
    if opcao == 5:
        print("O grafo possui ordem ", len(v))
        print("O grafo possui grau ", len(v1))

    # #Vértices adjacentes(req6)
    if opcao == 6:
        v_exist = 0
        vertice = input("Digite um vértice já inserido no grafo: ")

        for j in range(len(v)):
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
            for i in range(len(v1)):
                if vertice == v1[i]:
                    adj_v1.append(v2[i])
                elif vertice == v2[i]:
                    adj_v2.append(v1[i])
            
            for m in range(len(adj_v1)):
                if dir == 0:
                    if m == 0:
                        print("Vértices adjacentes:", end = " ")
                if dir == 1:
                    if m == 0:
                        print("Vértices de saída: ")
                print(adj_v1[m], end = " ")

            
            for n in range(len(adj_v2)):
                if dir == 1:
                    if n == 0:
                        print("\nVértices de entrada: ")
                print(adj_v2[n], end = " ")
                
            print("\n")

    #imprimindo grau do vértice (req7)
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

    # Para indentificar a menor distancia entre dois vertices (req9)
    if opcao == 9:
        if dir == 0:
            g = nx.Graph()
        else:
            g = nx.DiGraph()
            g.to_directed()

        for i in range(len(v1)):
            g.add_edge(v1[i], v2[i], weight=value[i])

        vertice1 = input("Digite o vértice de origem: ")
        #vertice1 = int(vertice1)
        vertice2 = input("Digite o vértice de destino: ")
        #vertice2 = int(vertice2)

        print("Caminho mais curto: ", nx.shortest_path(g, vertice1, vertice2, 'weight'))
        print("Custo para percorrer: ", nx.shortest_path_length(g, vertice1, vertice2, 'weight'))
          
    # Imprime a lista de adjacências (req4)
    if opcao == 10:
        v_exist = 1
        for i in range(len(v)):
            vertice = v[i]

            for j in range(len(v)):
                #print(v[j], "|", vertice, "|")
                if v[j] == vertice:
                    v_exist = 1
                    break
            if v_exist == 0:
                print("Esse vértice ainda não foi inserido")
            else:
                adj_v1 = []
                adj_v2 = []
                w = 0
                for w in range(len(v1)):
                    if vertice == v1[w]:
                        adj_v1.append(v2[w])
                    elif vertice == v2[w]:
                        adj_v2.append(v1[w])
                print(v[j], end = " ")
                for m in range(len(adj_v1)):
                    print(" -> ", end=" ")
                    print(adj_v1[m], end = " ")

                if (dir == 0):
                    for n in range(len(adj_v2)):
                        print(" -> ", end=" ")
                        print(adj_v2[n], end = " ")
                    
                print("-v")
        print("\n")
    # Vertices pendentes (req10 A)
    if opcao == 11:

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

            pend = len(adj_saida) + len(adj_entrada)
            if pend == 1:
                print("Esse vertice é do tipo pendente!")
            else:
                print("Esse vertice não é do tipo pendente")

    if opcao == 20:
        print(v)
        print(v1)
        print(v2)
        print(value)

    if opcao == 0:  
        print("Obrigado =))")
        break