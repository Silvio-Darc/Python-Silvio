entrada = input()
teste = 1
while entrada != "0 0 0 0":
    print("Teste", teste)
    x1, y1, x2, y2 = map(int, entrada.split())
    total = 0
    for meteorito in range(int(input())):
        xm, ym = map(int, input().split())
        if x1 <= xm <= x2 and y2 <= ym <= y1:
            total += 1
    print(total)
    teste += 1
    entrada = input()
