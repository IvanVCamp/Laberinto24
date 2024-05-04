from Orientaciones.Orientacion import Orientacion

class Oeste(Orientacion):
    __instance = None

    def __init__(self):
        if Oeste.__instance is None:
            Oeste.__instance = self
    
    def obtenerInstancia():
        if Oeste.__instance is None:
            Oeste.__instance = Oeste()
        
        return Oeste.__instance
    
    def obtenerElementoEn(self,cont):
        return cont.Oeste
    
    def calcularPosicionDesde(self,forma):
        unPunto = (forma.punto[0]-1,forma.punto[1])
        forma.Oeste.calcularPosicionDesde(forma,unPunto)
    
    def aceptar(self,visitor,forma):
        print("Has puesto un pie en la Vía de la Plata.")
        forma.Oeste.aceptar(visitor)
    
    def ponerElementoEn(self,em,cont):
        cont.Oeste = em
    
    def moverA(self,ente):
        cont = ente.posicion.forma
        cont.Oeste.entrar(ente)

    def obtenerComandosDe(self,forma,ente):
        return forma.Oeste.obtenerComandos(ente)

    def recorrerEn(self,cont,func):
        cont.Oeste.recorrer(func)
