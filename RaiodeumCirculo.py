import numpy as numpy

raio = float(input('Digite o valor do raio: '))


dia = 0
peri = 0
area = 0

dia = raio * 2

peri = 2 * raio * numpy.pi

area = numpy.pi * raio**2

print(f'O valor do diametro e: {round(dia,2)}')
print(f'O valor do perimetro e: {round(peri,2)}')
print(f'O valor da area e: {round(area,2)}')


