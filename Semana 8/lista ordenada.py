def remove_repetidos (lista):

    lista = sorted (lista)
    saida = []

    y = -1
    for i in lista:

        x = lista [y]
        if y < len(lista) and i != x:
            saida.append (i)

        y += 1        


    return saida
