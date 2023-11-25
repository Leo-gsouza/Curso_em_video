

def buscar(texto, letra):
    qtdd_letras = 0
    qtdd_especifica = 0

    for l in texto:
        if l.lower() == letra.lower():
            qtdd_especifica += 1
            qtdd_letras += 1
        else:
            qtdd_letras += 1
    
    return qtdd_letras, qtdd_especifica
        
texto = str(input('Copie e Cole o texto que desejar: '))
letra = str(input('Digite a letra que deseja consultar: '))
quantidade = buscar(texto, letra)

qtdd_letras, qtdd_especifica = buscar(texto, letra)
print(f'O texto tem {qtdd_letras} letras.\nA letra [{letra.upper()}] foi encontrada {qtdd_especifica} vezes no texto')