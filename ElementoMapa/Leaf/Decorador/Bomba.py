from ElementoMapa.Leaf.Decorador.Decorador import Decorador
from Command.Entrar import Entrar

class Bomba (Decorador):

    def __init__(self):
        super().__init__()
        self.num = None
        self.activa = True
        self.damage = 20
        self.obsActiva = []
        c = Entrar()
        c.receiver = self
        self.commands.append(c)

    def esBomba(self):
        return True
    
    def agregarObservadoresActiva(self,obs):
        self.obsActiva.append(obs)

    def aceptar(self,visitor):
        print("Visitar bomba")
        visitor.visitarBomba(self)
    
    def entrar(self, e):
        if self.activa:
            print("¡Ahí va, que te ha EXPLOTAO la bombaaaaaa!")
            print("Explo-explota... ¡Explota mi corazón! <3=-1")
            calculo=e.corazones-self.damage
            e.setCorazones(calculo)

            self.activa=False
            
            for co in self.commands:
                if co.esEntrar():
                    self.commands.remove(co)
            for obs in self.obsActiva:
                obs.visualBomba(self)
        else:
            if self.componente is not None:
                self.componente.entrar(e)
    