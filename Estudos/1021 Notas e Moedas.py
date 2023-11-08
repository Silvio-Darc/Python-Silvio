valor = float(input())
notas = [0, 0, 0, 0, 0, 0]
moedas = [0, 0, 0, 0, 0, 0]
tipos_notas = [100, 50, 20, 10, 5, 2]
tipos_moedas = [100, 50,25, 10, 5, 1]
for i in range(6):
    notas[i] = valor // tipos_notas[i]
    valor %= tipos_notas[i]
valor *= 100
for i in range(6):
    moedas[i] = valor // tipos_moedas[i]
    valor %= tipos_moedas[i]


print("NOTAS:")
for i in range(6):
    print(f"{notas[i]:.0f} nota(s) de R$ {tipos_notas[i]:.2f}")

print("MOEDAS:")
for i in range(6):
    print(f"{moedas[i]:.0f} moeda(s) de R$ {tipos_moedas[i] / 100:.2f}")
