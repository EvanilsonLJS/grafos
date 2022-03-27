

def saida(quant, list_1, list_2, list_3):

    for i in range(quant): #Dando erro
        if (i == list_1[i - 1]):
            break
    
        print(list_1[i], "→", list_1[i + 1], list_2[i], " ", list_3[i])