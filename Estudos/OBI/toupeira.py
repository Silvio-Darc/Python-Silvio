s, t = map(int, input().split())
tuneis = []
tuneis_reverso = []
caminhos_possiveis = 0
for tunel in range(t):
    x, y = map(int, input().split())
    tuneis.append((str(x), str(y)))
    tuneis_reverso.append((str(y), str(x)))
for rota in range(int(input())):
    entrada = input().replace(" ", "")
    qtd_saloes = int(entrada[0])
    rotas_impossiveis = 0
    if qtd_saloes == 2:
        if ((entrada[1], entrada[2]) not in tuneis) and ((entrada[1], entrada[2]) not in tuneis_reverso):
            rotas_impossiveis += 1
    else:
        for i in range(1, qtd_saloes-1):
            if ((entrada[i], entrada[i+1]) not in tuneis) and ((entrada[i], entrada[i+1]) not in tuneis_reverso):
                rotas_impossiveis += 1
    if rotas_impossiveis == 0:
        caminhos_possiveis += 1
print(caminhos_possiveis)
