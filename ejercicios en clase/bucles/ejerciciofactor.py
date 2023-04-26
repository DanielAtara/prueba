num1=int(input("ingrese el primer numero"))
num2=int(input("ingrese el primer numero"))
contador=1
while num1 % num2 == 1 or num2 % num1 == 1:
    print(f"su cantidad de intentos es {contador}")
    num1=int(input("ingrese el primer numero"))
    num2=int(input("ingrese el segundo numero"))
    
print(f"{num1}y{num2} son factores")    