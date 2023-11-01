precos = [4.00, 4.50, 5.00, 2.00, 1.50]
codigo, quantidade = map(int, input().split())
total = precos[codigo - 1] * quantidade
print(f"Total: R$ {total:.2f}")
