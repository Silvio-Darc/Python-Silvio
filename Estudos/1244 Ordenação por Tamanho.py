def contarLetras(palavra):
    tamanho = 0
    for letra in palavra:
        tamanho += 1
    return tamanho


for teste in (range(int(input()))):
    entrada = input().split()
    tamanhoPalavras = []
    for palavraEntrada in entrada:
        tamanhoPalavras.append(contarLetras(palavraEntrada))
    # Selection Sort dupla
    # Loop principal do Bubble Sort
    #tamanho = len(tamanhoPalavras)
    #for i in range(tamanho - 1):
        #for j in range(tamanho - i - 1):
            #if tamanhoPalavras[j] > tamanhoPalavras[j + 1]:
                # Troca os elementos de posição
                #tamanhoPalavras[j], tamanhoPalavras[j + 1] = tamanhoPalavras[j + 1], tamanhoPalavras[j]
                #entrada[j], entrada[j + 1] = entrada[j + 1], entrada[j]

    # Imprime a lista ordenada
    entrada.sort(reverse=True, key=len)
    for i in range(len(entrada)):
        if i == len(entrada) - 1:
            print(entrada[i])
        else:
            print(entrada[i], end=" ")
