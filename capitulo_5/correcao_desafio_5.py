#TODO: Receber os itens e armazenar na lista

lista = []

while True:
    item = input('Entre com dado(ou enter para sair: )')
    if item:
        lista.append(item)
        continue
    else:
        break
    print(lista)

#TODO: Eliminar os itens repetidos

lista_nova = list(set(lista))
print(lista_nova)

#TODO: Ordenar a lista

lista_nova.sort()

print(lista_nova)


