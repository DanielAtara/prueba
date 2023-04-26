
n=int(input('ingrese numero')) # se declara las variables dependindo el numero que ingrese la persona 
i=1 # se asigna una variable contadora 
while i<n: # se valoriza si la variable contadora es menor al numero ingresado por el usuario 
    if i%7==0: # si el i es modulo de 7 
        print(f'{i} es multiplo de 7') # se muestra el siguiente mensaje 
    else:
        print(i) # de igual forma se siguen impirmiendo los numeros y se van incrementando 
    i+=1