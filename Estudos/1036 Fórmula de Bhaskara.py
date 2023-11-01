from math import sqrt
valores = str.split(input())

a = float(valores[0])
b = float(valores[1])
c = float(valores[2])
delta = (b**2)-(4*a*c)

if delta < 0 or a == 0:
    print("Impossivel calcular")
else:
    r1 = (-b + sqrt(delta)) / (2*a)
    r2 = (-b - sqrt(delta)) / (2*a)
    print("R1 = {:.5f}\n".format(r1) +
          "R2 = {:.5f}".format(r2))
