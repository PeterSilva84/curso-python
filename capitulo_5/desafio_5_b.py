s = set()

while True:

    item = input('Entre com dado (ou entre para sair): ')
    if item:
        s.add(int(item))
        continue
    else:
        break
lista_final = list(sorted(s))

print(lista_final)