
alunos_notas = {'João':[7, 4, 5], 'Maria' : [5, 8, 9], 'Leo': [6, 7, 7], 'Pedro': [7, 4, 10]}

alunos_aprovados = dict(filter(lambda alunos: round(sum(alunos[1]) / len(alunos[1]), 2) >= 7, alunos_notas.items()))

print(*alunos_aprovados)

medias=(sum(n) for n in alunos_notas.values())
print(medias)