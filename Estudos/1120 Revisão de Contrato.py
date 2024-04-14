entrada = input()
while entrada != "0 0":
    digFalho, valorCerto = map(str, entrada.split())
    valorFalho = ""
    for dig in range(len(valorCerto) - 1):
        if dig == 0 and valorCerto[dig] != digFalho:
            valorFalho += valorCerto[dig]
        elif valorCerto[dig] != digFalho and valorCerto[dig] != valorCerto[dig + 1]:
            valorFalho += valorCerto[dig]
    if valorCerto[len(valorCerto) - 1] != digFalho:
        valorFalho += valorCerto[len(valorCerto) - 1]
    if valorFalho == "":
        valorFalho = "0"
    print(valorFalho)
    entrada = input()
