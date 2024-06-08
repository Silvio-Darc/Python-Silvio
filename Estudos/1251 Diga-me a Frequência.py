while True:
    try:
        dados = open("entrada", "r")
        entrada = dados.readline()
        dados.close()
        while entrada != "":
            dicionario = {}
            # Criar o dicionário
            for let in entrada:
                if let in dicionario:
                    dicionario[let] += 1
                else:
                    dicionario[let] = 1
            # Ordenar o dicionário crescentemente pelo valor usando Insertion Sort
            lista = list((i, dicionario[i]) for i in dicionario)  # Crio uma lista com tuplas do tipo (valor, 'chave')
            for i in range(1, len(lista)):
                chave = lista[i]
                j = i - 1
                while j >= 0 and chave[1] < lista[j][1]:
                    lista[j+1] = lista[j]
                    j -= 1
                lista[j+1] = chave
            # Verificar se, caso existam quantidades iguais, a maior letra venha primeiro
            for i in range(len(lista)-1):
                chave = lista[i]
                if lista[i][1] == lista[i+1][1] and ord(lista[i][0]) < ord(lista[i+1][0]):
                    lista[i] = lista[i+1]
                    lista[i+1] = chave
            # Imprimir cada tupla
            for tupla in lista:
                print("%s %s" % (ord(tupla[0]), tupla[1]))
            print()

            entrada = input()
    except EOFError:
        break
