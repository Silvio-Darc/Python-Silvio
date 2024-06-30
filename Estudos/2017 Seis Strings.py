stringx = input()
k = int(input())
strings = []
indiceMenor = 0
menor = len(stringx)
for _ in range(5):
    strings.append(input())

for indice in range(5):
    string = strings[indice]
    diferencas = len(string)
    for caractere in range(len(string)):
        if string[caractere] == stringx[caractere]:
            diferencas -= 1
    if diferencas < menor:
        indiceMenor = indice
        menor = diferencas
if menor > k:
    print(-1)
else:
    print(indiceMenor + 1)
    print(menor)
