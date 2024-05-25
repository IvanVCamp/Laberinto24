from Artefactos.Artefacto import Artefacto
from Command.Usar import Usar
from Command.Soltar import Soltar


class Katana(Artefacto):

    def __init__(self):
        super().__init__()
        self.poder = 10

    def esKatana(self):
        return True

    def aceptar(self, vst):
        print("Visitar katana")
        vst.visitarKatana(self)
    
    def usar(self, o):
        o.setKatana(self)
        o.mochila.usado(self)

        for c in self.comandos:
            if c.esSoltar():
                self.deleteCommand(c)
        for c in self.comandos:
            if c.esUsar():
                self.deleteCommand(c)
    
    def desequipar(self,ente):
        ente.setKatana(None)
        ente.mochila.addArtefacto(self)
        
        firstAction = Usar()
        firstAction.receiver= self

        secondAction = Soltar()
        secondAction.receiver = self

        self.addCommand(firstAction)
        self.addCommand(secondAction)

    def __str__(self):
        return "Katana REF nº: " +str(self.num)