# num=1
# print(type(num))
# num="sena"
# print(type(num))
num=1 #se le asigna un numero a la variable 
cont=0 # se realiza el contador 
sum=0 #
menor=1000000 #mientras numero sea menor que 10000 es menor
mayor=0 # mientras numero sea mayor a 0 sera mayor 
while num!=0: # mientras numero 0 no sea escrito realize
    num=int(input('ingrese numero')) # un ingreso de otro numero 
    cont=cont+1 # se mostrara la cantidad de veces que se a ingresado un numero 
    sum=sum+num # se sumara los numeros ingresados 
    if num>mayor: # se evalua cual de los numeros ingresados es mayor 
        mayor=num
    if num<menor and num!=0: # se evalua cual de los numeros ingresados es menor 
        menor=num
# se imprimen cada uno de los procesos anteriormente nombrado 
print(f'fueron ingresados {cont-1} numeros') # cantidad de numeros ingresados 
print(f'La suma es {sum}') # se suma los numeros nombrados 
print(f'El promedio es {sum/(cont-1)}') # se saca el promedio de los numeros ingresados 
print(f'El mayor es {mayor}') # se saca el mayor de los numeros ingresados 
print(f'El menor es {menor}') # se saca el menor de los numeros ingresados 