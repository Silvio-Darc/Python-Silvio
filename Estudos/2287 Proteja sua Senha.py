n = int(input())
teste = 1


while n != 0:
    senha = ""
    valores = []
    for _ in range(6):
        valores.append([0] * 10)

    for linha in range(n):
        entrada = input().split()

        a = [int(entrada[0]), int(entrada[1])]
        b = [int(entrada[2]), int(entrada[3])]
        c = [int(entrada[4]), int(entrada[5])]
        d = [int(entrada[6]), int(entrada[7])]
        e = [int(entrada[8]), int(entrada[9])]

        variaveis = [a, b, c, d, e]

        letras = [entrada[10], entrada[11], entrada[12], entrada[13], entrada[14], entrada[15]]
        alfabeto = ['A', 'B', 'C', 'D', 'E']

        for i in range(6):
            valor_atual = valores[i]
            letra_atual = letras[i]
            par = variaveis[alfabeto.index(letra_atual)]
            valor_atual[par[0]] += 1
            valor_atual[par[1]] += 1

    for i in range(6):
        casa = valores[i]
        digito = casa.index(n)
        senha += f"{digito} "
    print(f"Teste {teste}")
    print(senha)
    print()
    teste += 1
    n = int(input())

