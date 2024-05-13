from Ente.Ente import Ente
from Cuerpo.Cuerpo import Cuerpo

class Personaje(Ente):
    
    def __init__(self):
        super().__init__()
        self.nick=None
        self.bolsa=None
        self.cuerpo = Cuerpo()

    def obtenerComandosCuerpo(self):
        return self.cuerpo.obtenerComandos()
    
    def obtenerEscudo(self):
        return self.cuerpo.obtenerEscudo()
    
    def obtenerEspada(self):
        return self.cuerpo.obtenerArma()
    
    def setEscudo(self,obj):
        self.cuerpo.setEscudo(obj)

    def setEspada(self,obj):
        self.cuerpo.setEspada(obj)

    def setPosicion(self, pos):
        self.posicion= pos
        for obs in self.obsPosition:
            obs.mostrarCuerpo()
    
    def setVidas(self, vida):
        self.vidas = vida
        print("Vidas de ",str(self),":",str(self.vidas))
        for obs in self.obsCorazones:
            obs.mostrarVidasPersonaje()
    
    def enteMuere(self):
        self.juego.personajeMuere()

    def buscarEnemigo(self):
        return self.juego.buscarBicho()
    
    def obtenerComandos(self,ente):
        return self.posicion.obtenerComandos(self)
    
    def esPersonaje(self):
        return True
    
    def __str__(self):
        return "Personaje " + str(self.nick)
    
    def __repr__(self):
        return "Personaje " + str(self.nick)