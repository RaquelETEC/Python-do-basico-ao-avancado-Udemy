from array import array

#usamos o array quando há muitos itens , milhares 
#mas assim fica lento 

letras = ['a','b','c'] #string usamos o u 
numeros_i = [10,20,30] #inteiros usamos o i 
numeros_f = [1.2,2.2,3.1] #não interos usamos o f 

print(letras)
print(numeros_i)
print(f'{numeros_f} \n')

letras = array('u', letras)
numeros_i =array('i', numeros_i)  
numeros_f = array('f', numeros_f)


print(letras)
print(numeros_i)
print(numeros_f)



def somar(x):
    return x + 10

print(somar(2))