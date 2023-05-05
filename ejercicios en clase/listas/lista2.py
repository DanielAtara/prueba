import random

lista=[]
tam=random.randint(10,20)
print(tam)

for i in range(tam):
    num=random.randrange(10)
    lista.append(num)
print(lista) 
num=int(input("ingrese un numero "))

while num not in lista:
      num=int(input("el numero no se encuentra ingrese otro"))
      

        
for b in lista:
     contador=0
     for c in lista:
         if num==c:
             contador+=1

print(f"el {num} esta {contador} veces ")

for i in range(len(lista)):
    if num == lista[i]:
        print(f'{lista[i]} esta en la posicion {i}')