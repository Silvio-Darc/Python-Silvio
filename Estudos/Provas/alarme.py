# entrada vai ser algo como 23 32 0 12 
# o primeiro e o segundo valor são as horas e minutos do horário atual
# o terceiro e o quarto valor são as horas e minutos do alarme selecionado para o futuro
# o código deve retornar quanto tempo falta até o alarme tocar, em minutos
h1, m1, h2, m2 = list(map(int, input().split()))

while h1 + m1 + h2 + m2 != 0:
    if h2 < h1:
        h2 += 24
    if h2 == h1 and m2 < m1:
        h2 += 24

    print((h2 * 60 + m2) - (h1 * 60 + m1))
    h1, m1, h2, m2 = list(map(int, input().split()))
