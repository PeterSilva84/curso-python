

nome = input('Entre com seu nome:').title()
sobrenome = input('Entre com seu último nome:').upper()
idade = int(input('Entre com sua idade:'))  # int precisa ser declarado porque o padrão de input é str

print(type(nome))
print(type(sobrenome))
print(type(idade))


print(f'Oi meu nome é {nome}  {sobrenome} e tenho {idade} anos de idade.')

