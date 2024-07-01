senha = input('Cadastre uma senha de 6 dígitos: \n')

while True:
    if len(senha) != 6:
        senha = input('Só 6 digitos mané \n'
                      'Cadastre uma senha de 6 digitos: \n')
        continue
    else:
        break

print('Cadastro realizado com sucesso!')
