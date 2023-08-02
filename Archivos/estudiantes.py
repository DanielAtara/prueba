class estudiantes:
    def __init__(self,tp,estrato,cuartosHogar,genero):
       self.__tp=tp
       self.__estrato=estrato
       self.__cuartosHogar=cuartosHogar
       self.__genero=genero
       
    def gettp(self):
        return self.__tp
    def getestrato(self):
        return self.__estrato
    def getcuartosHogar(self):
        return self.__cuartosHogar
    def getgenero(self):
        return self.__genero