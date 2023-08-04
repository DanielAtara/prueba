def moda (datos):
    maximo=0
    for a in datos :
        contador=0
        for b in datos:
            if a==b:
                contador+=1
        if contador>maximo:
            maximo=contador
            moda1=a
    return f"la moda  es {datos}"
