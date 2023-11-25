numeros = []

for c in range(1,6):
    numero = int(input(f"Digite o {c}º número » "))
    numero_elevado = numero**2 if numero < 5 else numero
    numeros.append(numero_elevado)

numeros.sort()
print(numeros)

