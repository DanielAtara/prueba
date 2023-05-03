numero1=int(input("ingrese el primer numero"))
numero2=int(input("ingrese el segundo numero"))
numero3=int(input("ingrese el tercer numero"))
numero4=int(input("ingrese el cuatro numero"))


if numero1 > numero2 and numero1 > numero3 and numero1 > numero4:

    print(f"{numero1}es mayor que todos los otros numeros")

elif  numero2 > numero1 and numero2 > numero3 and numero2 > numero4:

    print(f"{numero2}es mayor que todos los otros numeros")

elif numero3 > numero1 and numero3 > numero2 and numero3 > numero4: 

    print(f"{numero3}es mayor que todos los otros numeros")

else :

    print(f"{numero4}es mayor que todos los otros numeros")






