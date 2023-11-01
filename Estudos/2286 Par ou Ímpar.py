t = 1
numero_partidas = int(input())  # Ler o número de partidas
while numero_partidas != 0:  # Para cada teste realizado
    jogador_par = input()  # Ler nome do jogador_par
    jogador_impar = input()  # Ler nome do jogador_impar

    print('Teste', str(t))  # Imprimir o nome do teste

    for _ in range(numero_partidas):  # Enquanto número de partidas != 0
        numero_partidas -= 1  # Diminuir uma partida
        dedos = input()
        dedos1 = int(str.split(dedos)[0])
        dedos2 = int(str.split(dedos)[1])
        resultado = (dedos1 + dedos2) % 2

        if resultado == 0:  # Se o resultado for par
            print(jogador_par)  # Imprima nome_par

        else:  # Senão
            print(jogador_impar)  # Imprima nome_impar

    print()  # Imprimir linha em branco

    t += 1  # Incrementar o teste em 1

    # Repetir o processo
    numero_partidas = int(input())
    