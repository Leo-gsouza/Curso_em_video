def fatorial(num):
    fatorial = 1
    for c in range(1,num+1):
        fatorial *= c
    return fatorial

def bhaskara(a, b, c):
    delta = (b**2) - 4*a*c
    if delta > 0:
        x1 = (- b + delta**0.5 )/(2*a)
        x2 = (- b - delta**0.5 )/(2*a)
        return x1, x2
    elif delta == 0:
        x = (-b + delta) /(2*a)
        return x
    else:
        info = 'Sem raiz'
        return info, delta
    
def somar(lista):
    soma = 0
    for c in lista:
        soma+= c
    return soma

def raiz(numero):
    raiz_n = numero **0.5
    return raiz_n



