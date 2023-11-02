# dado um inteiro n q eh o numero de criancas
# as proximas n entradas eh  numero de doces q aquela crianca tem
# duas criancas sao chamadas. quem tem mais da pra quem tem menos
# repita o processo ate todos tenham o msm numero de doces
# quantas rodadas foram necessarias?
# se for impossivel imprime -1
# para sair digite 0

def doces(lista):
    rodadas = 1
    if sum(lista) % len(lista) != 0:
        print(-1)
        return -1
    else:
        pobre = min(lista)
        rico = max(lista)
        while pobre != rico:
            lista[lista.index(pobre)] += 1
            lista[lista.index(rico)] -= 1
            print(lista)
            rodadas += 1
            pobre = min(lista)
            rico = max(lista)
    print(rodadas)
    return rodadas


assert doces([2, 2, 2]) == 1
assert doces([1, 2, 3]) == 2
assert doces([2, 3, 4, 5]) == -1
assert doces([2, 3, 4, 6]) == -1
assert doces([2, 3, 5, 6]) == 4
