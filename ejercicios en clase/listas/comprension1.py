import random 


longitud=random.randrange(20,30)
lista=[round(random.random()*5,2) for i in range(longitud)] 
print (lista)
for i in range(longitud):
    for j in range(i+1,longitud):
        if lista[i]>lista[j]:
            aux=lista[i]
            lista[i]=lista[j]
            lista[j]=aux
print (lista)

# aprobados=[ i for  i in lista if i>=3 ]
# print (aprobados)
# reprobados=[ e for  e in lista if e<3 ]
# print (reprobados)
# listadeuno=[o for o in lista if o<1]
# print (listadeuno)
# listadedos=[p for p in lista if p>=1 and p<2]
# print (listadedos)
# listadetres=[ q for q in lista if q>=2 and q<3]
# print (listadetres)
# listadecuatro=[ w for w in lista if w>=3 and w<4]
# print (listadecuatro) 
# listadecinco=[ r for r in lista if r>=4 and r<=5]
# print (listadecinco)