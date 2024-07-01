#TODO: Declarar as variaveis

nota1 = int(input("Entre com a primeira nota: "))
nota2 = int(input("Entre com a segunda nota: "))
media = (nota1+nota2)/2



if media == 10:
    print(f' Sua média foi {media} Aprovado com distinção.')
elif media >= 7:
    print(f' Sua média foi {media}  Aprovado.')
else:
    print(f'Sua média foi {media}, você é algum tipo de burro ?')