def para_minutos(horas, minutos):
    return horas * 60 + minutos


def alarme(h1, m1, h2, m2):
    if h2 < h1 or (h2 == h1 and m2 < m1):
        h2 += 24

    minutos_atual = para_minutos(h1, m1)
    minutos_alarme = para_minutos(h2, m2)
    minutos_restantes = minutos_alarme - minutos_atual
    print(minutos_restantes)
    return minutos_restantes


assert alarme(0, 0, 0, 1) == 1
assert alarme(0, 1, 0, 0) == 1439
assert alarme(0, 0, 1, 1) == 61
assert alarme(0, 0, 23, 59) == 1439
assert alarme(23, 59, 0, 0) == 1
assert alarme(0, 0, 0, 0) == 0
