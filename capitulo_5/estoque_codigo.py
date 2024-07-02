estoque = {}

print(type(estoque))
print('\n------- vamos atualizar o estoque no sistema--------')

while True:
    produto = input('Informe o nome do produto (ou enter para sair): ')
    if produto:
        quantidade = int(input(f'Quanto de {produto} temos em estoque: '))
        estoque[produto] = quantidade
        continue
    else:
        break
print('\n-----------Resumo de estoque-------------\n')
if len(estoque) > 0:
    for produto, quantidade in estoque.items():
        print(f'{produto}: {quantidade} unidades.')
    print(f'\n Temos um total de {sum(list(estoque.values()))} produtos no estoque. ')
else:
    print('O estoque está vazio.')