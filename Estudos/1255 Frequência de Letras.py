# Computers account for only 5% of the country's commercial electricity consumption.
for _ in range(int(input())):
    palavra = input().lower()
    letras = []
    frequencia_letras = []
    palavra_final = []
    for i in palavra:
        letras.append(ord(i))
    for i in range(26):
        frequencia_letras.append(letras.count(97 + i))
    valor_maximo = max(frequencia_letras)
    for i in range(26):
        if frequencia_letras[i] == valor_maximo:
            palavra_final.append(chr(97+i))
    print(''.join(palavra_final))