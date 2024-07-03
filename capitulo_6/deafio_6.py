
def temperatura_fahreheint():

    celsius = float(input('Entre com o valor da temperatura: '))
    f = (celsius * 1.8) + 32

    return f'{f} Farenheit'

resultado = temperatura_fahreheint()

print(resultado)
