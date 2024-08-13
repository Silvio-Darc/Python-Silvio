ordemMatriz = int(input())
while ordemMatriz != 0:
    matriz = []
    for i in range(1, ordemMatriz+1):
        linha = []
        for j in range(1, ordemMatriz+1):
            menor = maior = i
            if i < j:
                maior = j
            else:
                menor = j
            difMaior = (ordemMatriz + 1) - maior
            valor = ""
            if menor < difMaior:
                valor = menor
            else:
                valor = difMaior
            linha.append(str(valor).rjust(3, " "))
        matriz.append(linha)
    for lin in matriz:
        linha = " ".join(lin)
        print(linha)
    print()
    ordemMatriz = int(input())