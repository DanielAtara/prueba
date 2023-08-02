
contador=1
himno=open("C:\\clon\\pythondaza\\Archivos\\himno.txt","r",encoding="utf-8")
for linea in himno.readlines():
    print(contador,linea)
    contador+=1
        