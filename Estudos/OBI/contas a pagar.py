saldo = int(input())
acougue = int(input())
farmacia = int(input())
padaria = int(input())

if saldo >= acougue + farmacia + padaria:
    print("3")
elif saldo >= acougue + farmacia or saldo >= acougue + padaria or saldo >= padaria + farmacia:
    print("2")
elif saldo >= acougue or saldo >= padaria or saldo >= farmacia:
    print("1")
else:
    print("0")
