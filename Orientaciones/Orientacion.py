from abc import ABC, abstractmethod

class Orientacion(ABC):

    @abstractmethod
    def obtenerElementoEn(self,cont):
        pass

    @abstractmethod
    def ponerElementoEn(self,em,cont):
        pass
    
    @abstractmethod
    def aceptar(self,visitor,forma):
        pass
    
    @abstractmethod
    def calcularPosicionDesde(self,forma):
        pass

    @abstractmethod
    def obtenerComandosDe(self,forma,ente):
        pass

    @abstractmethod
    def moverA(ente):
        pass
    
    @abstractmethod
    def recorrerEn(self,cont,func):
        pass