valores = input()

a = float(str.split(valores)[0])
b = float(str.split(valores)[1])
c = float(str.split(valores)[2])

triangulo = (a * c) / 2
circulo = 3.14159 * (c ** 2)
trapezio = ((a + b) * c) / 2
quadrado = b ** 2
retangulo = a * b

print(
    'TRIANGULO: ' "%.3f" % triangulo + '\n'
    'CIRCULO: ' "%.3f" % circulo + '\n'
    'TRAPEZIO: ' "%.3f" % trapezio + '\n'
    'QUADRADO: ' "%.3f" % quadrado + '\n'
    'RETANGULO: ' "%.3f" % retangulo
    )

