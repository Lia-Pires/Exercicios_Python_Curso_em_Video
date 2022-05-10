produto = float(input('Digite o valor do produto: '))
precoComDesconto = produto * (1 - 0.05)
print('O valor do produto com desconto é de R${:.2f}'.format(precoComDesconto))
