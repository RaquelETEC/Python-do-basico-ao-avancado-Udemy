import datetime

nome = input('Qual seu nome: ')
data_nascimento = input('Digite a data do seu nascimento (no formato AAAA-MM-DD): ')
cidade = input('Qual sua cidade: ')

# Converta a string de data em um objeto datetime
data_nascimento = datetime.datetime.strptime(data_nascimento, '%Y-%m-%d')

# Obtenha o ano atual
ano_atual = datetime.datetime.now().year

# Calcule a idade
idade = ano_atual - data_nascimento.year

print(f'O {nome} tem {idade} anos e mora na cidade de {cidade}')