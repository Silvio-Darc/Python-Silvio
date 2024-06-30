def bubbleSort(lis):
    n = len(lis)
    for i in range(n - 1):
        troca = False
        for j in range(0, n - i - 1):
            if lis[j][0] == lis[j + 1][0]:
                if lis[j][1] == lis[j + 1][1]:
                    if lis[j][2] > lis[j + 1][2]:
                        troca = True
                        lis[j], lis[j + 1] = lis[j + 1], lis[j]
                elif lis[j][1] > lis[j + 1][1]:
                    troca = True
                    lis[j], lis[j + 1] = lis[j + 1], lis[j]
            elif lis[j][0] > lis[j + 1][0]:
                troca = True
                lis[j], lis[j + 1] = lis[j + 1], lis[j]
    if not troca:
        return

while True:
    try:
        alunos = int(input())
        lista = []
        for aluno in range(alunos):
            nome, regiao, distancia = map(str, input().split())
            lista.append([int(distancia), regiao, nome])
        bubbleSort(lista)
        for aluno in lista:
            print(aluno[2])
    except EOFError:
        break
