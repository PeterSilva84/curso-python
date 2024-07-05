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

print(f'Eu já vivi {hoje - meu_aniversario}.')

dias_vividos = hoje - meu_aniversario

dif_tempo = datetime.timedelta(1000)

dia_1000_depois = hoje + dif_tempo

print(dia_1000_depois)



