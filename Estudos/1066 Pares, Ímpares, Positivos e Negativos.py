par = 0
impar = 0
positivo = 0
negativo = 0

for _ in range(5):
    elemento = int(input())
    if elemento % 2 == 0:
        par += 1
    else:
        impar += 1
    if elemento > 0:
        positivo += 1
    elif elemento < 0:
        negativo += 1

print(str(par), "valor(es) par(es)")
print(str(impar), "valor(es) impar(es)")
print(str(positivo), "valor(es) positivo(s)")
print(str(negativo), "valor(es) negativo(s)")
