
def dobro(num):
    return num * 2


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


lista_dobro = list(map(dobro, lista))

print(lista_dobro)