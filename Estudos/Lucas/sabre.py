def check(mat, x, y):
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            x_ = mat[j][i]
            if not(x == i and y == j) and x_ != 7:
                return False
    return True


def matrix(mat):
    height = len(mat)
    width = len(mat[0])

    for x in range(1, width - 1):
        for y in range(1, height - 1):
            if mat[y][x] == 42:
                if check(mat, x, y):
                    result = f"{x+1} {y+1}"
                    print(result)
                    return result
    return f"0 0"


mat1 = [
    [11, 12, 7, 7, 7, 13, 14],
    [15, 6, 7, 42, 7, 7, 42],
    [98, -5, 7, 7, 7, 42, 7],
    [-1, 42, 3, 9, 7, 7, 7],
]

mat2 = [
    [11, 12, 7, 7, 7, 13, 14],
    [15, 6, 7, 12, 7, 7, 42],
    [98, -5, 7, 7, 7, 42, 7],
    [-1, 42, 3, 9, 7, 7, 7],
]

mat3 = [
    [7, 7, 7],
    [7, 42, 7],
    [7, 7, 7],
]

assert matrix(mat1) == "4 2"
assert matrix(mat2) == "0 0"
assert matrix(mat3) == "2 2"
