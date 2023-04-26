#en este ejercicio se piden un numero  hasta que este sea factor de el otro  numero ingresado  
x,y=3,5
cont=1 # se asigna un contador y su respectivo valor 
while not(x%y==0 or y%x==0): # se realiza la validacion de que los numeros ingresados sea factor  
    print(f'intento numero {cont}' ) # se muestra la cantidad de veces que se a intentado ingresar los numeros  
    x=int(input('ingrese numero')) # se piden nuevos numeros para realizar todo el anterior proceso
    y=int(input('ingrese numero'))
    cont+=1 # se incrementa el numero de intentos de uno en uno 

print(f'{x} y {y} son factor') # se imprime si los dos numeros son factores 