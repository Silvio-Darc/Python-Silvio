def alarme(h1, m1, h2, m2):
    if h2 < h1:
        h2 += 24
    if h2 == h1 and m2 < m1:
        h2 += 24

    minutos_1 = h1 * 60 + m1
    minutos_2 = h2 * 60 + m2

    minutos_restantes = minutos_2 - minutos_1
    print(minutos_restantes)
    return minutos_restantes


assert alarme(0, 0, 0, 1) == 1
assert alarme(0, 0, 1, 1) == 61
assert alarme(0, 0, 23, 59) == 1439
assert alarme(23, 59, 0, 0) == 1
assert alarme(0, 0, 0, 0) == 0
