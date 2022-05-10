from math import trunc
num = float(input('Digite um número: '))
#numint = num - (math.fmod(num, 1))
#print('Você digitou o número {} e sua parte inteira é {}.'.format(num, numint))
print('Você digitou o número {} e sua parte inteira é {}'. format(num, trunc(num)))
