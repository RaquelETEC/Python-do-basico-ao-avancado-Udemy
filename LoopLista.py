valores = [60,80,10,150,170]

for x in valores: 
    print(f'O valor final do produto é de  R$: {x}' )


cor_cliente = input('Digite a cor desejada ')

cores = {'amarelo','verde', 'azul', 'vermelho'}

#lower deixa em minusculo as coisas 
if cor_cliente.lower() in cores: 
    print('\nEm estoque')
else:
    print('\n Não temos estoque')