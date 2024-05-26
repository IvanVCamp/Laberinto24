from Orientaciones.Oeste import Oeste
from Orientaciones.Norte import Norte
from Orientaciones.Este import Este
from Orientaciones.Sur import Sur
from Orientaciones.Noreste import Noreste
from Orientaciones.Noroeste import Noroeste
from Orientaciones.Sureste import Sureste
from Orientaciones.Suroeste import Suroeste
from Estado.Vivo import Vivo

from abc import ABC,abstractmethod
class Ente(ABC):

    def __init__(self):
        self.corazones = 50
        self.poder = 25
        self.estado = Vivo()
        self.posicion= None
        self.juego = None
        self.obsPosition = []
        self.obsCorazones = []


    def subscribePosicion(self,obs):
        self.obsPosition.append(obs)

    def subscribeVida(self,obs):
        self.obsCorazones.append(obs)

    def setPosicion(self,pos):
        self.posicion = pos
    
    def setCorazones(self,corazones):
        self.corazones = corazones
        print(str(self), " coraçaos: ",str(self.corazones))

    def atacar(self):
        unEnte = self.buscarEnemigo()
        if unEnte is not None:
            unEnte.esAtacadoPor(self)
    
    def esAtacadoPor(self,unEnte):
        self.estado.esAtacadoPor(self,unEnte)

    def puedeSerAtacadoPor(self,unEnte):
        self.recalcularVidas(unEnte)
        if self.verificarEstado():
            self.Fenece()

    def recalcularVidas(self, ente):
        poder_de_ataque = ente.poder

        if ente.esPersonaje():
            arma = ente.obtenerArma()
            poder_de_ataque += arma.poder

        vidas_resultantes = self.corazones - poder_de_ataque
        vidas_resultantes = max(0, min(self.corazones, vidas_resultantes))
        self.setCorazones(vidas_resultantes)
    
    def verificarEstado(self):
        if self.corazones == 0:
            return True
        else:
            return False
        
    @abstractmethod
    def buscarEnemigo(self):
        pass

    def estaVivo(self):
        return self.estado.estaVivo()
    
    def irA(self,unaOr):
        unaOr.ir(self)

    def irAlNorte(self):
        self.irA(Norte.obtenerInstancia())

    def irAlEste(self):
        self.irA(Este.obtenerInstancia())

    def irAlOeste(self):
        self.irA(Oeste.obtenerInstancia())

    def irAlSur(self):
        self.irA(Sur.obtenerInstancia())

    def irAlNoreste(self):
        self.irA(Noreste.obtenerInstancia())

    def irAlNoroeste(self):
        self.irA(Noroeste.obtenerInstancia())

    def irAlSureste(self):
        self.irA(Sureste.obtenerInstancia())

    def irAlSuroeste(self):
        self.irA(Suroeste.obtenerInstancia())

    def esPersonaje(self):
        return False
    
    def esBicho(self):
        return False
    
    @abstractmethod
    def fenece():
        pass