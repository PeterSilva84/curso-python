import matplotlib.pyplot as plt

linguagens = ['C++', 'C#', 'Python', 'Java', 'Go']
votos = [100, 150, 350, 50, 60]

plt.bar(linguagens, votos, color='#820000', align="edge", width=0.1)
plt.title('Linguagens de programação x Quantidade de votos')
plt.xlabel('Linguagens de programção')
plt.ylabel('Votos por linguagem')
#plt.bar('linguagem, votos')
plt.show()
