idade = int(input("Entre com sua idade: "))

if idade >= 18:
    print("Pode dirigir!")
else:
    print("Pega o busão!")


user = ("default user")

if input('Entre com usuário:' ) == 'admin':
    print('Bem vindo!')
else:
    print('Usuário não tem as credenciais necessárias!')