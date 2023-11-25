

def buscar(texto, palavra):
    quantidade = 0
    for p in texto.split():
        if p.strip().title() == palavra.strip().title():
            quantidade += 1
    return quantidade

texto = str(input('Copie e Cole o texto que desejar: '))
palavra = str(input('Digite a palavra que deseja consultar: '))

quantidade = buscar(texto, palavra)
print(f'A palavra {palavra} foi encontrada {quantidade} vezes no texto')