for teste in range(int(input())):
    entrada = input().lower()
    # Criar o dicionário (Ele já vem em ordem alfabética)
    dicionario = dict()
    for letra in entrada:
        if ord(letra) in range(97, 123):
            if letra not in dicionario:
                dicionario[letra] = 1
            else:
                dicionario[letra] += 1
    # Achar os maiores e printar
    maiorValor = 0
    for letra in list(dicionario):
        if dicionario[letra] > maiorValor:
            maiorValor = dicionario[letra]
    for letra in sorted(dicionario):
        if dicionario[letra] == maiorValor:
            print(letra, end="")
    print()
