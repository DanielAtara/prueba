def creararchivo():
                nombrearchivo=input("ingrese el nombre del archivo que desea crear: ")
                with open(nombrearchivo) as name:
                     numerolineas=[]
                     a=name.readline()
                     for i in a :
                         numerolineas.append(i)
                print(f"su documento{numerolineas}")
creararchivo()
