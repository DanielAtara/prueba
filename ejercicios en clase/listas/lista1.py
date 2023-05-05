import random
import math
lista=[]
cuadrado=[]
sum=0
contador=0
mayor=0
menor=100000
resta=0
cuadrado=0
division=0

tam=random.randint(10,20)
print(tam)

for i in range(tam):
    num=random.randrange(100)
    lista.append(num)
print(lista) 

for e in lista:
    sum+=e
    contador+=1
    
print(sum)
promedio=sum//contador
print(f"el promedio de la lista es {promedio}")

for k in lista:
    if k >mayor:
        mayor=k
    if k <menor:
        menor=k
print (f"el numero mayor es{mayor}" )    
print(f"el numero menor es{menor}")
#desviacion estandar 
for q in lista:
    resta=q-promedio
    cuadrado=resta**2
    division=cuadrado//contador
    raiz=math.sqrt(division)
print(f"la desviacion estandar es {raiz}")


    
    
    
    
    