from cliente import*

class natural(cliente):
    def __init__(self,nombre,documento,numeroc):
        self.__nombre=nombre
        self.__documento=documento
        self.__numeroc=numeroc
        
    def getnombre(self):
        return self.__nombre
    def setnombre(self,nombre):
        self.__nombre=nombre
    def getdocumento(self):
        return self.__documento
    def setdocumento(self,documento):
        self.__documento=documento
    def getnumeroc(self):
        return self.__numeroc
    def setnumeroc(self,numeroc):
        self.__numeroc=numeroc

peña=natural("peña",2222222,11111)
print(peña.getnombre())
print(peña.getdocumento())
