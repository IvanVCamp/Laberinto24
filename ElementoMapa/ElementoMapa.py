from abc import ABC, abstractmethod

class ElementoMapa(ABC):
    
    def __init__(self):
        self.padre = None
        self.commands = []

    @abstractmethod 
    def entrar(self,ente):
        pass
    
    @abstractmethod
    def aceptar(self,visitor):
        pass

    def addCommand(self,comando):
        for c in self.commands:
            if c.equals(comando):
                return
        comando.receptor = self
        self.commands.append(comando)

    def obtenerComandos(self,ente):
        return self.commands
    
    def deleteCommand(self,comando):
        self.commands.remove(comando)

    def recorrer(self, fn):
        fn(self)

    def esHabitacion(self):
        return False
    
    def esBomba(self):
        return False
    
    def esPared(self):
        return False
    
    def esPuerta(self):
        return False

    
    def esEspada(self):
        return False
    

    def esArmario(self):
        return False
    
    def esTunel(self):
        return False
    
    def esBolsa(self):
        return False
    
    def esBanana(self):
        return False
    
    def esEscudo(self):
        return False