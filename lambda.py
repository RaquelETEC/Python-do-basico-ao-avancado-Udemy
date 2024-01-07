#é uma função pequena sem nome
#pode ter varios argumentos mas somente uma expressão
#muito utilizada em outras  funções 
#clean code
#pode ser atribuida a variaveis ou funções  

def soma(x):
    return x + 10

print(soma(2))

#criando a função lambda 

#argumento é o x 
#depois expressão
somar10 = lambda x,y : x + y + 10 

print(somar10(2,6))