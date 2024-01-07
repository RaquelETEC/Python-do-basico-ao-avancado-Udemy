#-------no default voce define valor padrao 
def boas_vindas(nome, quantidade):
    print(f'Ola {nome}')
    print(f'temos {str(quantidade)} laptops em estoque')



boas_vindas('raquel',4)

#-------default voce define valor padrao 

def boas_vindas(nome, quantidade=6):
    print(f'Ola 2 {nome}')
    print(f'temos {str(quantidade)} laptops em estoque2')

boas_vindas('raquel')

#--retorno
def somatoria(numero1, numero2):
    return numero1 + numero2 

resultado = somatoria(1,5)

print(f'O resultado é: {resultado}')

#passando varios argumentos 


def soma(*numeros):
    resultado = 0
    for num  in numeros:
        resultado += num 
    return resultado

x = soma(2,3,1,6)

print(f'A soma é: {x}')



#passando varios parametros mas com identificação 

def agencia(**carro):
    return carro 

print(agencia(marca='Gol', cor ='Branca', motor=1.0, placa = 1246))
print(agencia(marca='Pneu', cor ='Preto', motor=2.2))