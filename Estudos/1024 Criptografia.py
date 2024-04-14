testes = int(input())
for teste in range(testes):
    entrada = input()
    resultado1 = ""
    resultado2 = ""
    resultadoFinal = ""
    for letra in entrada:
        if ord(letra) in range(65, 91) or ord(letra) in range(97, 123):
            resultado1 += chr(ord(letra) + 3)
        else:
            resultado1 += letra
    for letra in resultado1:
        resultado2 = letra + resultado2
    for posLetra in range(len(resultado2)):
        if posLetra < (len(resultado2) // 2):
            resultadoFinal += resultado2[posLetra]
        else:
            resultadoFinal += chr(ord(resultado2[posLetra]) - 1)
    print(resultadoFinal)
