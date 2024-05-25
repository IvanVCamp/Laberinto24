from ElementoMapa.Container.Container import Container
class Laberinto(Container):

    def __init__(self):
        super().__init__(0)

    def agregarHabitacion(self, hab):
        self.objChildren.append(hab)

    def entrar(self, ref):
        h = self.getHab(1)
        h.entrar(ref)

    def getHab(self, index):
        return self.objChildren[index - 1]
    
    def recorrer(self, x):
        for ch in self.objChildren:
            ch.recorrer()

    def accept(self, visitante):
        print("Recorrer laberinto.")
        for ch in self.objChildren:
            ch.aceptar(visitante)

    
    def __str__(self):
        detalle = "Estado del laberinto:\n _________________________ \n"

        hijos = self.objChildren
        
        for h in hijos:
            detalle = detalle + str(h) + "\n ***************"
    
        return detalle

