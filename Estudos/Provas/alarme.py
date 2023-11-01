h1, m1, h2, m2 = list(map(int, input().split()))
while h1 + m1 + h2 + m2 != 0:
    if h2 < h1:
        h2 += 24
    if h2 == h1 and m2 < m1:
        h2 += 24

    minutos_1 = h1 * 60 + m1
    minutos_2 = h2 * 60 + m2

    minutos_restantes = minutos_2 - minutos_1
    print(minutos_restantes)
    h1, m1, h2, m2 = list(map(int, input().split()))
