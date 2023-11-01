valor = float(input())
notas = [0, 0, 0, 0, 0, 0]
moedas = [0, 0, 0, 0, 0, 0]
tipos_notas = [100, 50, 20, 10, 5, 2]
tipos_moedas = [1, 0.5, 0.25, 0.10, 0.05, 0.01]
for i in range(6):
    notas[i] = valor // tipos_notas[i]
    valor %= tipos_notas[i]
for i in range(6):
    moedas[i] = valor / tipos_moedas[i]
    valor %= tipos_moedas[i]
    valor = round(valor, 2)

print("NOTAS:")
for i in range(6):
    print(f"{notas[i]:.0f} nota(s) de R$ {tipos_notas[i]:.2f}")

print("MOEDAS:")
for i in range(6):
    print(f"{moedas[i]:.0f} moeda(s) de R$ {tipos_moedas[i]:.2f}")
