from ElementoMapa.ElementoMapa import ElementoMapa
from Command.Usar import Usar
from abc import ABC,abstractmethod

class Artefacto(ElementoMapa,ABC):
    
    def __init__(self):
        super().__init__()
        self.ref = None
        self.obsPos = []
        
    def entrar(self, obj):
        self.padre.objChildren.remove(self)
        obj.mochila.addObj(self)

        for com in self.commands:
            if com.esCoger:
                self.deleteCommand(com)

        self.agregarComando(Usar())
        for obs in self.observadoresPosicion:
            obs.mostrarObjeto(self)

    def agregarObservadorPosicion(self, observador):
        self.obsPos.append(observador)

    @abstractmethod
    def usar(self, obj):
        pass