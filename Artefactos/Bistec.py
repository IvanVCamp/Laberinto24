from Artefactos.Artefacto import Artefacto

class Bistec(Artefacto):
#
    def __init__(self):
        super().__init__()
        self.vida = 10

    def esBistec(self):
        return True
    
    def aceptar(self, vst):
        print("Visitar el bistec :P")
        vst.visitarBistec(self)

    def usar(self, o):
        o.setCorazones(o.corazones + self.vida)
        o.mochila.usado(self)

    def __str__(self):
        return "Bistec nº: " + str(self.ref)
