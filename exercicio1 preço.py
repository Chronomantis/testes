preco = float(input('digite o preço do produto: '))
percentual = float(input('digite o percentual de desconto (0-100%): '))

desconto = preco * (percentual / 100)
final = preco - desconto

print(f'o preço final do produto é {preco}. Desconto de {percentual}%')
print(f'o valor calculado de desconto: {desconto}. Valor final do produto: {final}')