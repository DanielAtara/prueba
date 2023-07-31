
while True:
    print("""
      1.crear un archivo
      2.ingresar datos
      3.ver la cantidad de digitos en el archivo
      
      """)
    desicion=input("ingrese el numero del proceso que desea realizar:")
    match desicion:
        case "1":
            nombrearchivo=input("ingrese el nombre del archivo que desea crear: ")
            def creararchivo(archivo):
                file1=open(archivo, "wt")
                file1.close()
                lineas=[]
                file2=open(archivo, "rt")
                a=file2.readlines()
                for i in a:
                    lineas.append(i)
                file2.close()
                print(f"su documento tiene",len(a),"lineas")
            creararchivo(nombrearchivo)
        case "2":
            def ingresodatos():
                nombre=input("digite su nombre")
                apellido=input("digite su apellido")
                telefono=input("ingrese su numero telefonico")
                dirrecion=input("ingrese su dirreccion de residencia")
                file=open(nombrearchivo,"wt")
                file.write(nombre+"\n"+apellido+"\n"+telefono+"\n"+dirrecion+"\n")
                file.close()
                
            ingresodatos()
                
                
    