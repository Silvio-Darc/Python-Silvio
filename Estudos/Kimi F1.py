numeroPilotos, numeroVoltas = map(int, input().split())

melhorVolta = "99999999999999999999999999999999999999999999999999999999999999999"

melhoresVoltas = []

pilotosMelhorVolta = []

pilotos = []

voltaFinal = []

for _ in range(numeroPilotos):
    linha = input().split()
    pilotos.append(linha[0])  # adiciona o número do piloto
    voltaFinal.append(linha[numeroVoltas])  # vai determinar a posição
    for i in range(numeroVoltas):
        if linha[i+1] < melhorVolta:
            melhorVolta = linha[i+1]  # vai salvar a melhor volta
            pilotosMelhorVolta.append(linha[0])  # vai determinar qual piloto fez a melhor volta


n = len(voltaFinal)
for i in range(n-1):
    for j in range(n-i-1):
        if voltaFinal[j] > voltaFinal[j+1]:
            voltaFinal[j], voltaFinal[j+1] = voltaFinal[j+1], voltaFinal[j]
            pilotos[j], pilotos[j + 1] = pilotos[j + 1], pilotos[j]

pilotos.reverse()
voltaFinal.reverse()

if pilotos.index(pilotosMelhorVolta) > 9: Preciso levar em conta os pilotos com melhores voltas iguais.
    print("NENHUM")
else:
    print(pilotosMelhorVolta)