def bubbleSort(lis):
    n = len(lis)
    for i in range(n - 1):
        troca = False
        for j in range(0, n - i - 1):
            if lis[j][1] == lis[j + 1][1]:
                if lis[j][0] < lis[j + 1][0]:
                    troca = True
                    lis[j], lis[j + 1] = lis[j + 1], lis[j]
            elif lis[j][1] > lis[j + 1][1]:
                troca = True
                lis[j], lis[j + 1] = lis[j + 1], lis[j]
    if not troca:
        return


while True:
    try:
        entrada = input()
        while entrada != "":
            dicionario = {}
            # Criar o dicionário
            for let in entrada:
                if let in dicionario:
                    dicionario[let] += 1
                else:
                    dicionario[let] = 1
            # Ordenar o dicionário crescentemente pelo valor usando Bubble
            lista = list((i, dicionario[i]) for i in dicionario)  # Crio uma lista com tuplas do tipo (valor, 'chave')
            bubbleSort(lista)
            # Imprimir cada tupla
            for tupla in lista:
                print("%s %s" % (ord(tupla[0]), tupla[1]))
            print()
            entrada = input()
    except EOFError:
        break
