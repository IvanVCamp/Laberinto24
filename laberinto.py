class Juego:
    def __init__(self):
        self.laberinto = None

    def CrearPared(self):
        return Pared()
    
    def CrearPuerta(self, lado1, lado2):
        puerta = Puerta(lado1, lado2)
        return puerta  
    
    def CrearHabitacion(self, id):
        habitacion = Habitacion(id)
        habitacion.norte = self.CrearPared()
        habitacion.este = self.CrearPared()
        habitacion.sur = self.CrearPared()
        habitacion.oeste = self.CrearPared()
        return habitacion

    def CrearLaberinto(self):
        return Laberinto()
    
    def make2RoomsLaberintoFM(self):

        self.laberinto = self.CrearLaberinto()
        habitacion1 = self.CrearHabitacion(1)
        habitacion2 = self.CrearHabitacion(2)
        
        puerta = self.CrearPuerta(habitacion1, habitacion2)
        
        habitacion1.sur = puerta
        habitacion2.norte = puerta
        
        self.laberinto.AñadeHab(habitacion1)
        self.laberinto.AñadeHab(habitacion2)
        
        return self.laberinto
    
    def make2RoomsLaberinto(self):
        
        self.laberinto = Laberinto()
        
        habitacion1 = Habitacion(1)
        habitacion2 = Habitacion(2)
        
        self.laberinto.AñadeHab(habitacion1)
        self.laberinto.AñadeHab(habitacion2)

        puerta = Puerta(habitacion1, habitacion2)
        
        habitacion1.sur = puerta
        habitacion2.norte = puerta
        return self.laberinto

class JuegoBomba(Juego):
    def CrearPared(self):
        return ParedBomba()

class ElementoMapa:
    def __init__(self):
        pass
    def entrar(self):
        pass

class Contenedor(ElementoMapa):
    
    def __init__(self):
        self.hijos = []
        
    def agregarHijo(self, hijo):
        self.hijos.append(hijo)
        
    def eliminarHijo(self, hijo):
        self.hijos.remove(hijo)

class Hoja(ElementoMapa):
    def accept(self, visitor):
        visitor.visitHoja(self)

class Decorator(Hoja):
    def __init__(self, componente):
        self.componente = componente

class Laberinto(Contenedor):
    def __init__(self):
        self.habitaciones = []
    
    def AñadeHab(self, habitacion):
        self.habitaciones.append(habitacion)
    
    def entrar(self):
        self.habitaciones[0].entrar()  

class Habitacion(Contenedor):
    def __init__(self, id):
        self.norte = None
        self.este = None
        self.oeste = None
        self.sur = None
    
        self.id = id
    
    def entrar(self):
        print("Has accedido a la habitación ", self.id)

class Puerta(ElementoMapa):
    def __init__(self, lado1, lado2):
        self.lado1 = lado1
        self.lado2 = lado2
        self.abierta = False
    def entrar(self):
        if self.abierta:
            self.lado2.entrar()
        else:
            print("La puerta está bloqueada.")
    
class Pared(ElementoMapa):
    def __init__(self):
        pass # Paredes don't need additional attributes
    def entrar(self):
        print("Hay una pared en medio.")

class ParedBomba(Pared):
    def __init__(self):
        self.activo = False   
    def entrar(self):
        if self.activo:
            print("BOOOM! La bomba explotó!")
        else:
            return super().entrar()

juego = Juego()
juego.make2RoomsLaberinto()
juego.laberinto.entrar()

juego = Juego()
juego.make2RoomsLaberintoFM()

juego = JuegoBomba()
juego.make2RoomsLaberintoFM()
juego.laberinto.entrar()
