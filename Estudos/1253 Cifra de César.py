n = int(input())
for _ in range(n):
    palavra = input()
    chave = int(input())
    palavra_nova = ""
    for i in range(len(palavra)):
        letra = ord(palavra[i])
        letra_nova = letra - chave
        while letra_nova < 65:
            letra_nova += 26
        palavra_nova += chr(letra_nova)
    print(palavra_nova)
