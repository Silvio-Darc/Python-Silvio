n = int(input())
while n != 0:
    for i in range(1, n+1):
        linha = ''
        for j in range(1, n+1):
            a = abs(i - j) + 1
            linha += str(a).rjust(3, " ") + " "
        print(linha.rstrip())
    print()
    n = int(input())
