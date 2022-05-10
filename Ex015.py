dias = float(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos km o carro rodou? '))
preco = (dias * 60) + (km * 0.15)
print('O carro foi utilizado por {:.1f} dias e todos {:.1f} Km, o valor total do aluguel é R${:.2f}.'.format(dias, km, preco))

