n = int(input())
while n != 0:
    entrada = list(map(int, input().split()))
    if sum(entrada) % n == 0:
        rodadas = 0
        lista_ideal = []
        n_ideal = sum(entrada) / n
        for i in range(n):
            n_ideal = int(sum(entrada) / n)
            lista_ideal.append(n_ideal)
        while entrada != lista_ideal:
            for i in range(n):
                if i + 1 > n - 1:
                    i -= n - 1
                if entrada[i + 1] - entrada[i] > 0:
                    rodadas += 1
                    entrada[i + 1] -= 1
                    entrada[i] += 1
                elif entrada[i + 1] - entrada[i] < 0:
                    rodadas += 1
                    entrada[i + 1] += 1
                    entrada[i] -= 1
        print(rodadas)
        n = int(input())
    else:
        print(-1)
        n = int(input())
