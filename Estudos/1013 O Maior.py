entrada = input()

valores = str.split(entrada)

a = float(valores[0])
b = float(valores[1])
c = float(valores[2])


def maior(arg1, arg2):
    return ((arg1+arg2)+abs(arg1-arg2)) / 2


maior_final = maior(maior(a, b), c)

print(str(int(maior_final)), 'eh o maior')
