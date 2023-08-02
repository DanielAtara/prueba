
himno=open("C:\\clon\\pythondaza\\Archivos\\himno.txt","r",encoding="utf-8")
cont=1
linea=himno.readline()
for line in himno:
    cont+=1
    print(cont,line)
    
    