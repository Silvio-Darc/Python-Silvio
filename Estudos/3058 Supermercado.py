menor_valor = float('inf')
for _ in range(int(input())):
    valor, peso = map(float, input().split())
    if valor * (1000 / peso) < menor_valor:
        menor_valor = valor * (1000 / peso)
print(f"{menor_valor:.2f}")

