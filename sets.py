#------------ VERIFICA SE TEM ITEM DUPLICADO NA LISTA ---------------# 

list1 = [10, 20,30,50]
list2 = [10,20,60,70]

num1 = set(list1) #perdeu os index
num2 = set(list2)

print(num1 | num2)#Union Ele junta mas sem duplicar itens qe ja apareceram 

print(num1 - num2 )#Diference , tira todos os itens da da lista 2 que estao dentro da lista 1 (10e 20) sobra 30 e 50 

print(num1 ^ num2 )#msotra apenas os valores que são unicos em cada lista

print (num1 & num2)#o que é duplicado 
print()

#-------------sets--------------#

s1 ={1,2,3,4,5,6}

s1.update([6,7,8,9])
s1.remove(9) #se nao tem o item ele avisa
s1.discard(90) #se nao tem o item ele nao avisa 


#------------funções----------------#
set1 ={'a','b','c'}
set2 ={'a','d','e'}
set3 ={'c','d','g'}

set4 = set1.intersection(set2)
print(set4)
set4 = set1.union(set2)
print(set4)
