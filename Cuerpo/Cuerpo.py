class Cuerpo():
    def __init__(self):
        self.brazoDefensa = None #Escudos (Defensa)
        self.brazoAtaque = None
        self.bodyObservers = []

    def addBodyObservers(self,obs):
        self.bodyObservers.append(obs)

    def obtenerEscudo(self):
        return self.brazoDefensa
    
    def obtenerArma(self):
        return self.brazoAtaque
    
    def setEscudo(self,obj):
        self.brazoDefensa = obj
        for obs in self.bodyObservers:
            obs.mostrarCuerpo()

    def setEspada(self,obj):
        self.brazoAtaque = obj
        for obs in self.bodyObservers:
            obs.mostrarCuerpo()

    def obtenerComandos(self,ente):
        comandos = []
        if self.brazoDefensa is not None:
            comandos.extend(self.brazoDefensa.obtenerComandos(ente))
        if self.brazoAtaque is not None:
            comandos.extend(self.brazoAtaque.obtenerComandos(ente))
        return comandos
    
    def esCuerpo(self):
        return True