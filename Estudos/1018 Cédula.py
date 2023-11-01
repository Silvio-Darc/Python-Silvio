valor = int(input())

nota100 = valor // 100
nota50 = (valor % 100) // 50
nota20 = (valor % 100 % 50) // 20
nota10 = (valor % 100 % 50 % 20) // 10
nota5 = (valor % 100 % 50 % 20 % 10) // 5
nota2 = (valor % 100 % 50 % 20 % 10 % 5) // 2
nota1 = (valor % 100 % 50 % 20 % 10 % 5 % 2) // 1

print(f'{valor}\n'
      f'{nota100} nota(s) de R$ 100,00\n'
      f'{nota50} nota(s) de R$ 50,00\n'
      f'{nota20} nota(s) de R$ 20,00\n'
      f'{nota10} nota(s) de R$ 10,00\n'
      f'{nota5} nota(s) de R$ 5,00\n'
      f'{nota2} nota(s) de R$ 2,00\n'
      f'{nota1} nota(s) de R$ 1,00')
