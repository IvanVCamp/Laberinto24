from Orientaciones.Orientacion import Orientacion

class Sur(Orientacion):
    __instance = None

    def __init__(self):
        if Sur.__instance is None:
            Sur.__instance = self
    
    def obtenerInstancia():
        if Sur.__instance is None:
            Sur.__instance = Sur()
        
        return Sur.__instance
    
    def getElement(self,cont):
        return cont.Sur
    
    def calcularPosicionDesde(self,forma):
        unPunto = (forma.punto[0],forma.punto[1]+1)
        forma.Sur.calcularPosicionDesde(forma,unPunto)
    
    def aceptar(self,visitor,forma):
        print("Has puesto un pie en el territorio Tartessos.")
        forma.Sur.aceptar(visitor)
    
    def putElementOn(self,em,cont):
        cont.Sur = em
    
    def moverA(self,ente):
        cont = ente.posicion.forma
        cont.Sur.entrar(ente)

    def getCommands(self,forma,ente):
        return forma.Sur.getCommands(ente)

    def recorrerEn(self,cont,func):
        cont.Sur.recorrer(func)
