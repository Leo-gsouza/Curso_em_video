#Modularização

from uteis import numeros

numero = int(input('Digite um número: '))
fat = numeros.fatorial(numero)

print(f'O fatorial de {numero} é {fat}')
