import datetime

hoje = (datetime.datetime.now())

print(hoje.day)
print(hoje.month)
print(hoje.year)
print(hoje.minute)
print(hoje.second)
print(hoje.microsecond)
print(hoje.strftime('%W'))

meu_aniversario = datetime.datetime(1984, 11, 20)

print('Eu nasci no ano de:' + meu_aniversario.strftime('%Y'))
print('No mês de:' + meu_aniversario.strftime('%m'))
print('No dia:' + meu_aniversario.strftime('%d'))
