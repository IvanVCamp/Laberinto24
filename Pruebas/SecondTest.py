
import unittest
import sys
from io import StringIO
from Builder.Builder import Director
from Ente.Character import Character

class TestLab4Hab4BichosTunel(unittest.TestCase):

    def setUp(self):
        super().setUp()
        sys.stdout_save =sys.stdout
        sys.stdout = StringIO()#Deshabilitamos la salida para facilitar la lectura de los test
        director = Director()
        director.procesar('json/lab4hab4bichos-rombo.json')
        self.juego = director.obtenerJuego()
        personaje = Character()
        personaje.nick = "Prueba"
        self.juego.agregarPersonaje(personaje)
        sys.stdout=sys.stdout_save#Volvemos a habilitarla

    def testIniciales(self):
        self.assertEqual(self.juego is not None, True)
        self.assertEqual(self.juego.esJuego(),True)
        self.assertEqual(len(self.juego.laberinto.hijos),4)
        print("TEST INICIAL SUPERADO.\n")
    
    def testHabitaciones(self):
        #Habitación 1
        hab1 = self.juego.laberinto.hijos[0]
        self.assertEqual(hab1.esHabitacion(),True)
        self.assertEqual(hab1.num,1)
        self.assertEqual(len(hab1.hijos),1)
        self.assertEqual(hab1.forma.esRombo(),True)
        self.assertEqual(hab1.forma.noreste.esPuerta(),True)
        self.assertEqual(hab1.forma.noroeste.esPared(),True)
        self.assertEqual(hab1.forma.sureste.esPuerta(),True)
        self.assertEqual(hab1.forma.suroeste.esPared(),True)
        #Habitación 2
        hab2 = self.juego.laberinto.hijos[1]
        self.assertEqual(hab2.esHabitacion(),True)
        self.assertEqual(hab2.num,2)
        self.assertEqual(len(hab2.hijos),1)
        self.assertEqual(hab2.forma.esRombo(),True)
        self.assertEqual(hab2.forma.noreste.esPuerta(),True)
        self.assertEqual(hab2.forma.noroeste.esPuerta(),True)
        self.assertEqual(hab2.forma.sureste.esPared(),True)
        self.assertEqual(hab2.forma.suroeste.esPared(),True)
        #Habitación 3
        hab3 = self.juego.laberinto.hijos[2]
        self.assertEqual(hab3.esHabitacion(),True)
        self.assertEqual(hab3.num,3)
        self.assertEqual(len(hab3.hijos),1)
        self.assertEqual(hab3.forma.esRombo(),True)
        self.assertEqual(hab3.forma.noreste.esPared(),True)
        self.assertEqual(hab3.forma.noroeste.esPared(),True)
        self.assertEqual(hab3.forma.sureste.esPuerta(),True)
        self.assertEqual(hab3.forma.suroeste.esPuerta(),True)
        #Habitación 4
        hab4 = self.juego.laberinto.hijos[3]
        self.assertEqual(hab4.esHabitacion(),True)
        self.assertEqual(hab4.num,4)
        self.assertEqual(len(hab4.hijos),0)
        self.assertEqual(hab4.forma.esRombo(),True)
        self.assertEqual(hab4.forma.noreste.esPared(),True)
        self.assertEqual(hab4.forma.noroeste.esPuerta(),True)
        self.assertEqual(hab4.forma.sureste.esPared(),True)
        self.assertEqual(hab4.forma.suroeste.esPuerta(),True)

        print("ESTRUCTURA DE LAS HABITACIONES COMPROBADAS.\n")


    def testBichos(self):
        bichos = self.juego.bichos
        #Bicho 1
        b1 = bichos[0]
        self.assertEqual(b1.num,1)
        self.assertEqual(b1.modo.esAgresivo(),True)
        self.assertEqual(b1.posicion,self.juego.laberinto.hijos[0])
        self.assertEqual(b1.juego,self.juego)
        self.assertEqual(b1.estado.estaVivo(),True)
        #Bicho 2
        b2 = bichos[1]
        self.assertEqual(b2.num,2)
        self.assertEqual(b2.modo.esPerezoso(),True)
        self.assertEqual(b2.posicion,self.juego.laberinto.hijos[3])
        self.assertEqual(b2.juego,self.juego)
        self.assertEqual(b2.estado.estaVivo(),True)
        
        print("TEST DE LOS BICHOS SUPERADO.\n")

    def testPersonaje(self):
        personaje = self.juego.personaje
        self.assertEqual(personaje.nick,"Prueba")
        self.assertEqual(personaje.posicion,self.juego.obtenerHabitacion(1))
        self.assertEqual(personaje.estado.estaVivo(),True)
        self.assertEqual(personaje.juego, self.juego)
        self.assertEqual(personaje.bolsa.esBolsa(),True)
        self.assertEqual(len(personaje.bolsa.hijos),0)
        self.assertEqual(personaje.cuerpo.esCuerpo(),True)
        self.assertEqual(personaje.cuerpo.mDerecha is None, True)
        self.assertEqual(personaje.cuerpo.mIzquierda is None, True)
        print("TEST DEL PERSONAJE SUPERADO.\n")

    def testPuertas(self):
        #Puerta 1
        p1 = self.juego.obtenerHabitacion(1).forma.sureste
        self.assertEqual(p1.esPuerta(),True)
        self.assertEqual(p1.lado1,self.juego.obtenerHabitacion(1))
        self.assertEqual(p1.lado2,self.juego.obtenerHabitacion(2))
        self.assertEqual(p1.comandos[0].esAbrir(),True)
        self.assertEqual(p1.comandos[0].receptor,p1)
        #Puerta 2
        p2 = self.juego.obtenerHabitacion(2).forma.noreste
        self.assertEqual(p2.esPuerta(),True)
        self.assertEqual(p2.lado1,self.juego.obtenerHabitacion(2))
        self.assertEqual(p2.lado2,self.juego.obtenerHabitacion(4))
        self.assertEqual(p2.comandos[0].esAbrir(),True)
        self.assertEqual(p2.comandos[0].receptor,p2)
        #Puerta 3
        p3 = self.juego.obtenerHabitacion(4).forma.noroeste
        self.assertEqual(p3.esPuerta(),True)
        self.assertEqual(p3.lado1,self.juego.obtenerHabitacion(4))
        self.assertEqual(p3.lado2,self.juego.obtenerHabitacion(3))
        self.assertEqual(p3.comandos[0].esAbrir(),True)
        self.assertEqual(p3.comandos[0].receptor,p3)
        #Puerta 4
        p4 = self.juego.obtenerHabitacion(3).forma.suroeste
        self.assertEqual(p4.esPuerta(),True)
        self.assertEqual(p4.lado1,self.juego.obtenerHabitacion(3))
        self.assertEqual(p4.lado2,self.juego.obtenerHabitacion(1))
        self.assertEqual(p4.comandos[0].esAbrir(),True)
        self.assertEqual(p4.comandos[0].receptor,p4)
        print("TEST DE PUERTAS SUPERADO.\n")

    def testArmarios(self):
        #Armario 1
        arm1 = None
        pad1 = None
        for hijo in (pad1:=self.juego.obtenerHabitacion(1)).hijos:
            if hijo.esArmario():
                arm1 = hijo
        self.assertEqual(arm1.num,1)
        self.assertEqual(arm1.padre,pad1)
        self.assertEqual(len(arm1.hijos),3)
        self.assertEqual(arm1.forma.esRombo(),True)
        self.assertEqual(arm1.forma.noroeste.esPared(),True)
        self.assertEqual(arm1.forma.noreste.esPared(),True)
        self.assertEqual(arm1.forma.sureste.esPared(),True)
        self.assertEqual((p1:=arm1.forma.suroeste).esPuerta(),True)
        self.assertEqual(p1.estaAbierta(),False)
        self.assertEqual(p1.comandos[0].esAbrir(),True)
        self.assertEqual(p1.comandos[0].receptor,p1)

        print("TEST DE ARMARIOS SUPERADO.")

    def testTuneles(self):
        pass#No tiene túneles
    
    def testbombas(self):
        #Bomba 1
        bomba1 = None
        pad1 = None
        for hijo in (pad1:=self.juego.obtenerHabitacion(3)).hijos:
            if hijo.esBomba():
                bomba1 = hijo
        self.assertEqual(bomba1.num,1)
        self.assertEqual(bomba1.activa,True)
        self.assertEqual(bomba1.padre,pad1)
        self.assertEqual(bomba1.comandos[0].esEntrar(),True)
        self.assertEqual(bomba1.comandos[0].receptor,bomba1)

    def testObjetos(self):
        #Objetos Habitación 1
        hab1 = self.juego.obtenerHabitacion(1)
        #Banana 1
        arm1 = hab1.hijos[0]
        self.assertEqual((banana1:=arm1.hijos[0]).esBanana(),True)
        self.assertEqual((com1:=banana1.comandos[0]).esCoger(),True)
        self.assertEqual(com1.receptor,banana1)
        #Banana 2
        self.assertEqual((banana2:=arm1.hijos[0]).esBanana(),True)
        self.assertEqual((com1:=banana2.comandos[0]).esCoger(),True)
        self.assertEqual(com1.receptor,banana2)
        #Objetos Habitación 2
        hab2 = self.juego.obtenerHabitacion(2)
        #Espada metal
        self.assertEqual((katana:=hab2.hijos[0]).esEspada(),True)
        self.assertEqual(katana.num,1)
        self.assertEqual(katana.comandos[0].esCoger(),True)
        self.assertEqual(katana.comandos[0].receptor,katana)
        self.assertEqual(katana.material.esMetal(),True)
        print("TEST DE OBJETOS SUPERADO.\n")
        
unittest.main()
