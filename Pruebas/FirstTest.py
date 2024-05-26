import unittest
import sys
from io import StringIO
from Builder.Builder import Director
from Ente.Character import Character

class TestLab4Hab4BichosTunel(unittest.TestCase):

    def setUp(self):
        super().setUp()
        sys.stdout_save =sys.stdout
        sys.stdout = StringIO()
        director = Director()
        director.procesar('maze4hab.json')
        self.juego = director.obtenerJuego()
        personaje = Character()
        personaje.nick = "Personaje 1"
        self.juego.addCharacter(personaje)
        sys.stdout=sys.stdout_save

    def testIniciales(self):
        self.assertEqual(self.juego is not None, True)
        self.assertEqual(self.juego.esJuego(),True)
        self.assertEqual(len(self.juego.laberinto.objChildren),4)
        print("TEST INICIAL SUPERADO.\n")
    
    def testHabitaciones(self):
        #Habitación 1
        hab1 = self.juego.laberinto.hijos[0]
        self.assertEqual(hab1.esHabitacion(),True)
        self.assertEqual(hab1.num,1)
        self.assertEqual(len(hab1.hijos),3)
        self.assertEqual(hab1.forma.esCuadrado(),True)
        self.assertEqual(hab1.forma.norte.esPared(),True)
        self.assertEqual(hab1.forma.este.esPuerta(),True)
        self.assertEqual(hab1.forma.oeste.esPared(),True)
        self.assertEqual(hab1.forma.sur.esPuerta(),True)
        #Habitación 2
        hab2 = self.juego.laberinto.hijos[1]
        self.assertEqual(hab2.esHabitacion(),True)
        self.assertEqual(hab2.num,2)
        self.assertEqual(len(hab2.hijos),1)
        self.assertEqual(hab2.forma.esCuadrado(),True)
        self.assertEqual(hab2.forma.norte.esPuerta(),True)
        self.assertEqual(hab2.forma.este.esPuerta(),True)
        self.assertEqual(hab2.forma.oeste.esPared(),True)
        self.assertEqual(hab2.forma.sur.esPared(),True)
        #Habitación 3
        hab3 = self.juego.laberinto.hijos[2]
        self.assertEqual(hab3.esHabitacion(),True)
        self.assertEqual(hab3.num,3)
        self.assertEqual(len(hab3.hijos),2)
        self.assertEqual(hab3.forma.esCuadrado(),True)
        self.assertEqual(hab3.forma.norte.esPared(),True)
        self.assertEqual(hab3.forma.este.esPared(),True)
        self.assertEqual(hab3.forma.oeste.esPuerta(),True)
        self.assertEqual(hab3.forma.sur.esPuerta(),True)
        #Habitación 4
        hab4 = self.juego.laberinto.hijos[3]
        self.assertEqual(hab4.esHabitacion(),True)
        self.assertEqual(hab4.num,4)
        self.assertEqual(len(hab4.hijos),2)
        self.assertEqual(hab4.forma.esCuadrado(),True)
        self.assertEqual(hab4.forma.norte.esPuerta(),True)
        self.assertEqual(hab4.forma.este.esPared(),True)
        self.assertEqual(hab4.forma.oeste.esPuerta(),True)
        self.assertEqual(hab4.forma.sur.esPared(),True)

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
        self.assertEqual(b2.posicion,self.juego.laberinto.hijos[1])
        self.assertEqual(b2.juego,self.juego)
        self.assertEqual(b2.estado.estaVivo(),True)
        #Bicho 3
        b3 = bichos[2]
        self.assertEqual(b3.num,3)
        self.assertEqual(b3.modo.esAgresivo(),True)
        self.assertEqual(b3.posicion,self.juego.laberinto.hijos[2])
        self.assertEqual(b3.juego,self.juego)
        self.assertEqual(b3.estado.estaVivo(),True)
        #Bicho 4
        b4 = bichos[3]
        self.assertEqual(b4.num,4)
        self.assertEqual(b4.modo.esPerezoso(),True)
        self.assertEqual(b4.posicion,self.juego.laberinto.hijos[3])
        self.assertEqual(b4.juego,self.juego)
        self.assertEqual(b4.estado.estaVivo(),True)
        
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
        p1 = self.juego.obtenerHabitacion(1).forma.sur
        self.assertEqual(p1.esPuerta(),True)
        self.assertEqual(p1.lado1,self.juego.obtenerHabitacion(1))
        self.assertEqual(p1.lado2,self.juego.obtenerHabitacion(2))
        self.assertEqual(p1.comandos[0].esAbrir(),True)
        self.assertEqual(p1.comandos[0].receptor,p1)
        self.assertEqual(p1.estaAbierta(),False)
        #Puerta 2
        p2 = self.juego.obtenerHabitacion(2).forma.este
        self.assertEqual(p2.esPuerta(),True)
        self.assertEqual(p2.lado1,self.juego.obtenerHabitacion(2))
        self.assertEqual(p2.lado2,self.juego.obtenerHabitacion(4))
        self.assertEqual(p2.comandos[0].esAbrir(),True)
        self.assertEqual(p2.comandos[0].receptor,p2)
        self.assertEqual(p2.estaAbierta(),False)
        #Puerta 3
        p3 = self.juego.obtenerHabitacion(4).forma.norte
        self.assertEqual(p3.esPuerta(),True)
        self.assertEqual(p3.lado1,self.juego.obtenerHabitacion(4))
        self.assertEqual(p3.lado2,self.juego.obtenerHabitacion(3))
        self.assertEqual(p3.comandos[0].esAbrir(),True)
        self.assertEqual(p3.comandos[0].receptor,p3)
        self.assertEqual(p3.estaAbierta(),False)
        #Puerta 4
        p4 = self.juego.obtenerHabitacion(3).forma.oeste
        self.assertEqual(p4.esPuerta(),True)
        self.assertEqual(p4.lado1,self.juego.obtenerHabitacion(3))
        self.assertEqual(p4.lado2,self.juego.obtenerHabitacion(1))
        self.assertEqual(p4.comandos[0].esAbrir(),True)
        self.assertEqual(p4.comandos[0].receptor,p4)
        self.assertEqual(p4.estaAbierta(),False)
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
        self.assertEqual(len(arm1.hijos),1)
        self.assertEqual(arm1.forma.esCuadrado(),True)
        self.assertEqual(arm1.forma.norte.esPared(),True)
        self.assertEqual(arm1.forma.este.esPared(),True)
        self.assertEqual(arm1.forma.oeste.esPared(),True)
        self.assertEqual((p1:=arm1.forma.sur).esPuerta(),True)
        self.assertEqual(p1.estaAbierta(),False)
        self.assertEqual(p1.comandos[0].esAbrir(),True)
        self.assertEqual(p1.comandos[0].receptor,p1)
        #Armario 2
        arm2 = None
        pad2 = None
        for hijo in (pad2:=self.juego.obtenerHabitacion(4)).hijos:
            if hijo.esArmario():
                arm2 = hijo
        self.assertEqual(arm2.num,2)
        self.assertEqual(arm2.padre,pad2)
        self.assertEqual(len(arm2.hijos),0)
        self.assertEqual(arm2.forma.esCuadrado(),True)
        self.assertEqual(arm2.forma.norte.esPared(),True)
        self.assertEqual(arm2.forma.este.esPared(),True)
        self.assertEqual(arm2.forma.oeste.esPared(),True)
        self.assertEqual((p2:=arm1.forma.sur).esPuerta(),True)
        self.assertEqual(p2.estaAbierta(),False)
        self.assertEqual(p2.comandos[0].esAbrir(),True)
        self.assertEqual(p2.comandos[0].receptor,p2)

        print("TEST DE ARMARIOS SUPERADO.")

    def testTuneles(self):
        tunel = None
        padre = None
        for hijo in (padre:=self.juego.obtenerHabitacion(3)).hijos:
            if hijo.esTunel():
                tunel = hijo
        self.assertEqual(tunel.padre,padre)
        self.assertEqual(tunel.laberinto,None)
        print("TEST DE TÚNELES SUPERADO.\n")
    
    def testbombas(self):
        #Bomba 1
        bomba1 = None
        pad1 = None
        for hijo in (pad1:=self.juego.obtenerHabitacion(1)).hijos:
            if hijo.esBomba():
                bomba1 = hijo
        self.assertEqual(bomba1.num,1)
        self.assertEqual(bomba1.activa,True)
        self.assertEqual(bomba1.padre,pad1)
        self.assertEqual(bomba1.comandos[0].esEntrar(),True)
        self.assertEqual(bomba1.comandos[0].receptor,bomba1)
        #Bomba 2
        bomba2 = None
        pad2 = None
        for hijo in (pad2:=self.juego.obtenerHabitacion(4)).hijos:
            if hijo.esBomba():
                bomba2 = hijo
        self.assertEqual(bomba2.num,2)
        self.assertEqual(bomba2.activa,True)
        self.assertEqual(bomba2.padre,pad2)
        self.assertEqual(bomba2.comandos[0].esEntrar(),True)
        self.assertEqual(bomba2.comandos[0].receptor,bomba2)
        print("TEST DE BOMBAS SUPERADO.")

    def testObjetos(self):
        #Objetos Habitación 1
        hab1 = self.juego.obtenerHabitacion(1)
        #Banana 1
        arm1 = hab1.hijos[0]
        self.assertEqual((banana1:=arm1.hijos[0]).esBanana(),True)
        self.assertEqual((com1:=banana1.comandos[0]).esCoger(),True)
        self.assertEqual(com1.receptor,banana1)
        #Escudo
        self.assertEqual((escudo:=hab1.hijos[1]).esEscudo(),True)
        self.assertEqual(escudo.num,1)
        self.assertEqual(escudo.comandos[0].esCoger(),True)
        self.assertEqual(escudo.comandos[0].receptor,escudo)
        #Objetos Habitación 2
        hab2 = self.juego.obtenerHabitacion(2)
        #Espada metal
        self.assertEqual((espada1:=hab2.hijos[0]).esEspada(),True)
        self.assertEqual(espada1.num,1)
        self.assertEqual(espada1.comandos[0].esCoger(),True)
        self.assertEqual(espada1.comandos[0].receptor,espada1)
        self.assertEqual(espada1.material.esMetal(),True)
        #Objetos Habitación 3
        hab3 = self.juego.obtenerHabitacion(3)
        #Espada metal
        self.assertEqual((espada2:=hab3.hijos[0]).esEspada(),True)
        self.assertEqual(espada2.num,1)
        self.assertEqual(espada2.comandos[0].esCoger(),True)
        self.assertEqual(espada2.comandos[0].receptor,espada2)
        self.assertEqual(espada2.material.esDiamante(),True)
        print("TEST DE OBJETOS SUPERADO.\n")

    def testFuncionalidades(self):
        #Abrir puertas
        self.juego.abrirPuertas()
        p1 = self.juego.obtenerHabitacion(1).forma.sur
        p2 = self.juego.obtenerHabitacion(2).forma.este
        p3 = self.juego.obtenerHabitacion(4).forma.norte
        p4 = self.juego.obtenerHabitacion(3).forma.oeste
        self.assertEqual(len(p1.comandos),2)
        self.assertEqual(p1.esPuerta(),True)
        self.assertEqual(p1.comandos[0].esEntrar(),True)
        self.assertEqual(p1.comandos[0].receptor,p1)
        self.assertEqual(p1.comandos[1].esCerrar(),True)
        self.assertEqual(p1.comandos[1].receptor,p1)
        self.assertEqual(len(p2.comandos),2)
        self.assertEqual(p2.esPuerta(),True)
        self.assertEqual(p2.comandos[0].esEntrar(),True)
        self.assertEqual(p2.comandos[0].receptor,p2)
        self.assertEqual(p2.comandos[1].esCerrar(),True)
        self.assertEqual(p2.comandos[1].receptor,p2)
        self.assertEqual(len(p3.comandos),2)
        self.assertEqual(p3.esPuerta(),True)
        self.assertEqual(p3.comandos[0].esEntrar(),True)
        self.assertEqual(p3.comandos[0].receptor,p3)
        self.assertEqual(p3.comandos[1].esCerrar(),True)
        self.assertEqual(p3.comandos[1].receptor,p3)
        self.assertEqual(len(p4.comandos),2)
        self.assertEqual(p4.esPuerta(),True)
        self.assertEqual(p4.comandos[0].esEntrar(),True)
        self.assertEqual(p4.comandos[0].receptor,p4)
        self.assertEqual(p4.comandos[1].esCerrar(),True)
        self.assertEqual(p4.comandos[1].receptor,p4)
        #Cerrar puertas
        self.juego.cerrarPuertas()
        self.assertEqual(len(p1.comandos),1)
        self.assertEqual(p1.esPuerta(),True)
        self.assertEqual(p1.comandos[0].esAbrir(),True)
        self.assertEqual(p1.comandos[0].receptor,p1)
        self.assertEqual(len(p2.comandos),1)
        self.assertEqual(p2.esPuerta(),True)
        self.assertEqual(p2.comandos[0].esAbrir(),True)
        self.assertEqual(p2.comandos[0].receptor,p2)
        self.assertEqual(len(p3.comandos),1)
        self.assertEqual(p3.esPuerta(),True)
        self.assertEqual(p3.comandos[0].esAbrir(),True)
        self.assertEqual(p3.comandos[0].receptor,p3)
        self.assertEqual(len(p4.comandos),1)
        self.assertEqual(p4.esPuerta(),True)
        self.assertEqual(p4.comandos[0].esAbrir(),True)
        self.assertEqual(p4.comandos[0].receptor,p4)
        #Comandos personaje posición Habitación 1
        personaje = self.juego.personaje
        self.assertEqual(len(coms:=personaje.obtenerComandos(personaje)),5)
        coms[0].ejecutar(personaje)#Abrir armario 1
        coms= personaje.obtenerComandos(personaje)
        coms[0].ejecutar(personaje)#Entrar en armario 1 
        coms= personaje.obtenerComandos(personaje)
        coms[0].ejecutar(personaje)#Coger Banana
        self.assertEqual(len(bolsa:=personaje.bolsa.hijos),1)
        self.assertEqual((banana:=bolsa[0]).esBanana(),True)
        self.assertEqual(len((coms:=banana.obtenerComandos(personaje))),2)
        coms[0].ejecutar(personaje)#Soltar banana
        self.assertEqual(banana.padre,personaje.posicion)
        coms= personaje.obtenerComandos(personaje)
        coms[0].ejecutar(personaje)#Volver a coger banana
        coms= personaje.bolsa.hijos[0].obtenerComandos(personaje)
        vida = personaje.vidas
        coms[1].ejecutar(personaje)#Comer banana
        self.assertEqual(personaje.vidas, vida + banana.vida) #Se le sumará la vida de la banana
        coms= personaje.obtenerComandos(personaje)
        coms[0].ejecutar(personaje)#Irse del armario
        coms= personaje.obtenerComandos(personaje)
        coms[2].ejecutar(personaje)#Cogemos escudo
        self.assertEqual(len(hijos:=personaje.bolsa.hijos),1)
        self.assertEqual((esc:=hijos[0]).esEscudo(),True)
        self.assertEqual(len(coms:=esc.comandos),2)
        self.assertEqual(coms[0].esSoltar(),True)
        self.assertEqual(coms[1].esUsar(),True)
        coms[1].ejecutar(personaje)
        self.assertEqual(len(personaje.bolsa.hijos),0)#Ya no tiene escudo en el inventario
        self.assertEqual(personaje.cuerpo.mIzquierda,esc)#Tiene escudo en la mano izquierda
        coms= personaje.obtenerComandos(personaje)
        bomba=coms[2].receptor
        vidas = personaje.vidas
        coms[2].ejecutar(personaje)#Detonamos la bomba
        self.assertEqual(bomba.activa,False)
        self.assertEqual(personaje.vidas,vidas-bomba.dano)#Comprobamos que el personaje ha recibido daño de la explosión
        coms= personaje.obtenerComandos(personaje)
        coms[3].ejecutar(personaje)#Abrimos la puerta 1 - 2
        coms= personaje.obtenerComandos(personaje)
        coms[3].ejecutar(personaje)#Entramos en la habitación 2
        hab2 = self.juego.obtenerHabitacion(2)
        self.assertEqual(personaje.posicion,hab2)#Comprobamos que la posición del personaje es la habitación 2
        coms= personaje.obtenerComandos(personaje)
        coms[0].ejecutar(personaje)#Cogemos la espada de metal.
        self.assertEqual(len(hijos:=personaje.bolsa.hijos),1)
        self.assertEqual((esc:=hijos[0]).esEspada(),True)
        self.assertEqual(esc.material.esMetal(),True)
        self.assertEqual(len(coms:=esc.comandos),2)
        self.assertEqual(coms[0].esSoltar(),True)
        self.assertEqual(coms[1].esUsar(),True)
        coms[1].ejecutar(personaje)
        self.assertEqual(len(personaje.bolsa.hijos),0)#Ya no tiene la espada de metal en el inventario
        self.assertEqual(personaje.cuerpo.mDerecha,esc)#Tiene la espada en la mano derecha
        personaje.atacar()
        personaje.atacar()
        bicho2 = self.juego.bichos[1]
        self.assertEqual(bicho2.estaVivo(),False) #Acabamos con el bicho 2 perezoso con 2 golpes gracias a la espada.
        coms= personaje.obtenerComandos(personaje)
        coms[2].ejecutar(personaje)
        coms= personaje.obtenerComandos(personaje)
        coms[2].ejecutar(personaje)#Entramos en la habitación 4
        hab4 = self.juego.obtenerHabitacion(4)
        self.assertEqual(personaje.posicion,hab4)#Comprobamos que la posición del personaje es la habitación 4
        coms= personaje.obtenerComandos(personaje)
        bomba=coms[0].receptor
        vidas = personaje.vidas
        coms[0].ejecutar(personaje)#Detonamos la bomba
        self.assertEqual(bomba.activa,False)
        self.assertEqual(personaje.vidas,vidas-bomba.dano)#Comprobamos que el personaje ha recibido daño de la explosión
        personaje.atacar()
        personaje.atacar()
        bicho4 = self.juego.bichos[3]
        self.assertEqual(bicho4.estaVivo(),False) #Acabamos con el bicho 2 perezoso con 2 golpes gracias a la espada.
        coms= personaje.obtenerComandos(personaje)
        coms[0].ejecutar(personaje)
        coms= personaje.obtenerComandos(personaje)
        coms[0].ejecutar(personaje)#Entramos en el armario 2
        self.assertEqual((arm:=personaje.posicion).esArmario(),True)
        self.assertEqual(arm.num,2)#El armario es el armario 2
        coms= personaje.obtenerComandos(personaje)
        coms[0].ejecutar(personaje)#Abandonamos el armario
        self.assertEqual(personaje.posicion,hab4)#La posición del personaje vuelve a ser la habitación 4
        coms= personaje.obtenerComandos(personaje)
        coms[2].ejecutar(personaje)
        coms= personaje.getCommands(personaje)
        coms[2].ejecutar(personaje)#Entramos en la habitación 3
        hab3 = self.juego.obtenerHabitacion(3)
        self.assertEqual(personaje.posicion,hab3)#Comprobamos que la posición del personaje es la habitación 3
        self.assertEqual((espada:=hab3.hijos[0]).esEspada(),True)
        self.assertEqual(espada.material.esDiamante(),True)#Cogemos y comprobamos la espada de diamante
        espada.comandos[0].ejecutar(personaje)
        espada.comandos[1].ejecutar(personaje)
        self.assertEqual(personaje.cuerpo.mDerecha,espada)#Hemos equipado la espada de diamante
        self.assertEqual((espMetal:=personaje.bolsa.hijos[0]).material.esMetal(),True)#La espada de metal vuelve al inventario al equipar la de diamante.
        espMetal.comandos[1].ejecutar(personaje)#Soltamos la espada de metal
        self.assertEqual(personaje.posicion.hijos[1].material.esMetal(),True)
        personaje.atacar()
        personaje.atacar()
        personaje.atacar()
        self.assertEqual(self.juego.bichos[2].estaVivo(),False)#Matamos a un bicho agresivo con 3 golpes de espada de diamante.
        espada.comandos[0].ejecutar(personaje)
        espada.comandos[1].ejecutar(personaje)
        self.assertEqual((espMetal:=personaje.posicion.hijos[2]).material.esDiamante(),True)#La espada de diamante vuelve a la habitación al soltarse.
        coms= personaje.obtenerComandos(personaje)
        coms[2].ejecutar(personaje)
        coms= personaje.obtenerComandos(personaje)
        coms[2].ejecutar(personaje)#Entramos en la habitación 1
        hab1 = self.juego.obtenerHabitacion(1)
        self.assertEqual(personaje.posicion,hab1)#Comprobamos que la posición del personaje es la habitación 1
        for i in range(1,13):
            self.assertEqual(self.juego.bichos[0].estaVivo(),True)
            personaje.atacar()
        self.assertEqual(self.juego.bichos[0].estaVivo(),False)#Nos toma 12 golpes acabar con un bicho agresivo sin espada.
        self.juego.fase.esFinal()#El juego ha terminado al matar a los bichos.
        print("TEST FUNCIONALES SUPERADAS.")
        
unittest.main()