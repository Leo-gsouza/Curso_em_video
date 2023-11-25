def metade(valor):
    return valor/2

def dobro(valor):
    return valor*2

def aumentar(valor, percentual):
    return valor + valor*percentual/100

def diminuir(valor, percentual):
    return valor - valor*percentual/100

def cifrao(valor = 0, cifrao= 'R$'):
    return f'{cifrao}{valor:.2f}'.replace('.',',')