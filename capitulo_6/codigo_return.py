
def area_circunferencia():

    raio = float(input('Entre com o raio da circunferencia: '))
    pi = 3.14

    return f'{pi * raio ** 2} m²'

resultado = area_circunferencia()

print(resultado)