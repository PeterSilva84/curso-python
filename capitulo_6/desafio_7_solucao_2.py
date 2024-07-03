def bissexto():
    ano = int(input("Digite o ano: \n"))
    if ano % 400 == 0:
        print('é bissexto!')
    elif ano % 4 == 0:
        if ano % 100 != 0:
            print('é bissexto!')
        else:
            print('não é bissexto')
    else:
        print('Não é bissexto!')

bissexto()