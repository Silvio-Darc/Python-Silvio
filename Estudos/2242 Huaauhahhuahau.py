def criar_risada(entrada):
    risada = []

    for i in range(len(entrada)):
        if entrada[i] in ['a', 'e', 'i', 'o', 'u']:
            risada.append(entrada[i])
    return risada


def inverter_risada(risada_original):
    risada_invertida = []
    for n in range(len(risada_original)):
        risada_invertida.append(risada_original[len(risada_original) - n - 1])
    return risada_invertida


a = criar_risada(input())
b = inverter_risada(a)

if a == b:
    print('S')
else:
    print('N')
