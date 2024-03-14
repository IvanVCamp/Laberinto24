import random
import time

class ElementoMapa:
    def __init__(self):
        pass
    

    def ingresar(self, persona):
        pass

    def mostrar(self):
        print("Elemento del Mapa")
    
    def esSala(self):
        return False

class Muro(ElementoMapa):
    def __init__(self):
        super().__init__()

    def mostrar(self):
        print("Muro")

    def ingresar(self, persona):
        print(f"{persona} se ha chocado con un muro")

class ContenedorSala(ElementoMapa):
    def __init__(self):
        super().__init__()
        self.hijos = []
        self.direcciones = []

    def añadirHijo(self, componente):
        self.hijos.append(componente)

    def eliminarHijo(self, componente):
        self.hijos.remove(componente)
    
    def mostrar(self):
        print("Contenedor de Sala")
    
    def caminarAleatorio(self, persona):
        direccion = self.obtenerDireccionAleatoria()
        direccion.caminarAleatorio(persona)

    def añadirDireccion(self, direccion):
        self.direcciones.append(direccion)
    
    def eliminarDireccion(self, direccion):
        self.direcciones.remove(direccion)

    def obtenerDireccionAleatoria(self):
        return random.choice(self.direcciones)

    def irNorte(self, persona):
        self.norte.ingresar(persona)
    
    def irEste(self, persona):
        self.este.ingresar(persona)
    
    def irSur(self, persona):
        self.sur.ingresar(persona)
    
    def irOeste(self, persona):
        self.oeste.ingresar(persona)
    
    def establecerDireccion(self, elemento, direccion):
        direccion.establecerDireccion(elemento, self)

class Laberinto(ContenedorSala):
    def __init__(self):
        super().__init__()

    def añadirSala(self, sala):
        self.añadirHijo(sala)

    def ingresar(self, persona):
        self.hijos[0].ingresar(persona)

    def mostrar(self):
        print("Laberinto")   

    def buscarSala(self, id):
        for sala in self.hijos:
            if sala.id == id:
                return sala
        return None

class Sala(ContenedorSala):
    def __init__(self, id):
        super().__init__()
        self.id = id

    def ingresar(self, persona):
        print(f"{persona} ha ingresado a la sala {self.id}")
    
    def mostrar(self):
        print("Sala")

    def esSala(self):
        return True

class Puerta(ElementoMapa):
    def __init__(self, lado1, lado2):
        super().__init__()
        self.lado1 = lado1
        self.lado2 = lado2
        self.abierta = False

    def ingresar(self, persona):
        if self.abierta:
            self.lado2.ingresar(persona)
        else:
            print("La puerta está cerrada")
    
    def mostrar(self):
        print("Puerta")

# Clases de dirección
class Direccion:
    def __init__(self):
        pass

    def caminarAleatorio(self, persona):
        pass

    def establecerDireccion(self, elemento, contenedor):
        pass

class Norte(Direccion):
    instancia = None

    def __new__(cls):
        if cls.instancia is None:
            cls.instancia = super(Norte, cls).__new__(cls)
        return cls.instancia

    def establecerDireccion(self, elemento, contenedor):
        contenedor.norte = elemento

    def caminarAleatorio(self, persona):
        persona.irNorte()

class Sur(Direccion):
    instancia = None

    def __new__(cls):
        if cls.instancia is None:
            cls.instancia = super(Sur, cls).__new__(cls)
        return cls.instancia

    def establecerDireccion(self, elemento, contenedor):
        contenedor.sur = elemento

    def caminarAleatorio(self, persona):
        persona.irSur()

class Este(Direccion):
    instancia = None

    def __new__(cls):
        if cls.instancia is None:
            cls.instancia = super(Este, cls).__new__(cls)
        return cls.instancia

    def establecerDireccion(self, elemento, contenedor):
        contenedor.este = elemento

    def caminarAleatorio(self, persona):
        persona.irEste()

class Oeste(Direccion):
    instancia = None

    def __new__(cls):
        if cls.instancia is None:
            cls.instancia = super(Oeste, cls).__new__(cls)
        return cls.instancia

    def establecerDireccion(self, elemento, contenedor):
        contenedor.oeste = elemento

    def caminarAleatorio(self, persona):
        persona.irOeste()

class Bicho:
    def __init__(self, estado):
        self.estado = estado
        self.fuerza = 2
        self.salud = 10
        self.ubicacion = None
        self.estado = estado
        self.indice = 0
    
    def __str__(self):
        plantilla = 'Bicho-{0.estado}{0.indice}'
        return plantilla.format(self)
    
    def esHostil(self):
        return self.estado.esHostil()

    def esPerezoso(self):
        return self.estado.esPerezoso()
    
    def ejecutarAccion(self):
        self.estado.ejecutarAccion(self)
    
    def mover(self):
        self.ubicacion.mover(self)
    
    def moverNorte(self):
        self.ubicacion.moverNorte(self)
    def moverEste(self):
        self.ubicacion.moverEste(self)
    def moverSur(self):
        self.ubicacion.moverSur(self)
    def moverOeste(self):
        self.ubicacion.moverOeste(self)
    def comenzar(self):
        self.ejecutarAccion()
    def finalizar(self):
        print(self, " ha finalizado su acción")
        exit(0)


class Estado:
    def __init__(self):
        pass
    def __str__(self):    
        pass
    def esHostil(self):
        return False
    def esPerezoso(self):
        return False
    def ejecutarAccion(self, bicho):
        self.descansar(bicho)
        self.explorar(bicho)
    def explorar(self, bicho):
        bicho.mover()
    def descansar(self, bicho):
        print(bicho," está descansando")
        time.sleep(3)

class Hostil(Estado):
    def __init__(self):
        super().__init__()
    
    def __str__(self):
        return "Hostil"
    
    def esHostil(self):
        return True

    def mostrar(self):
        print("Bicho hostil está listo")

class Perezoso(Estado):
    def __init__(self):
        super().__init__()
    
    def __str__(self):    
        return "Perezoso"
    
    def mostrar(self):
        print("Bicho perezoso en reposo")

    def esPerezoso(self):
        return True

class GestorHilos:
    def __init__(self):
        self.hilos = []

    def agregarHilo(self, hilo):
        self.hilos.append(hilo)

    def iniciarHilos(self):
        for hilo in self.hilos:
            hilo.comenzar()

    def unirHilos(self):
        for hilo in self.hilos:
            hilo.finalizar()

    def detenerHilos(self):
        for hilo in self.hilos:
            if hasattr(hilo, 'finalizar'):
                hilo.finalizar()
            else:
                print("El hilo no tiene un método 'finalizar' definido.")

class Juego:
    def __init__(self):
        self.mundo = None
        self.bichos = []
        self.gestorHilos = GestorHilos()

    def lanzarHilos(self):
        for bicho in self.bichos:
            self.gestorHilos.agregarHilo(bicho)
        self.gestorHilos.iniciarHilos()

    def detenerHilos(self):
        self.gestorHilos.detenerHilos()
        self.gestorHilos.unirHilos()

    def añadirBicho(self, bicho):
        bicho.indice = len(self.bichos) + 1
        self.bichos.append(bicho)        

    def eliminarBicho(self, bicho):
        self.bichos.remove(bicho)
    
    def crearBichoHostil(self, ubicacion):
        bicho = Bicho(Hostil())
        bicho.fuerza = 5
        bicho.ubicacion = ubicacion
        return bicho
    
    def crearBichoPerezoso(self, ubicacion):
        bicho = Bicho(Perezoso())
        bicho.fuerza = 1
        bicho.ubicacion = ubicacion
        return bicho
