import random

def llenado(tam,rango):
    lista=[]
    lista=[random.randrange(rango) for i in range(tam)]
    return lista

l1=llenado(5,10)
l2=llenado(5,10)
print(f"lista numero uno {l1}")
print(f"lista numero dos {l2}")
def sumar(lista):
    sumar=0
    for i in  lista :
        sumar+=i
    return  sumar

sumalista1=(sumar(l1))
sumalista2=(sumar(l2))

if sumalista1>sumalista2:
    print(f"la suma de la lista numero uno  es mayor a la suma de la lista numero 2: {sumalista1} ")
else :
    print(f"la suma de la lista numero dos es mayor a la suma de la lista numero 1: {sumalista2} ")
    
def mayor(lista):
    mayor=0
    for k in lista:
        if k >mayor:
            mayor=k
    return mayor

def menor(lista):
    menor=0
    for k in lista:
        if k <menor:
            menor=k
    return menor

mayorl1=(mayor(l1))
mayorl2=(mayor(l2))
def mayorlistas(mayorl1,mayorl2):
    if mayorl1>mayorl2:
        mayorlistas=mayorl1
    else:
        mayorlistas=mayorl2
    return mayorlistas
    
print("el mayor de las dos listas es ",mayorlistas(mayorl1,mayorl2)) 
    
    
menorl1=(menor(l1))
menorl2=(menor(l2))

def menorlistas(menorl1,menorl2):
    if menorl1<menorl2:
        menorlistas=menorl1
    else:
        menorlistas=menorl2
    return menorlistas

print("el menor de las dos listas es ",menorlistas(menorl1,menorl2))
    
     
listaconjunto=l1+l2
def promedio(lista):
    promedio=sumar(lista)/len(lista)
    return promedio

print ("el promedio de las dos listas conjunto es :",promedio(listaconjunto))

promediol1=(promedio(l1))
promediol2=(promedio(l2))
promedioconjunto=(promedio(listaconjunto))
if promediol1>promedioconjunto:
    print(f"el promedio de la lista uno es mayor a de la lista conjunto : {promediol1}")
else:print(f"el promedio de la lista conjunto es superior a de la lista uno : {promedioconjunto}")
if promediol2>promedioconjunto:
    print(f"el promedio de la lista dos es mayor a de la lista conjunto : {promediol2}")
else:print(f"el promedio de la lista conjunto es superior a de la lista dos : {promedioconjunto}")

def pares(lista):
    pares=0
    for i in lista:
        if i%2==0:
            pares+=1
    return pares
def impares(lista):
    impares=0
    for i in lista:
        if i%2==1:
            impares+=1
    return impares
            
paresl1=(pares(l1))
paresl2=(pares(l2))

if paresl1>paresl2:
    print("la lista numero uno tiene mayor cantidad de pares con la cantidad de :",paresl1)
elif paresl1==paresl2:
    print("las dos listas tienen la misma cantidad de impares con la cantidad de :",paresl1)
else:
    print("la lista numero dos tiene mayor cantidad de pares que la lista numero  uno con la cantidad de :",paresl2)
    
imparesl1=(impares(l1))
imparesl2=(impares(l2))

if imparesl1>imparesl2:
    print("la lista numero uno tiene mayor cantidad de impares que la lista numero dos con la cantidad de : ",imparesl1)
elif imparesl1==imparesl2:
    print("las dos listas tienen la misma cantidad de impares con la cantidad de :",imparesl1)
else:
    print("la lista numero dos tiene mayor cantidad de impares que la lista numero uno con la cantidad de : ",imparesl2)
    

