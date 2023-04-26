num=1
cont=0
suma=0
while num!=0:
    num=int(input('ingrese numero'))
    cont=cont+1
    suma+=num
print(f'fueron ingresados {cont-1} numeros')
print(f"la suma de los numeros es {suma}")
print(f"el promedio es {suma/(cont-1)}")

