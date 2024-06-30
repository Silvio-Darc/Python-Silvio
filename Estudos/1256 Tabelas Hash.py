testes = int(input())
for teste in range(testes):
    enderecos, qtdNumeros = map(int, input().split())
    lista = []
    for _ in range(enderecos):
        lista.append([])
    nums = list(map(int, input().split()))
    for num in nums:
        resto = num % (enderecos)
        lista[resto].append(num)
    for i in range(len(lista)):
        linha = "%.i -> " % i
        if lista[i]:
            for j in lista[i]:
                linha += "%.i -> " % j
        linha += chr(92)
        print(linha)
    if teste != testes - 1:
        print()
