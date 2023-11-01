valores = str.split(input())
a = int(valores[0])
b = int(valores[1])

q = a / b
r = a - (b*int(q))

print(f'{int(q)} {int(r)}')
