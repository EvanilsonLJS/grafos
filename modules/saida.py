

def saida(quant, list_1, list_2, list_3):

    for i in range(quant): 
        print(list_1[i], "→", list_1[i + 1], list_2[i], " ", list_3[i])
        
        if (i == list_1[range(quant) - 1]):
            break
    
        