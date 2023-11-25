def potencia(volt=0, ampere=0, ohm=0):
    if volt > 0 and ampere > 0:
        return f'{volt*ampere:.1f} watts'
    elif volt > 0 and ohm > 0:
        return f'{volt**2 / ohm:.1f} watts'
    elif ampere > 0 and ohm > 0:
        return f'{ampere**2 * ohm:.1f} watts'
    else:
        return f'\n\033[1;31mErro! Você digitou apenas uma grandeza\033[m\
            \n{"▄"*21}\n│ Tensão = {volt:<7}{"│":>3}\n│ Corrente = {ampere:<5}{"│":>3}\n│ Resistencia = {ohm:<4}{"│":>1}\n{"▀"*21}\n'

def tensao(watt=0, ampere=0, ohm=0):
    if watt > 0 and ampere > 0:
        return f'{watt/ampere:.1f} volts'
    elif watt > 0 and ohm > 0:
        return f'{watt**0.5 * ohm:.1f} volts'
    elif ampere > 0 and ohm > 0:
        return f'{ampere * ohm:.1f} volts'
    else:
        return f'\n\033[1;31mErro! Você digitou apenas uma grandeza\033[m\
            \n{"▄"*21}\n│ Potencia = {watt:<6}{"│":>2}\n│ Corrente = {ampere:<5}{"│":>3}\n│ Resistencia = {ohm:<4}{"│":>1}\n{"▀"*21}\n'
    
def corrente(watt=0, volt=0, ohm=0):
    if watt > 0 and volt > 0:
        return f'{watt/volt:.1f} amperes'
    elif watt > 0 and ohm > 0:
         return f'{watt**0.5 / ohm**0.5:.1f} amperes'
    elif volt > 0 and ohm > 0:
            return f'{volt / ohm:.1f} amperes'
    else:
        return f'\n\033[1;31mErro! Você digitou apenas uma grandeza\033[m\
            \n{"▄"*21}\n│ Potencia = {watt:<6}{"│":>2}\n│ Tensão = {volt:<6}{"│":>4}\n│ Resistencia = {ohm:<4}{"│":>1}\n{"▀"*21}\n'
    
def resistencia(watt=0, volt=0, ampere=0):
    if watt > 0 and volt > 0:
        return f'{volt**2 / watt:.1f} ohm'
    elif watt > 0 and ampere > 0:
         return f'{watt/ ampere**2:.1f} ohm'
    elif volt > 0 and ampere > 0:
            return f'{volt / ampere:.1f} ohm'
    else:
        return f'\n\033[1;31mErro! Você digitou apenas uma grandeza\033[m\
            \n{"▄"*21}\n│ Potencia = {watt:<6}{"│":>2}\n│ Tensão = {volt:<6}{"│":>4}\n│ Corrente = {ampere:<5}{"│":>3}\n{"▀"*21}\n'

