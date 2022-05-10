nome = str(input('Digite seu nome completo: ')).strip()
#.strip tira os espaços antes e depois
print('Analisando seu nome.. ')
print('Seu nome em maíuculas é {}' .format(nome.upper()))
print('seu nome em minúscular é {}' .format(nome.lower()))
print('Seu nome tem ao todo {} letras' .format(len(nome)-nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))

