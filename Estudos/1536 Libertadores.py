# Critério de desempate:
    # Normal) pontos.
    # 1) saldo de gols (número de gols a favor menos o número de gols contra).
    # 2) mais gols marcados na casa do adversário.
    # 3) disputa por pênaltis.


def comparar(time1, time2):
    if time1 > time2:
        print("Time 1")
    elif time1 < time2:
        print("Time 2")
    else:
        return 1



for _ in range(int(input())):
    jogo1 = list(map(int, input().split(" x ")))
    jogo2 = list(map(int, input().split(" x ")))
    pontosTime1 = 0
    pontosTime2 = 0
    golsTime1 = jogo1[0] + jogo2[1]
    golsTime2 = jogo1[1] + jogo2[0]
    if jogo1[0] > jogo1[1]:
        pontosTime1 += 3
    elif jogo1[0] == jogo1[1]:
        pontosTime1 += 1
        pontosTime2 += 1
    else:
        pontosTime2 += 3
    if jogo2[0] > jogo2[1]:
        pontosTime2 += 3
    elif jogo2[0] == jogo2[1]:
        pontosTime1 += 1
        pontosTime2 += 1
    else:
        pontosTime1 += 3

    if comparar(pontosTime1, pontosTime2) == 1:
        if comparar(golsTime1, golsTime2) == 1:
            if comparar(jogo2[1], jogo1[1]) == 1:
                print("Penaltis")


