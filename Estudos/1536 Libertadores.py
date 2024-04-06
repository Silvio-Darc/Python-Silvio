def verificar(time1: int, time2: int) -> bool:
    if time1 == time2:
        return False
    elif time1 > time2:
        print("Time 1")
    else:
        print("Time 2")
    return True


def calcularPontos (placares: list, time: int, adversario: int):
    pontos = 0
    for placar in placares:
        if placar[time] > placar[adversario]:
            pontos += 3
        elif placar[time] == placar[adversario]:
            pontos += 1
    return pontos


for _ in range(int(input())):
    placarIda = list(map(int, input().split(" x ")))
    placarVolta = list(map(int, input().split(" x ")))
    placarVolta.reverse()
    pontosTime1 = calcularPontos([placarIda, placarVolta], 0, 1)
    pontosTime2 = calcularPontos([placarIda, placarVolta], 1, 0)
    saldoTime1 = placarIda[0] + placarVolta[0]
    saldoTime2 = placarIda[1] + placarVolta[1]
    golsFeitosForaDeCasaTime1 = placarVolta[0]
    golsFeitosForaDeCasaTime2 = placarIda[1]

    if not verificar(pontosTime1, pontosTime2):
        if not verificar(saldoTime1, saldoTime2):
            if not verificar(golsFeitosForaDeCasaTime1, golsFeitosForaDeCasaTime2):
                print("Penaltis")
