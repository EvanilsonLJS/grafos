# Grafos Avaliação 1

### Sistema em python que armazena um grafo simples onde a definição do grafo é definida pelo usuário

## Ferramentas

Ferramentas utilizadas no sistema:
- [Python] - Codificação do software.
- [Git e GitHub] - Para o controle de vercionamento.
- [Notion] - Para gerenciamento das tarefas do projeto.
- [Networkx] - Biblioteca python para manipulação e criação de estruturas.
- [Discord] - Para reuniões do projeto.

## Funcionalidades

- O usuário pode interagir com o sistema pelo terminal com um menu de navegação de criação, e visualização do grafo 
- O usuário pode criar o grafo inserindo um item por vez ou em lote
- O usuário pode criar grafos direcionados ou não
- O usuário pode imprimir a lista de adjacência do grafo
- O usuário pode obter informações do tamanho e ordem do grafo
- Dado um vertice qualquer o usuário pode obter a lista de vértices adjacentes (os de entradas e saída)
- Para um grafo direcionado o usuário pode obter o grau adjacente de um vértice específico
- Dado dois vértices  o usuário pode saber se são adjacentes ou não
- O usuário pode saber o caminho mais curto entre dois vértices



## Descrição do código do sistema:

### Abaixo tem a descrição de tres das funcionalidades do sistema, para cada instrução no código tem um comentário

- Primeiro foi declarado quatro listas que irão ser usadas para armazenamento do grafo. ```v``` representa a lista de vértices, logo após temos ```v1``` que representa a lista do primeiro vértice de cada aresta, ```v2``` representa a lista do segundo vértice de cada aresta, e por último, ```value``` representa a lista dos valores das arestas. Observe abaixo:
```sh
v = [] # Lista de vertices
v1 = [] # Lista do primeiro vertice de cada aresta
v2 = [] # Lista do segundo vertice de cada aresta
value = [] # Lista dos valores das arestas

```

- Nesse ponto temos o menu que irá ser impresso no terminal após o software ser executado. No primeiro momento precisamos digitar um valor boleano onde vai ser a definição do grafo direcionado ou não direcionado, onde: 0 é para não direcionado e 1 é para direcionado. Mais abaixo temos um loop que vai sempre verificar se o usuário digitou '0' caso contrario o usuário poderar escolher cada opção onde será executada a funcionalidade (cada opção representa uma funcionalidade que veremos com mais detalhes abaixo)
```sh
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
```

- OK, nesse ponto podemos ver que a denpender da opção que o usuário digitar o código redirecionará para funcionalidade da opção digitada, veja abaixo:
- Para cada opção que o usuário digitar acima, tem um "if" que verifica e executa a funcionalidade, por exemplo: ```if opcao == 1 ```
- No código abaixo temos o algoritimo da funcionalidade que representa o requisito 1 da atividade proposta (Inserir um item por vez).
```sh
  #Inserindo um de cada vez (req1)
    if opcao == 1:
        print('Digite:')
        print("1 - Para inserir um vértice")
        print("2 - Para inserir uma aresta")
        opcao2 = int(input("Opção: "))
        
        # Recebe o vertice e verifica se o mesmo já foi adicionado no grafo
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

        # Recebe o vértice de cada aresta
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
```

- Nesse ponto recebemos os vértices e as arestas do grafo em lote, requisito 2 da atividade proposta:
```sh
#Inserindo em lote (req2)
    if opcao == 2:
        
        # Recebe o nome do arquivo de vértices e de arestas
        arq_vert = input("Digite o nome do arquivo de vertices: ")
        arq_arest = input("Digite o nome do arquivo de arestas: ")
        
        # Ler o arquvio especifico e adiciona na lista especifica
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
```
## Como executar o sistema:

- [ATENÇÂO] - certifique-se que você tem ferramentas dependentes para obter o repósitorio no GitHub e para executar o sistema. Veja as ferramentas utilizadas no primeiro tópico desse readme. 
- 
- Primeiro voce precisa obter o diretório que contém o arquivo de execução do sistema ```main.py``` e os arquivos de dependência ```aero_a.txt```, ```aero_v.txt``` para no caso deseje obter o grafo em lote. Para obter o sistema você pode clonar esse repositório em sua maquina.

- Considerando que você tem o git instalado Em sua maquina, digite ```sh git clone https://github.com/EvanilsonLJS/grafos.git```

- Após o repositório clonado voce pode navegar para raiz do diretório ```grafos/```, e em seu terminal digite: ```python3 main.py```

- Por fim voce pode se divertir criando grafos, obrigado =).
