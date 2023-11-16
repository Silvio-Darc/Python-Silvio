for _ in range(int(input())):
    a, b = map(str, input().split())
    if a[len(a) - len(b):len(a)] == b:
        print('encaixa')
    else:
        print('nao encaixa')
