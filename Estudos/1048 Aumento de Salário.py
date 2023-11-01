def aumento(percentual, salario):
    porcentagem = 1 + percentual / 100
    novo_salario = salario * porcentagem
    reajuste_ganho = novo_salario - salario
    print(f"Novo salario: {novo_salario:.2f}")
    print(f"Reajuste ganho: {novo_salario - salario:.2f}")
    print(f"Em percentual: {percentual:.0f} %")
    return

salario = float(input())
if salario <= 400:
    aumento(15.00, salario)
elif salario <= 800.00:
    aumento(12, salario)
elif salario <= 1200.00:
    aumento(10, salario)
elif salario <= 2000.00:
    aumento(7, salario)
else:
    aumento(4, salario)
