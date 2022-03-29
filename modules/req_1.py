
from saida import saida
class Requisito_1:

    v = [] # Lista de vertices

    v1 = [] # Lista do primeiro vertice de cada aresta
    v2 = [] # Lista do segundo vertice de cada aresta
    list_val = [] # Lista dos valores das arestas

    list_dir = [] # Lista do direcionamento ou não

    def inserir(lista, valor):

        for i in range(len(lista)):
            if (valor == lista[i]):
                print(f"O vértice: {valor} já foi criado!")

        lista.append(valor)


    #Recebe os vértices até digitar nenhum valor
    cont = 0
    while True:
        vertice = input("Digite o vértice: ")
        if (vertice == ''):
            print("Ok! Agora precisamos conectar os vertices")
            break

        inserir(v, vertice)
        cont += 1

    #Recebe os vértices que vão se conectar
    for i in range(cont):
        vertice = input(f"Digite o {i + 1} vertice da aresta: ")
        inserir(v1, vertice) #Não precisa do v2


    #Verificando se são ou não direcionados ou valorados 
    dir = input("A aresta é direcionada?  [Y/n]: ").upper()
    val = input("A aresta valorada? [Y/n]: ").upper()

    if (dir == 'Y'):
        inserir(list_dir, 1)

    elif (dir == 'N'):
        inserir(list_dir, 0)

    if (val == 'N'):
        inserir(list_val, 0)

    elif (val == 'Y'):
        val_2 = input("Qual o valor da aresta? : ").upper()
        inserir(list_val, val_2)

    saida(cont, v1, list_val, list_dir)

