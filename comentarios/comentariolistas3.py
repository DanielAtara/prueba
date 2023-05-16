import random #se importa una libreria para poder usar la funcion de generar numeros aleatorios 
lista=[] # se crea una lista vacia 
cuadrado=[] 
tam=random.randint(5,10) #se asignan un valor a una variable y se usa una funcion que genera numeros aleatorios dependiedo el rango que se le asigne
print(tam)
for i in range(tam):#se crea un for que este en el rando de la variable anteriormente asignada 
    num=random.randrange(100) #se asigna un valor a una variable usando una funcion cuyo proposito es generar numeros aleatorios de cero hasta el numero asignado 
    lista.append(num) #se agraga un valor a una lista 
print(lista)

for i in range(len(lista)): 
    cuadrado.append(lista[i]**2)
    #lista[i]=lista[i]**2
    # print(lista[i]*lista[i])
    # print(lista[i]**2)
    # print(math.pow(lista[i],2))

print(cuadrado)