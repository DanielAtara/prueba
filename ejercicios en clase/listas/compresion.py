import random 
import math
tam =random.randrange(5,10)

lista=[random.randrange(10)for i in range(tam)] 

print(lista)
lista2=[math.sqrt(e) if e%2==0  else e**2 for e in lista]
print(lista2)