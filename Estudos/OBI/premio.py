pontos = int(input())
pontos += (int(input()) * 2)
pontos += (int(input()) * 3)
if pontos >= 150:
    print("B")
elif pontos >= 120:
    print("D")
elif pontos >= 100:
    print("P")
else:
    print("N")
