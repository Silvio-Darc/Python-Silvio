def calcularAprovacao(chamada:str):
    presencas = medicos = 0
    for dia in chamada:
        if dia == "P":
            presencas += 1
        elif dia == "M":
            medicos += 1
    frequencia = (presencas / len(chamada) - medicos)
    if frequencia < 0.75:
        return True
    return False


for _ in range(int(input())):
    quantidadeEstudantes = int(input())
    listaAlunos = input().split()
    presencaAlunos = input().split()
    reprovados = []
    for aluno in range(quantidadeEstudantes):
        variavel = calcularAprovacao(presencaAlunos[aluno])
        if variavel:
            reprovados.append(listaAlunos[aluno])
    print(" ".join(reprovados))


