numero = int(input("Digite um número: "))
fatorial = numero
cont = 0

while cont != numero-1:
    cont += 1
    multiplicador = numero - cont
    fatorial *= multiplicador
    
print(f"Fatorail de {numero} = {fatorial}")