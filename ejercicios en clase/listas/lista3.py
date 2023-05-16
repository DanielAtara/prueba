import random 
lista1=[]
lista2=[]
contador,contador1,contador2=0,0,0
sum1,sum2,sum3,sum4,sum5=0,0,0,0,0
mayor1,mayor2=0,0
menor1,menor2=1000000,1000000
tam=random.randint(10,15)

for i in range(tam):
    num=random.randrange(10)
    lista1.append(num)
print(lista1) 

for e in lista1:
    sum1+=e
    contador+=1
print(f"{sum1}")

tam=random.randint(10,15)

for i in range(tam):
    num=random.randrange(10)
    lista2.append(num)
print(lista2) 

for e in lista2:
    sum2+=e
    contador+=1
print(f"{sum2}")

if sum1>sum2:
    print (f"laa suma mas alta es {sum1}")

else :
    print (f"la suma mas alta es {sum2}")

for k in lista1:
    if k >mayor1:
        mayor1=k
    if k <menor1:
        menor1=k
        


        
for i in lista2:
    if k >mayor2:
        mayor2=k
    if k <menor2:
        menor2=k

if mayor1>mayor2:
    print (f"el numero mayor es {mayor1}")

else:
    print(f"el numero mayor es {mayor2}") 
    
if menor1<menor2:
    print (f"el numero menor es {menor1}")
else:
    print(f"el numero menor es {menor2}")

conjunto=lista1+lista2
print(conjunto)
for e in conjunto:
    sum3+=e
    contador1+=1
    promedioconj=sum3//contador

for o in lista1:
    sum4+=o
    contador2+=1
    promedio1=sum3//contador

if promedioconj>promedio1:
    print("el promedio conjunto esta por encima del arreglo de la primera lista ")
elif promedioconj==promedio1:
    print(f"los dos promedios son iguales {promedio1} {promedioconj}" )
else :
    print("el promedio de la lista uno esta por encima de promedio conjunto ")

