valor = int(input('Digite o valor do seu produto: '))


def calcular(valor): 
     while valor > 20:
        valor = (valor * 0.10) + valor
        print(f'O valor final do seu produto sera de: R${valor}')
        break


calcular(valor)