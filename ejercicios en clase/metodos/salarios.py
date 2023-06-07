class empleado:
    def __init__ (self,nombre,cargo,salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario
    
    def getnombre(self):
        return self.nombre
    def setnombre(self,nombre):
        self.nombre = nombre
    def getcargo(self):
        return self.cargo
    def setcargo(self,cargo):
        self.cargo = cargo
    def getsalario(self):
        return self.salario
    def setsalario(self,salario):
        self.salario = salario
    
    def salariohoras(self):
        salariodias=self.salario//30
        salariohora=salariodias//8
        
        return salariohora 
    
    def incrementoipc(self):
        if self.salario>=1160000:
            ipc=self.salario*16.12/100
            incrementosalario=self.salario+ipc
        else:
            ipc=self.salario*13.12/100
            incrementosalario=self.salario+ipc
        return incrementosalario

    def horasextra(self,horas):
        if horas <=60:
            valorhora=(self.salario//30)//8
            incremento=valorhora*horas
            print(incremento)
        else:
            print("la cantidad de horas extras  es superior a la permitida")


            
persona1=empleado("daniel","bodegero",1200000)
print(persona1.salariohoras())        
print(persona1.incrementoipc())
print(persona1.horasextra(30))