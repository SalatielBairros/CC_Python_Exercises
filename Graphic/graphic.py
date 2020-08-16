import matplotlib.pyplot as plt
from random import randrange, seed

notas_matematica = ['Matemática',8,7,6,6,7,7,8,10]
notas_portugues = ['Português',9,9,9,8,5,6,8,5]
notas_geografia = ['Geografia',10,10,6,7,7,7,8,7]
notas = [notas_matematica, notas_portugues, notas_geografia]

plt.title('Resultado')
plt.xlabel('Provas')
plt.ylabel('Notas')

for materia in notas:
  nX = range(len(materia) - 1)
  plt.plot(nX, materia[1:], marker='o')  

plt.show()