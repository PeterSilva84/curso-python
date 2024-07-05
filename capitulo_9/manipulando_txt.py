

meu_arquivo = open('meu_texto.txt', 'x')

meu_arquivo.write('Meu arquivo teste')

meu_arquivo.close()

with open('meu_texto.txt', 'a') as file:

    file.writelines(['\nLinha1 ', '\nLinha2 ', '\nFui!'])

