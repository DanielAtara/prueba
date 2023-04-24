distancia=float(input("ingrese la distancia en centimetros"))
pregunta=input("escriba a que distancia desea convertir.(metros o kilometros)")

if pregunta=="metros":

    ope1=distancia*0.01

    print(f"la distancia en metros es {ope1}")

elif pregunta=="kilometros":

    ope2=distancia*0.00001

    print(f"la distancia e kilometros es {ope2}")

else:

    print("escriba una unidad metrica valida")