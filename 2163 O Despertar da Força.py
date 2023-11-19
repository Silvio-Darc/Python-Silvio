def criar_matriz():
    matriz = []
    i, j = map(int, input().split())
    for indice in range(i):
        matriz.append(list(map(int, input().split())))
    return matriz


def verificar_matriz(matriz):
    for i in range(1, len(matriz) - 1):
        for j in range(1, len(matriz[1]) - 1):
            if matriz[i][j] == 42:
                if matriz[i-1][j-1] == 7 and matriz[i-1][j] == 7 and matriz[i-1][j+1] == 7:
                    if matriz[i][j-1] == 7 and matriz[i][j+1] == 7:
                        if matriz[i+1][j-1] == 7 and matriz[i+1][j] == 7 and matriz[i+1][j+1] == 7:
                            return f"{i+1} {j+1}"
    return "0 0"


print(verificar_matriz(criar_matriz()))
