testes = int(input())
for teste in range(testes):
    entrada = input()
    resultado1 = ""
    resultadoFinal = ""
    for posletra in range(len(entrada)):
        if ord(entrada[posletra]) < 65 or ord(entrada[posletra]) > 122 or 91 <= ord(entrada[posletra]) <= 96:
            resultado1 = entrada[posletra] + resultado1
        else:
            resultado1 = chr(ord(entrada[posletra]) + 3) + resultado1
    for posLetra in range(len(resultado1)):
        if posLetra < (len(resultado1) // 2):
            resultadoFinal += resultado1[posLetra]
        else:
            resultadoFinal += chr(ord(resultado1[posLetra]) - 1)
    print(resultadoFinal)
