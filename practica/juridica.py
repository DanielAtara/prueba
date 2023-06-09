from cliente import*

class juridica(cliente):
    def __init__(self,nombre,nit,numeroc):
        self.__nombre=nombre
        self.__nit=nit
        self.__numeroc=numeroc
    def getnombre(self):
        return self.__nombre
    def setnombre(self,nombre):
        self.__nombre=nombre
    def getnit(self):
        return self.__nit
    def setnit(self,nit):
        self.__nit =nit
    def getnumeroc(self):
        return self.__numeroc
    def setnumeroc(self,numeroc):
        self.__numeroc =numeroc
    
    
    
   
alpina=juridica("alpina",269630,33333333)
print(alpina.getnombre)

