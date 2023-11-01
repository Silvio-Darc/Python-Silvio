# Ler entrada do número de colunas
numero_colunas = int(input())
colunas_formula = []
colunas_perfeitas = []
somatorio = []

# Ler entrada do número de blocos em cada coluna
# Separar essa entrada em uma lista
colunas_atual = list(map(int, input().split()))
for i in range(numero_colunas):
    colunas_formula.append(1*i)
n = sum(colunas_formula)
numero_principal = (sum(colunas_atual) + n) / numero_colunas
# Para cada lista dessa entrada
for i in range(numero_colunas):
    # Achar a escada perfeita dessa lista usando a fórmula
    colunas_perfeitas.append(numero_principal - (1*i))
# Reverter essa sequência
colunas_perfeitas.reverse()
# Para cada elemento num raio do número de colunas
for i in range(numero_colunas):
    k = colunas_atual[i] - colunas_perfeitas[i]
    # Se lista_atual[elemento] - lista_perfeita[elemento] >= 0
    if k >= 0:
        # Adicionar essa subtração a uma lista somatório
        somatorio.append(k)
# Se lista somatório = []
if colunas_perfeitas[0] % 1 != 0:
    # Imprimir -1
    print('-1')
# Senão
else:
    # Imprimir somatorio somatório
    print(f'{sum(somatorio):.0f}')
