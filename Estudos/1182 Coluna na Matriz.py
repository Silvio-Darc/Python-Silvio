# Subprogramas
def soma(vetor: list):
    somatorio = 0
    for val in vetor:
        somatorio += val[colunaOperacao]
    return somatorio


def media(vetor: list):
    somatorio = soma(vetor)
    mediatorio = somatorio / nLinhas
    return mediatorio


# Main
colunaOperacao = int(input())
operacao = input()
nLinhas = 12
nColunas = 12
matriz = []
for _ in range(nLinhas):
    linha = []
    for _ in range(nColunas):
        linha.append(float(input()))
    matriz.append(linha)
if operacao == "S":
    print("%.1f" % soma(matriz))
else:
    print("%.1f" % media(matriz))
