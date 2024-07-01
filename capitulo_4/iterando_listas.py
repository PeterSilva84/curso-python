import time

num = int(input("informe o tamanho de sua lista: "))

lista = []

for numero in range(1, num + 1):
    lista.append(numero)

print(lista)

for elemento in lista:
    if elemento % 2 == 0:
        lista.remove(elemento)

print(lista)

for i in range(1, 6):
    lista.append(i)
    print(lista)
    time.sleep(1)

for i in range(5, 1,-1):
    lista.remove(i)
    print(lista)
    time.sleep(1)


