
from Command.Abrir import Abrir
from Command.Cerrar import Cerrar
from ElementoMapa.ElementoMapa import ElementoMapa

class Puerta(ElementoMapa):
    def __init__(self, l1, l2):
        super().__init__()
        self.lado1 = l1
        self.lado2 = l2
        self.opened = False
        self.traspasada= False
        self.addCommand(open(), self)
                
    def __str__(self):
        return "Puerta de hab" + str(self.lado1.num) + " a hab" + str(self.lado2.num) + " acciones: " + str(self.obtenerComandos())

    def entrar(self,alguien):
        if self.abierta:
            if self.lado1 == alguien.posicion:
                self.lado2.entrar(alguien)
                alguien.posicion = self.lado2
            else:
                self.lado1.entrar(alguien)
                alguien.posicion = self.lado1    
            
            if not alguien.esBicho():
                if alguien.compi is not None:
                    alguien.compi.posicion = alguien.posicion    
        else:
            print(str(alguien)+" HA PEGADO UN PORTAZO")
    
    def open(self,ch):
        self.opened = True
        print("Puerta abierta por", ch)

        for c in self.commands:
            if c.esAbrir():
                self.deleteCommand(c)
                self.addCommand(Cerrar(), self)

    def close(self, alguien):
        self.opened = False
        print("¡Portazo de ", alguien,"!")

        for c in self.commands:
            if c.esCerrar():
                self.deleteCommand(c)
                self.addCommand(open(), self)
                
    def esPuerta (self):
        return True
    
