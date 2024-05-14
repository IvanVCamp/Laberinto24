from ElementoMapa.Pared import Pared

class ParedBomba(Pared):

    def __init__(self):
        super().__init__()
        self.activa = True

    def entrar(self,ente):
        if self.activa:
            print("¡BOOOOOOM! La bomba te ha explotado...")
            self.activa = False
        else:
            print("¡Que te chocas, muchacho!")