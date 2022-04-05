from saida import saida
class Requisito_1:

    v = [] # Lista de vertices
    v1 = [] # Lista do primeiro vertice de cada aresta
    v2 = [] # Lista do segundo vertice de cada aresta
    list_val = [] # Lista dos valores das arestas
    list_dir = [] # Lista do direcionamento ou não

   

    

    #Recebe os vértices e adiciona a lista de vertices até digitar nenhum valor
    cont = 0
    vertice = 0
    while vertice != '':
        vertice = input("Digite o vértice: ")    
        if vertice != '':
            v.append(vertice)
            cont += 1
        

    # print("Lista de Vertices:")
    # for i in v:
    #     print(f"|{i}|")

    
    flag = True
    while flag:
        vertice_1 = input(f"Digite o vertice da aresta: ")
        vertice_2 = input(f"Digite o vertice da aresta: ") 
        
        if vertice_1 == '' and vertice_2 == '': # Para o loop caso o usuário n queira criar mais aresta
            break

        v1.append(vertice_1)
        v2.append(vertice_2)

        if (len(v1) and len(v2)) == len(v): # Verifica se a lista de vertices que representa as arestas está completa
            flag = False
    
    # Verificando se foi adicionado corretamente (Pode ser removido no futuro)
    print("Lista v1")
    for i in v1:
        print(f"|{i}|")
    
    print("\n")

    print("Lista v2")
    for i in v2:
        print(f"|{i}|")
    
    # #Verificando se são ou não direcionados ou valorados 
    # dir = input("A aresta é direcionada?  [Y/n]: ").upper()
    # val = input("A aresta valorada? [Y/n]: ").upper()

    # if (dir == 'Y'):
    #     inserir(list_dir, 1)

    # elif (dir == 'N'):
    #     inserir(list_dir, 0)

    # if (val == 'N'):
    #     inserir(list_val, 0)

    # elif (val == 'Y'):
    #     val_2 = input("Qual o valor da aresta? : ").upper()
    #     inserir(list_val, val_2)

    # saida(cont, v1, list_val, list_dir)

