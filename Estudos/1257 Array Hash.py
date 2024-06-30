testes = int(input())
for teste in range(testes):
    soma = 0
    linhas = int(input())
    for linha in range(linhas):
        entrada = input()
        for caractere in range(len(entrada)):
            soma += caractere
            soma += ord(entrada[caractere]) - 65
            soma += linha
    print(soma)
