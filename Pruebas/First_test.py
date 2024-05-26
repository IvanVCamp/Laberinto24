import unittest
import sys
import os
from io import StringIO
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'LaberintoBuilder')))
from LaberintoBuilder.Director import Director
from Ente.Character import Character

class First_test(unittest.TestCase):

    def setUp(self):
        super().setUp()
        sys.stdout_save =sys.stdout
        sys.stdout = StringIO()
        director = Director()
        director.procesar('maze4hab.json')
        self.juego = director.getJuego()
        personaje = Character()
        personaje.seudonimo = "Matías"
        self.juego.agregarPersonaje(personaje)
        sys.stdout=sys.stdout_save

    def testIniciales(self):
        self.assertEqual(self.juego is not None, True)
        self.assertEqual(self.juego.esJuego(),True)
        self.assertEqual(len(self.juego.laberinto.objChildren),4)
        print("TEST INICIAL SUPERADO.\n")
    
    def testHabitaciones(self):
        hab1 = self.juego.laberinto.objChildren[0]
        self.assertEqual(hab1.esHabitacion(),True)
        self.assertEqual(hab1.ref,1)
        self.assertEqual(len(hab1.hijos),3)
        self.assertEqual(hab1.form.esCuadrado(),True)
        self.assertEqual(hab1.form.norte.esPared(),True)
        self.assertEqual(hab1.form.este.esPuerta(),True)
        self.assertEqual(hab1.form.oeste.esPared(),True)
        self.assertEqual(hab1.form.sur.esPuerta(),True)
        #Habitación 2
        hab2 = self.juego.laberinto.objChildren[1]
        self.assertEqual(hab2.esHabitacion(),True)
        self.assertEqual(hab2.ref,2)
        self.assertEqual(len(hab2.objChildren),1)
        self.assertEqual(hab2.form.esCuadrado(),True)
        self.assertEqual(hab2.form.norte.esPuerta(),True)
        self.assertEqual(hab2.form.este.esPuerta(),True)
        self.assertEqual(hab2.form.oeste.esPared(),True)
        self.assertEqual(hab2.form.sur.esPared(),True)
        #Habitación 3
        hab3 = self.juego.laberinto.objChildren[2]
        self.assertEqual(hab3.esHabitacion(),True)
        self.assertEqual(hab3.ref,3)
        self.assertEqual(len(hab3.objChildren),2)
        self.assertEqual(hab3.form.esCuadrado(),True)
        self.assertEqual(hab3.form.norte.esPared(),True)
        self.assertEqual(hab3.form.este.esPared(),True)
        self.assertEqual(hab3.form.oeste.esPuerta(),True)
        self.assertEqual(hab3.form.sur.esPuerta(),True)
        #Habitación 4
        hab4 = self.juego.laberinto.objChildren[3]
        self.assertEqual(hab4.esHabitacion(),True)
        self.assertEqual(hab4.ref,4)
        self.assertEqual(len(hab4.objChildren),2)
        self.assertEqual(hab4.form.esCuadrado(),True)
        self.assertEqual(hab4.form.norte.esPuerta(),True)
        self.assertEqual(hab4.form.este.esPared(),True)
        self.assertEqual(hab4.form.oeste.esPuerta(),True)
        self.assertEqual(hab4.form.sur.esPared(),True)

        print("ESTRUCTURA DE LAS HABITACIONES COMPROBADAS.\n")


    def testBichos(self):
        bichos = self.juego.bichos
        #Bicho 1
        b1 = bichos[0]
        self.assertEqual(b1.numero_identificador,1)
        self.assertEqual(b1.modo.esAgresivo(),True)
        self.assertEqual(b1.posicion,self.juego.laberinto.objChildren[0])
        self.assertEqual(b1.juego,self.juego)
        self.assertEqual(b1.estado.estaVivo(),True)
        #Bicho 2
        b2 = bichos[1]
        self.assertEqual(b2.numero_identificador,2)
        self.assertEqual(b2.modo.esPerezoso(),True)
        self.assertEqual(b2.posicion,self.juego.laberinto.objChildren[1])
        self.assertEqual(b2.juego,self.juego)
        self.assertEqual(b2.estado.estaVivo(),True)
        #Bicho 3
        b3 = bichos[2]
        self.assertEqual(b3.numero_identificador,3)
        self.assertEqual(b3.modo.esAgresivo(),True)
        self.assertEqual(b3.posicion,self.juego.laberinto.objChildren[2])
        self.assertEqual(b3.juego,self.juego)
        self.assertEqual(b3.estado.estaVivo(),True)
        #Bicho 4
        b4 = bichos[3]
        self.assertEqual(b4.numero_identificador,4)
        self.assertEqual(b4.modo.esPerezoso(),True)
        self.assertEqual(b4.posicion,self.juego.laberinto.objChildren[3])
        self.assertEqual(b4.juego,self.juego)
        self.assertEqual(b4.estado.estaVivo(),True)
        
        print("TEST DE LOS BICHOS SUPERADO.\n")

    def testPersonaje(self):
        personaje = self.juego.prota
        self.assertEqual(personaje.seudonimo,"Matías")
        self.assertEqual(personaje.posicion,self.juego.getHab(1))
        self.assertEqual(personaje.estado.estaVivo(),True)
        self.assertEqual(personaje.juego, self.juego)
        self.assertEqual(personaje.children.eschildren(),True)
        self.assertEqual(len(personaje.mochila.children),0)
        self.assertEqual(personaje.cuerpo.esCuerpo(),True)
        self.assertEqual(personaje.cuerpo.brazoAtaque is None, True)
        print("TEST DEL PERSONAJE SUPERADO.\n")

    def testPuertas(self):
        #Puerta 1
        p1 = self.juego.getHab(1).form.sur
        self.assertEqual(p1.esPuerta(),True)
        self.assertEqual(p1.lado1,self.juego.getHab(1))
        self.assertEqual(p1.lado2,self.juego.getHab(2))
        self.assertEqual(p1.commands[0].esAbrir(),True)
        self.assertEqual(p1.commands[0].receiver,p1)
        self.assertEqual(p1.estaAbierta(),False)
        #Puerta 2
        p2 = self.juego.getHab(2).form.este
        self.assertEqual(p2.esPuerta(),True)
        self.assertEqual(p2.lado1,self.juego.getHab(2))
        self.assertEqual(p2.lado2,self.juego.getHab(4))
        self.assertEqual(p2.commands[0].esAbrir(),True)
        self.assertEqual(p2.commands[0].receiver,p2)
        self.assertEqual(p2.estaAbierta(),False)
        #Puerta 3
        p3 = self.juego.getHab(4).form.norte
        self.assertEqual(p3.esPuerta(),True)
        self.assertEqual(p3.lado1,self.juego.getHab(4))
        self.assertEqual(p3.lado2,self.juego.getHab(3))
        self.assertEqual(p3.commands[0].esAbrir(),True)
        self.assertEqual(p3.commands[0].receiver,p3)
        self.assertEqual(p3.estaAbierta(),False)
        #Puerta 4
        p4 = self.juego.getHab(3).form.oeste
        self.assertEqual(p4.esPuerta(),True)
        self.assertEqual(p4.lado1,self.juego.getHab(3))
        self.assertEqual(p4.lado2,self.juego.getHab(1))
        self.assertEqual(p4.commands[0].esAbrir(),True)
        self.assertEqual(p4.commands[0].receiver,p4)
        self.assertEqual(p4.estaAbierta(),False)
        print("TEST DE PUERTAS SUPERADO.\n")

    def testArmarios(self):
        #Armario 1
        arm1 = None
        pad1 = None
        for hijo in (pad1:=self.juego.getHab(1)).objChildren:
            if hijo.esArmario():
                arm1 = hijo
        self.assertEqual(arm1.ref,1)
        self.assertEqual(arm1.padre,pad1)
        self.assertEqual(len(arm1.objChildren),1)
        self.assertEqual(arm1.form.esCuadrado(),True)
        self.assertEqual(arm1.form.norte.esPared(),True)
        self.assertEqual(arm1.form.este.esPared(),True)
        self.assertEqual(arm1.form.oeste.esPared(),True)
        self.assertEqual((p1:=arm1.form.sur).esPuerta(),True)
        self.assertEqual(p1.estaAbierta(),False)
        self.assertEqual(p1.commands[0].esAbrir(),True)
        self.assertEqual(p1.commands[0].receiver,p1)
        #Armario 2
        arm2 = None
        pad2 = None
        for hijo in (pad2:=self.juego.getHab(4)).objChildren:
            if hijo.esArmario():
                arm2 = hijo
        self.assertEqual(arm2.ref,2)
        self.assertEqual(arm2.padre,pad2)
        self.assertEqual(len(arm2.objChildren),0)
        self.assertEqual(arm2.form.esCuadrado(),True)
        self.assertEqual(arm2.form.norte.esPared(),True)
        self.assertEqual(arm2.form.este.esPared(),True)
        self.assertEqual(arm2.form.oeste.esPared(),True)
        self.assertEqual((p2:=arm1.form.sur).esPuerta(),True)
        self.assertEqual(p2.estaAbierta(),False)
        self.assertEqual(p2.commands[0].esAbrir(),True)
        self.assertEqual(p2.commands[0].receiver,p2)

        print("TEST DE ARMARIOS SUPERADO.")

    def testTuneles(self):
        tunel = None
        padre = None
        for hijo in (padre:=self.juego.getHab(3)).objChildren:
            if hijo.esTunel():
                tunel = hijo
        self.assertEqual(tunel.padre,padre)
        self.assertEqual(tunel.laberinto,None)
        print("TEST DE TÚNELES SUPERADO.\n")
    
    def testbombas(self):
        #Bomba 1
        bomba1 = None
        pad1 = None
        for hijo in (pad1:=self.juego.getHab(1)).objChildren:
            if hijo.esBomba():
                bomba1 = hijo
        self.assertEqual(bomba1.ref,1)
        self.assertEqual(bomba1.activa,True)
        self.assertEqual(bomba1.padre,pad1)
        self.assertEqual(bomba1.commands[0].esEntrar(),True)
        self.assertEqual(bomba1.commands[0].receiver,bomba1)
        #Bomba 2
        bomba2 = None
        pad2 = None
        for hijo in (pad2:=self.juego.getHab(4)).objChildren:
            if hijo.esBomba():
                bomba2 = hijo
        self.assertEqual(bomba2.ref,2)
        self.assertEqual(bomba2.activa,True)
        self.assertEqual(bomba2.padre,pad2)
        self.assertEqual(bomba2.commands[0].esEntrar(),True)
        self.assertEqual(bomba2.commands[0].receiver,bomba2)
        print("TEST DE BOMBAS SUPERADO.")

    def testObjetos(self):
        #Objetos Habitación 1
        hab1 = self.juego.getHab(1)

        arm1 = hab1.objChildren[0]
        self.assertEqual((bistec:=arm1.objChildren[0]).esBistec(),True)
        self.assertEqual((com1:=bistec.commands[0]).esCoger(),True)
        self.assertEqual(com1.receiver,bistec)
        #Objetos Habitación 2
        hab2 = self.juego.getHab(2)
        self.assertEqual((Katana1:=hab2.objChildren[0]).esKatana(),True)
        self.assertEqual(Katana1.ref,1)
        self.assertEqual(Katana1.commands[0].esCoger(),True)
        self.assertEqual(Katana1.commands[0].receiver,Katana1)
        #Objetos Habitación 3
        hab3 = self.juego.getHab(3)
        self.assertEqual((Katana2:=hab3.objChildren[0]).esKatana(),True)
        self.assertEqual(Katana2.ref,1)
        self.assertEqual(Katana2.commands[0].esCoger(),True)
        self.assertEqual(Katana2.commands[0].receiver,Katana2)
        print("TEST DE OBJETOS SUPERADO.\n")

    def testFuncionalidades(self):
        #Abrir puertas
        self.juego.openDoors()
        p1 = self.juego.getHab(1).form.sur
        p2 = self.juego.getHab(2).form.este
        p3 = self.juego.getHab(4).form.norte
        p4 = self.juego.getHab(3).form.oeste
        self.assertEqual(len(p1.commands),2)
        self.assertEqual(p1.esPuerta(),True)
        self.assertEqual(p1.commands[0].esEntrar(),True)
        self.assertEqual(p1.commands[0].receiver,p1)
        self.assertEqual(p1.commands[1].esCerrar(),True)
        self.assertEqual(p1.commands[1].receiver,p1)
        self.assertEqual(len(p2.commands),2)
        self.assertEqual(p2.esPuerta(),True)
        self.assertEqual(p2.commands[0].esEntrar(),True)
        self.assertEqual(p2.commands[0].receiver,p2)
        self.assertEqual(p2.commands[1].esCerrar(),True)
        self.assertEqual(p2.commands[1].receiver,p2)
        self.assertEqual(len(p3.commands),2)
        self.assertEqual(p3.esPuerta(),True)
        self.assertEqual(p3.commands[0].esEntrar(),True)
        self.assertEqual(p3.commands[0].receiver,p3)
        self.assertEqual(p3.commands[1].esCerrar(),True)
        self.assertEqual(p3.commands[1].receiver,p3)
        self.assertEqual(len(p4.commands),2)
        self.assertEqual(p4.esPuerta(),True)
        self.assertEqual(p4.commands[0].esEntrar(),True)
        self.assertEqual(p4.commands[0].receiver,p4)
        self.assertEqual(p4.commands[1].esCerrar(),True)
        self.assertEqual(p4.commands[1].receiver,p4)
        #Cerrar puertas
        self.juego.openDoors()
        self.assertEqual(len(p1.commands),1)
        self.assertEqual(p1.esPuerta(),True)
        self.assertEqual(p1.commands[0].esAbrir(),True)
        self.assertEqual(p1.commands[0].receiver,p1)
        self.assertEqual(len(p2.commands),1)
        self.assertEqual(p2.esPuerta(),True)
        self.assertEqual(p2.commands[0].esAbrir(),True)
        self.assertEqual(p2.commands[0].receiver,p2)
        self.assertEqual(len(p3.commands),1)
        self.assertEqual(p3.esPuerta(),True)
        self.assertEqual(p3.commands[0].esAbrir(),True)
        self.assertEqual(p3.commands[0].receiver,p3)
        self.assertEqual(len(p4.commands),1)
        self.assertEqual(p4.esPuerta(),True)
        self.assertEqual(p4.commands[0].esAbrir(),True)
        self.assertEqual(p4.commands[0].receiver,p4)
        #commands personaje posición Habitación 1
        personaje = self.juego.prota
        self.assertEqual(len(coms:=personaje.obtenerComandos(personaje)),5)
        coms[0].ejecutar(personaje)#Abrir armario 1
        coms= personaje.obtenerComandos(personaje)
        coms[0].ejecutar(personaje)#Entrar en armario 1 
        coms= personaje.obtenerComandos(personaje)
        coms[0].ejecutar(personaje)#Coger bistec
        self.assertEqual(len(mochila:=personaje.mochila.children),1)
        self.assertEqual((bistec:=mochila[0]).esBistec(),True)
        self.assertEqual(len((coms:=bistec.obtenerComandos(personaje))),2)
        coms[0].ejecutar(personaje)#Soltar bistec
        self.assertEqual(bistec.padre,personaje.posicion)
        coms= personaje.obtenerComandos(personaje)
        coms[0].ejecutar(personaje)#Volver a coger bistec
        coms= personaje.mochila.children[0].obtenerComandos(personaje)
        vida = personaje.corazones
        coms[1].ejecutar(personaje)#Comer bistec
        self.assertEqual(personaje.corazones, vida + bistec.vida) #Se le sumará la vida de la bistec
        coms= personaje.obtenerComandos(personaje)
        coms[0].ejecutar(personaje)#Irse del armario
        coms= personaje.obtenerComandos(personaje)
        coms[2].ejecutar(personaje)#Cogemos escudo
        self.assertEqual(len(hijos:=personaje.mochila.children),1)
        self.assertEqual((esc:=hijos[0]).esEscudo(),True)
        self.assertEqual(len(coms:=esc.commands),2)
        self.assertEqual(coms[0].esSoltar(),True)
        self.assertEqual(coms[1].esUsar(),True)
        coms[1].ejecutar(personaje)
        self.assertEqual(len(personaje.mochila.children),0)#Ya no tiene escudo en el inventario
        coms= personaje.obtenerComandos(personaje)
        bomba=coms[2].receiver
        corazones = personaje.corazones
        coms[2].ejecutar(personaje)#Detonamos la bomba
        self.assertEqual(bomba.activa,False)
        self.assertEqual(personaje.corazones,corazones-bomba.damage)#Comprobamos que el personaje ha recibido daño de la explosión
        coms= personaje.obtenerComandos(personaje)
        coms[3].ejecutar(personaje)#Abrimos la puerta 1 - 2
        coms= personaje.obtenerComandos(personaje)
        coms[3].ejecutar(personaje)#Entramos en la habitación 2
        hab2 = self.juego.getHab(2)
        self.assertEqual(personaje.posicion,hab2)#Comprobamos que la posición del personaje es la habitación 2
        coms= personaje.obtenerComandos(personaje)
        coms[0].ejecutar(personaje)#Cogemos la Katana de metal.
        self.assertEqual(len(hijos:=personaje.mochila.children),1)
        self.assertEqual((esc:=hijos[0]).esKatana(),True)
        self.assertEqual(len(coms:=esc.commands),2)
        self.assertEqual(coms[0].esSoltar(),True)
        self.assertEqual(coms[1].esUsar(),True)
        coms[1].ejecutar(personaje)
        self.assertEqual(len(personaje.mochila.hijos),0)#Ya no tiene la Katana de metal en el inventario
        self.assertEqual(personaje.cuerpo.brazoAtaque,esc)#Tiene la Katana en la mano derecha
        personaje.atacar()
        personaje.atacar()
        bicho2 = self.juego.bichos[1]
        self.assertEqual(bicho2.estaVivo(),False) #Acabamos con el bicho 2 perezoso con 2 golpes gracias a la Katana.
        coms= personaje.obtenerComandos(personaje)
        coms[2].ejecutar(personaje)
        coms= personaje.obtenerComandos(personaje)
        coms[2].ejecutar(personaje)#Entramos en la habitación 4
        hab4 = self.juego.getHab(4)
        self.assertEqual(personaje.posicion,hab4)#Comprobamos que la posición del personaje es la habitación 4
        coms= personaje.obtenerComandos(personaje)
        bomba=coms[0].receiver
        corazones = personaje.corazones
        coms[0].ejecutar(personaje)#Detonamos la bomba
        self.assertEqual(bomba.activa,False)
        self.assertEqual(personaje.corazones,corazones-bomba.damage)#Comprobamos que el personaje ha recibido daño de la explosión
        personaje.atacar()
        personaje.atacar()
        bicho4 = self.juego.bichos[3]
        self.assertEqual(bicho4.estaVivo(),False) #Acabamos con el bicho 2 perezoso con 2 golpes gracias a la Katana.
        coms= personaje.obtenerComandos(personaje)
        coms[0].ejecutar(personaje)
        coms= personaje.obtenerComandos(personaje)
        coms[0].ejecutar(personaje)#Entramos en el armario 2
        self.assertEqual((arm:=personaje.posicion).esArmario(),True)
        self.assertEqual(arm.ref,2)#El armario es el armario 2
        coms= personaje.obtenerComandos(personaje)
        coms[0].ejecutar(personaje)#Abandonamos el armario
        self.assertEqual(personaje.posicion,hab4)#La posición del personaje vuelve a ser la habitación 4
        coms= personaje.obtenerComandos(personaje)
        coms[2].ejecutar(personaje)
        coms= personaje.obtenerComandos(personaje)
        coms[2].ejecutar(personaje)#Entramos en la habitación 3
        hab3 = self.juego.getHab(3)
        self.assertEqual(personaje.posicion,hab3)#Comprobamos que la posición del personaje es la habitación 3
        self.assertEqual((Katana:=hab3.hijos[0]).esKatana(),True)
        Katana.commands[0].ejecutar(personaje)
        Katana.commands[1].ejecutar(personaje)
        self.assertEqual(personaje.cuerpo.brazoAtaque,Katana)#Hemos equipado la Katana de diamante
        katana=personaje.mochila.children[0]
        katana.commands[1].ejecutar(personaje)#Soltamos la Katana de metal
        personaje.atacar()
        personaje.atacar()
        personaje.atacar()
        self.assertEqual(self.juego.bichos[2].estaVivo(),False)#Matamos a un bicho agresivo con 3 golpes de Katana de diamante.
        Katana.commands[0].ejecutar(personaje)
        Katana.commands[1].ejecutar(personaje)
        coms= personaje.obtenerComandos(personaje)
        coms[2].ejecutar(personaje)
        coms= personaje.obtenerComandos(personaje)
        coms[2].ejecutar(personaje)#Entramos en la habitación 1
        hab1 = self.juego.getHab(1)
        self.assertEqual(personaje.posicion,hab1)#Comprobamos que la posición del personaje es la habitación 1
        for i in range(1,13):
            self.assertEqual(self.juego.bichos[0].estaVivo(),True)
            personaje.atacar()
        self.assertEqual(self.juego.bichos[0].estaVivo(),False)#Nos toma 12 golpes acabar con un bicho agresivo sin Katana.
        self.juego.fase.esFinal()#El juego ha terminado al matar a los bichos.
        print("TEST FUNCIONALES SUPERADAS.")
        
if __name__ == '__main__':
    unittest.main()