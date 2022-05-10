import math
ang = float(input('Digite um ângulo: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print('O ângulo digitado foi {:.2f}, seu seno é {:.2f}, seu cosseno é {:.2f} e sua tangente é {:.2f}.'.format(ang,sen,cos,tan))
