from math import hypot
op = float(input('Qual a medida do cateto oposto? '))
ad = float(input('Qual a medida do cateto adjacente? '))
#hip = ((op**2)+(ad**2))**(1/2)
hip = hypot(op, ad)
print('O cateto oposto é {:.2f}, o cateto adjacente é {:.2f} e a hipotenusa é {:.2f}'.format(op, ad, hip))
