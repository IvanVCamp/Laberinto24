from ElementoMapa.Container.Container import Container

class Armario(Container):
    
    def __init__(self, ref):
        super().__init__(ref)
        self.observaciones = []

    def accept(self, visitante):
        print("Visitando Sodoma (el armario, para quien le cueste pillarlo)")
        visitante.visitArmario(self)
       
        for ch in self.objChildren:
            ch.accept(visitante)

        self.form.accept(visitante)

    def subscribeOpen(self, obs):
        self.observaciones.append(obs)

    def notifySubs(self):
        for obs in self.observaciones.opened:
            obs.muestraArmario(self)

    def abrir(self, x):
        self.op_puertas(x, operacion="abrir")

    def cerrar(self, x):
        self.op_puertas(x, operacion="cerrar")

    def estaAbierto(self):
        return any(door.isOpen() for door in self._obtener_puertas())

    def getCommands(self, ref):
        setCommands = self.commands[:]

        if ref.pos == self:
            for hijo in self.objChildren:
                setCommands.extend(hijo.obtenerComandos(ref))
        setCommands.extend(self.forma.obtenerComandos(ref))

        return setCommands
    
    def entrar(self, ente):
        ente.setPosition(self)

    def esArmario(self):
        return True

    def __str__(self):
        return "Armario " + str(self.num)

    def _obtener_puertas(self):
        return [ori.getElementOn(self.form) for ori in self.form.orientaciones if ori.getElementOn(self.forma).esPuerta()]

    def op_puertas(self, door, operacion):
        for d in self._obtener_puertas():
            if operacion == "abrir":
                d.abrir()
            elif operacion == "cerrar":
                d.cerrar()
