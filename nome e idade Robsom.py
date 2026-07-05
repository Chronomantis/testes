nome = input('Qual seu nome?')
idade = int(input('Qual sua idade?'))

if nome == 'Robsom':
    print('Olá Robsom, seja bem vindo!')
elif idade < 18:
    print('Você não é o Robsom! E é menor de idade!')
elif idade > 100:
    print('Diferente do Robsom, você não é imortal!')