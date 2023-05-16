#[], {}, (), {()}
x=100 #se asignan un valor a la variable 
print(type(x)) #se consulta el tipo de dato de la variable usando la funcion type
x='Soacha' #se altera el valor de la variable por un valor de cadena de texto 
print(type(x)) #vuelve a consultar el tipo de dato actual de la variable 
lista=['python',100,[1,2,3,[]],'a'] # se genera una lista y se asignan distintos elementos cada uno con un tipo de dato distinto 
print(type(lista)) # consulta el tipo de dato que se presenta dando como resultado un dato llamado lista 
print(len(lista)) # se ejecuta una funcion para medir la longitud de la lista 
print(lista[0]) # se imprime el elemento cero 
print(lista[1]) # se imprime el elemento uno 
print(lista[3]) # se imprime el elemento tres
print(lista[-4]) # se imprime el elemento -4 teniendo en cuenta de que al usar un numero negativo se iniciara la cuenta de fin hasta el principio 
del lista[-2] # seutiliza para eliminar un elemento de la lista enm este caso el menos dos 
print(lista) # se imprime la lista 

"""
#cuenta1=cuenta()
#cuenta2=cuenta()
#cuenta3=cuenta()
#cuenta1.deposit()
#print(type(cuenta1))
#cuenta2.deposit()
#cuenta3.deposit()