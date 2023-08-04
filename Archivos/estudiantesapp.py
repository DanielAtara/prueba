from estudiantes import*
from operaciones import*
import csv
estudiante=[]
with open("C:\\clon\\pythondaza\\Archivos\\Saber_11__2019-2.csv") as filecsv:
    filereader=csv.reader(filecsv)
    for row in filereader:
        objeto=estudiantes(row[0],row[14],row[16],row[2],row[80])
        print(objeto.verDatos())
        estudiante.append(objeto)
    for ap in estudiante:
        documento=ap.gettp()
        estrato=ap.getestrato()
        genero=ap.getgenero()
        puntaje=ap.getpuntajeMatematicas()
    print(moda(documento))
    print(moda(estrato))
    print(moda(genero))
    print(puntaje)
        






