horaingre = int(input("Escriba la hora: "))
minutosingre = int(input("Escriba los minutos: "))
segundosingre = int(input("Escriba los segundos: "))

devolverSegundos = 0
devolverMinutos = 0
devolverHora = 0
         

if segundosingre < 59:
    segundosingre+=1
elif minutosingre >=59:
    if segundosingre >=59:
        segundos = devolverSegundos
    minutos=devolverMinutos
    horaingre+=1   
elif segundosingre >= 59:
    segundos = devolverSegundos
    minutosingre+=1
elif minutosingre >=59:
    if segundosingre <=59:
        segundosingre+=1
    minutosingre+=0

           
if horaingre == 24:
    hora= devolverHora
    
print(f"{horaingre}: {minutosingre}: {segundosingre}")