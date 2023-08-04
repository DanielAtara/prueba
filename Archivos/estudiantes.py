class estudiantes:
    def __init__(self,tp,estrato,cuartosHogar,genero,puntajeMatematicas):
       self.__tp=tp
       self.__estrato=estrato
       self.__cuartosHogar=cuartosHogar
       self.__genero=genero
       self.__puntajeMatematicas=puntajeMatematicas
    def verDatos(self):
        return f"{self.__tp} {self.__estrato} {self.__cuartosHogar} {self.__genero}{self.__puntajeMatematicas}"
       
    def gettp(self):
        return self.__tp
    def getestrato(self):
        return self.__estrato
    def getcuartosHogar(self):
        return self.__cuartosHogar
    def getgenero(self):
        return self.__genero
    def getpuntajeMatematicas(self):
        return self.__puntajeMatematicas