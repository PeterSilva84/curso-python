
def numeros_pares(num):
    return num % 2 == 0

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista_pares = list(filter(numeros_pares, lista))

print(lista_pares)