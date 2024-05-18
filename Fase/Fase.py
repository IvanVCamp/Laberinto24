from abc import ABC, abstractmethod
class Fase(ABC):
    
    @abstractmethod
    def addCharacter(self, ch, game):
        pass
    
    @abstractmethod
    def lanzarLosBichos(self, game):
        pass

    def esComienzo(self):
        return False
    
    def esJugando(self):
        return False
    
    def esFinal(self):
        return False