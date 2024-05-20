from Orientaciones.Orientacion import Orientacion

class Noroeste(Orientacion):
    __instance = None

    def __init__(self):
        if Noroeste.__instance is None:
            Noroeste.__instance = self
    
    def obtenerInstancia():
        if Noroeste.__instance is None:
            Noroeste.__instance = Noroeste()
        
        return Noroeste.__instance
    
    def obtenerElementoEn(self,cont):
        return cont.norte
    
    def calcularPosicionDesde(self,forma):
        unPunto = (forma.punto[0]-1,forma.punto[1]-1)
        forma.norte.calcularPosicionDesde(forma,unPunto)
    
    def aceptar(self,visitor,forma):
        print("A terra dos galleguinhos.")
        forma.norte.aceptar(visitor)
    
    def ponerElementoEn(self,em,cont):
        cont.norte = em
    
    def moverA(self,ente):
        cont = ente.posicion.forma
        cont.norte.entrar(ente)

    def obtenerComandosDe(self,forma,ente):
        return forma.norte.obtenerComandos(ente)

    def recorrerEn(self,cont,func):
        cont.norte.recorrer(func)
