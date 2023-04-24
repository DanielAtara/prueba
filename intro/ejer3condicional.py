pregunta=input("que area desea calcular el circulo o el triangulo")

if pregunta=="triangulo":

    base=float(input("ingrese la base del triangulo"))
    altura=float(input("ingrese la altura"))

    ope1=(base*altura)/2

    print(f"el area del triangulo es {ope1}")

elif pregunta=="circulo" :

    radio=float(input("ingrese el radio del circulo"))
    pi=3.1416
    
    ope2=(radio**2)*pi

    print(f"el area del circulo es {ope2}")
else :
    print("ingrese un termino valido ")



