"""escriba cuantas letras tiene cada linea en el coro del himno de soacha escriba las respuestas en otro archivo"""
himno=open("C:\\clon\\pythondaza\\Archivos\\coro.txt","r",encoding="utf-8")

for linea in himno.readlines():
    print(contador,linea)
    contador+=1