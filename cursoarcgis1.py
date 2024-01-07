#Import modules
import math

#Assign variables to numbers
a = -10
b = 0
c = 10

#Find the square root of numbers
numbers = [a, b, c]
raiz = []
for number in numbers:
    if number >= 0:
        raiz.append(math.sqrt(number))
    else:
        pass
print(raiz)