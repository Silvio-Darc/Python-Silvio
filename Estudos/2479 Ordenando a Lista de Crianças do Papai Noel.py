qtdCriancas = int(input())
lista = []
boas = 0
ruins = 0
for crianca in range(qtdCriancas):
    comportamento, nome = map(str, input().split())
    if comportamento == "+":
        boas += 1
    else:
        ruins += 1
    lista.append(nome)
for crianca in sorted(lista):
    print(crianca)
print("Se comportaram: %s | Nao se comportara,: %s" % (boas, ruins))
