dicionario = {"1": 2, "2": 5, "3": 5, "4": 4, "5": 5, "6": 6, "7": 3, "8": 7, "9": 6, "0": 6}
for _ in range(int(input())):
    total = 0
    for i in input():
        total += dicionario[i]
    print(total, "leds")
