n = int(input())
while n != 0:
    rodadas = 0
    doces = list(map(int, input().split()))
    n_alunos = len(doces)
    for i in range(n_alunos):
        if i+1 > n_alunos - 1:
            i -= n_alunos - 1
        if doces[i+1] - doces[i] > 0:
            rodadas += 1
            doces[i+1] -= 1
            doces[i] += 1
        elif doces[i+1] - doces[i] < 0:
            rodadas += 1
            doces[i+1] += 1
            doces[i] -= 1
        else:
            print(rodadas)
            n = int(input())
