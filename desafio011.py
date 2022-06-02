print('Este script calculara a quantidade de tinta para pintar uma parede de acordo com sua medida.')
l = float(input('Digite a largura da parede em metros: '))
a = float(input('Digite a altura da parede em metros: '))
area = a*l
litros = area/2
print('Sua parede tem a area de {:.2f}m² será necessário {:.1f} litros de tinta para pintar essa area!'.format(area, litros))
