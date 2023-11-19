n, i, f = map(int, input().split())
vetores = list(map(int, input().split()))
pares = 0

for o in range(n-1):
    for j in range(n-1-o):
        if f >= vetores[o] + vetores[j+o+1] >= i:
            pares += 1
print(pares)
