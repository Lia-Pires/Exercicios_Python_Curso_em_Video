largura = float(input('Digite a largura da parede em metros: '))
altura = float(input('Digite a altura da parede em metros: '))
area = largura * altura
litrosTinta = area / 2

print ('Para pintar {}m² serão necessários {} litros de tinta'.format(area, litrosTinta))
