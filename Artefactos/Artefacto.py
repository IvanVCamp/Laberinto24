from Command.Usar import Usar
from ElementoMapa.ElementoMapa import ElementoMapa
from abc import ABC,abstractmethod

class Artefacto(ElementoMapa, ABC):
    
    def __init__(self):
        super().__init__()
        self.ref = None
        self.obsPos = []
        
    def entrar(self, obj):
        self.padre.objChildren.remove(self)
        obj.mochila.addArtefacto(self)

        for com in self.commands:
            if com.esCoger:
                self.deleteCommand(com)

        self.addCommand(Usar())
        for obs in self.obsPos:
            obs.visualObjeto(self)

    def agregarObservadorPosicion(self, observador):
        self.obsPos.append(observador)

    @abstractmethod
    def usar(self, obj):
        pass