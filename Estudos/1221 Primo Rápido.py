def e_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True


for teste in range(int(input())):
    num = int(input())
    if e_primo(num):
        print("Prime")
    else:
        print("Not Prime")
