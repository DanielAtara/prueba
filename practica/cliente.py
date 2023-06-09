from producto import* 
class cliente:
    def __init__(self,tipousuario,nombreproducto,tipoproducto):
        self.__tipousuario =tipousuario
        self.__nombreproducto =nombreproducto
        self.__tipoproducto =tipoproducto
        self.__producto=[]
        
    def agregarproducto(self,producto):
        self.__producto.append(producto)
    
    def componerproducto(self,nombre,tipoproducto):
        producto2=producto(nombre,tipoproducto)
        self.__producto.append(producto2)  
    
   