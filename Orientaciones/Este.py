from Orientaciones.Orientacion import Orientacion

class Este(Orientacion):
    __instance = None

    def __init__(self):
        if Este.__instance is None:
            Este.__instance = self
    
    def obtenerInstancia():
        if Este.__instance is None:
            Este.__instance = Este()
        
        return Este.__instance
    
    def obtenerElementoEn(self,cont):
        return cont.norte
    
    def calcularPosicionDesde(self,forma):
        unPunto = (forma.punto[0]+1,forma.punto[1])
        forma.norte.calcularPosicionDesde(forma,unPunto)
    
    def aceptar(self,visitor,forma):
        print("Bienvenido a la Terreta.")
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
