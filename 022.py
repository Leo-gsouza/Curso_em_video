nome = str(input("Informe o nome completo: ")).strip()

print(nome.upper())#LEONARDO GARCIA DE SOUZA
print(len(nome) - nome.count(" "))#21
print(nome.find(" "))#8
# opção 1
letras_nome = nome.find(" ")
print(f"Nome = {nome[:letras_nome]}")

# opção 2
nome_separado = nome.split()
print(f"Nome = {nome_separado[0]}")
print(f"Sobrenome  = {nome_separado[-1]}")
