# Ler a quantidade de observações
n = int(input())
t = 1

# Enquanto a quantidade de observações for diferente de 0 faça
while n != 0:
    # Criar lista de tamanho 6 contendo sublistas de tamanho 10,
    #   que são contadores inicializados com o valor 0. Cada um dos
    #   contadores armazena a quantidade de vezes que o dígito respectivo
    #   apareceu nas observações.
    contadores = []
    for _ in range(6):
        contadores.append([0] * 10)
    # Versão Pythonica -> contadores = [[0] * 10 for _ in range(6)]

    # Para cada observação faça
    for _ in range(n):
        # Ler mapeamento entre pares de dígitos e as 5 letras
        # Ler a observação composta por 6 letras
        linha = input().split()
        mapa = []
        for k in range(5):
            mapa.append([int(linha[k * 2]), int(linha[k * 2 + 1])])

        # Para cada um das 6 posições da senha faça
        for i in range(6):
            contador_atual = contadores[i]
            # Incrementa os contadores associados aos dois dígitos que
            #   estão mapeados para a letra informada pelo usuário
            letra_informada = linha[10 + i]
            par = mapa[ord(letra_informada) - ord("A")]
            contador_atual[par[0]] += 1
            contador_atual[par[1]] += 1

    # Para cada um das 6 posição da senha faça
    print(f"Teste {t}")
    for i in range(6):
        contador_atual = contadores[i]
        # Coletar o dígito que mais recebeu votos
        maior_conhecido = -1
        digito_maior_conhecido = None
        for digito in range(10):
            if contador_atual[digito] > maior_conhecido:
                maior_conhecido = contador_atual[digito]
                digito_maior_conhecido = digito
        # Mostrar dígito encontrado
        print(digito_maior_conhecido, end=' ')
    print()
    print()

    # Ler a quantidade de observações
    n = int(input())
    t += 1