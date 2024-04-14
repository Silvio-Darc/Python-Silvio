entrada = input()
while entrada != "0 0":
    digFalho, valorCerto = map(str, entrada.split())
    valorFalho = ""
    for dig in range(len(valorCerto)):
        if valorCerto[dig] != digFalho:
            valorFalho += valorCerto[dig]
    if valorFalho == "" or valorFalho == "0" * len(valorFalho):
        valorFalho = "0"
        print(valorFalho)
        entrada = input()
    else:
        lista = []
        for letra in valorFalho:
            lista.append(letra)
        while lista[0] == "0":
            lista.remove("0")
        print("".join(lista))
        entrada = input()
