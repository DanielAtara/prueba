
class personas:
    def __init__(self,nombre,documento):
        self.__nombre=nombre
        self.__documento=documento
        self.__cursos=[]
    
    def getnombre(self):
        return self.__nombre
    def setnombre (self,nombre):
        self.__nombre=nombre
    def getdocumento(self):
        return self.__documento
    def setdocumento (self,documento):
        self.__documento=documento
    def getdatos (self):
        return f"{self.__nombre},{self.__documento}"
    
    def agregarcursos(self,curso):
        self.__cursos.append(curso)
    def getcursos(self):
        return self.__cursos
    def deletecursos(self,curso):
        self.__cursos.remove(curso)
    def buscarcursos(self,curso):
        if curso in self.__cursos:
            return f"el curso {curso} esta en a lista de cursos"  
        
    
a=personas("aura",102552)
b=personas("daniel",2515)
print(a.getnombre())
print(a.getdocumento())
a.agregarcursos("matematicas")
a.agregarcursos("ingles")
a.agregarcursos("filosofia")
a.deletecursos("matematicas")
print (a.buscarcursos("ingles"))
print (a.buscarcursos("filosofia"))
print(a.getcursos())   

     
        