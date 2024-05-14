from ElementoMapa.ElementoMapa import ElementoMapa
from Command.Abrir import Abrir
from Command.Entrar import Entrar
from Command.Cerrar import Cerrar
from Estado.EstadoPuerta.Cerrada import Cerrada
from Estado.EstadoPuerta.Abierta import Abierta

class Puerta(ElementoMapa):

    def __init__(self): 
        super().__init__()
        self.estado = Cerrada()
        self.lado1 = None
        self.lado2 = None
        self.visited = False
        self.observers = []

    def entrar(self,ente):
        if self.estaAbierta():
            if ente.pos == self.lado1:
                self.lado2.entrar(ente)
            else:
                self.lado1.entrar(ente)
        else:
            print(str(ente)," se chocó con una puerta.")

    def subsOpened(self,observer):

        self.observers.append(observer)

    def EstimarDistancia(self, obj, coord):
        
        if self.visited:
            return self
        
        self.visited=True
        
        if obj.num == self.lado1.num:
        
            self.lado2.setCoord(coord)
            self.lado2.hacerCalculo()
        
        else:
            self.lado1.setCoord(coord)
            self.lado1.calcularPosicion()

    def aceptar(self,visitor):
        print("Visitando una puerta")
        visitor.visitarPuerta(self)

    def abrir(self):

        self.estado.abrir(self)

    def puedeAbrirse(self):
        self.estado = Abierta()
        self.deleteAbrir()

        com1 = Entrar()
        com2 = Cerrar()
        
        com1.receiver = self
        com2.receiver = self

        self.addCommand(com1)
        self.addCommand(com2)

        self.lado1.notificarSubs()
        self.lado2.notificarSubs()
        self.notificarSubs()

    def notificarSubs(self):
        for obs in self.observers:
            obs.mostrar(self)

    def deleteAbrir(self):
        for com in self.comandos:
            if com.esAbrir():
                self.deleteCommand(com)
                return

    def cerrar(self):
        self.estado = Cerrada()
        self.deleteClose()
        self.deleteEntrar()

        com = Abrir()

        com.receiver = self

        self.addCommand(com)

        self.lado1.notificarSubs()
        self.lado2.notificarSubs()
        self.notificarSubs()

    def deleteClose(self):
        for com in self.commands:
            if com.esCerrar():
                self.deleteCommand(com)
                return
    
    def deleteEntrar(self):
        for com in self.cç:
            if com.esEntrar():
                self.deleteCommand(com)
                return
        
    def esPuerta(self):
        return True
    
    def estaAbierta(self):
        return self.estado.estaAbierta()
