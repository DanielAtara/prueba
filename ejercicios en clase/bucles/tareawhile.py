while True:
    
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))

    
    if num1 > num2:
        mayor = num1
        menor = num2
        break
    elif num1 < num2:
        mayor = num2
        menor = num1
        break
    else:
        print("Los números son iguales. Introduce números diferentes.")

    while resultado!=0:    
    resultado = mayor - menor
    if resultado > menor:
        resultado -= menor


print("El resultado es:", resultado)