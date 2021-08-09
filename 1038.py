#1038

valores = input().split(" ")

codigo = float(valores[0])
quantidade = float(valores[1])

if float(valores[0]) == 1:
    n = 4.00 * float(valores[1])
elif float(valores[0]) == 2:
    n = 4.50 * float(valores[1])
elif float(valores[0]) == 3:
    n = 5.00 * float(valores[1])
elif float(valores[0]) == 4:
    n = 2.00 * float(valores[1])
else:
    n = 1.50 * float(valores[1])

print(f"Total: R$ {n:.2f}")
