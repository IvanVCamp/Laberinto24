from LaberintoBuilder.Director import Director
from Ente.Character import Character
from GUI import Interfaz
import os

nombre = input("Nick del personaje: ")
personaje = Character()
opcion = input("Opción de juego:\n    1.Jugar con GUI\n    2.Jugar en consola\nSelecciona una opción: ")
jsons = os.listdir('json/')
print("JSON disponibles:")
i = 0
for js in jsons:
    if opcion == '1' and 'rombo' in js:
        print(i,". Forma rombo no disponible con GUI, solo consola.")
    else:
        print(i,". ",js)
    i += 1
json = input("Selecciona un json: ")
json = jsons[int(json)]
if opcion == "1":
    vista = Interfaz()
    vista.starJuego('json/'+json,nombre)

if opcion == "2":
    director = Director()
    director.procesar('json/'+json)
    juego = director.getJuego()
    forma = director.form
    personaje.seudonimo = nombre
    juego.agregarPersonaje(personaje)
    juego.prota = personaje
    while not juego.fase.esFinal():
        if forma == "Cuadrado":
            print("¿Qué deseas hacer?\n    A. Atacar\n    1. Mover al norte\n    2. Mover al este\n    3. Mover al oeste\n    4. Mover al sur\n",
                  "   5. Abrir Puertas\n    6. Lanzar bichos\n    7. Mostrar comandos bolsa\n    8. Mostrar comandos cuerpo\n",   
                  "   H. Obtener hijos de la posición del personaje\n    C. Obtener Comandos\n    I. Mostrar inventario")
        if forma == "Rombo":
            print("¿Qué deseas hacer?\n    A. Atacar\n    1. Mover al noreste\n    2. Mover al noroeste\n    3. Mover al sureste\n    4. Mover al suroeste\n",
              "   5. Abrir Puertas\n    6. Lanzar bichos\n    7. Mostrar comandos bolsa\n    8. Mostrar comandos cuerpo\n",
              "   H. Obtener hijos de la posición del personaje\n    C. Obtener Comandos\n    I. Mostrar inventario")
        eleccion=input()
        if forma == "Cuadrado":
            if eleccion == "1":
                personaje.irAlNorte()
            if eleccion == "2":
                personaje.irAlEste()
            if eleccion == "3":
                personaje.irAlOeste()
            if eleccion == "4":
                personaje.irAlSur()
        if forma == "Rombo":
            if eleccion == "1":
                personaje.irAlNoreste()
            if eleccion == "2":
                personaje.irAlNoroeste()
            if eleccion == "3":
                personaje.irAlSureste()
            if eleccion == "4":
                personaje.irAlSuroeste()
        if eleccion == "5":
            juego.openDoors()
        if eleccion == "6":
            juego.lanzarBichos()
        if eleccion == "7":
            i = 0
            coms=personaje.mochila.getCommands(personaje)
            if len(coms) > 0:
                for com in coms:
                    print("    ",i,". ",com,"\n")
                    i += 1
                el = input()
                el = int(el)
                coms[el].ejecutar(personaje)
            else:
                print("No hay objetos en la bolsa.")
        if eleccion == "8":
            print("    1. ¿De verdad quieres usar el brazo ataque?")
            el = input()
            el = int(el)
            if el == 1:
                i = 0
                if personaje.cuerpo.brazoAtaque is not None:
                    for com in (coms:=personaje.cuerpo.brazoAtaque.commmands):
                        print("    ",i,". ",com,"\n")
                        i += 1
                    ele = input()
                    ele = int(ele)
                    coms[ele].ejecutar(personaje)
                else:
                    print("No hay nada en la mano derecha.")

        if eleccion == "a" or eleccion == "A":
            personaje.atacar()

        if eleccion == "i" or eleccion == "I":
            i = 0
            for obj in personaje.mochila.children:
                print("    ",i,". ",obj,"\n")
                i+=1
            el = input()
            el = int(el)
            i = 0
            for com in personaje.mochila.children[el].getCommands(personaje):
                print("    ",i,". ",com,"\n")
                i += 1
            ele = input()
            ele = int(ele)
            personaje.mochila.children[el].getCommands(personaje)[ele].ejecutar(personaje)


        if eleccion == "h" or eleccion == "H":
            hijos = juego.getChildrenPosition()
            if len(hijos) > 0:
                print("Selecciona hijo: ")
                i = 0
                for hijo in hijos:
                    print("    ",i,". ",hijo)
                    i+=1
                el = input()
                el = int(el)
                if el < len(hijos) and el >= 0:
                    hijos[el].entrar(personaje)
                else:
                    print("Has introducido un índice incorrecto.")
            else:
                print("No hay hijos disponibles.")

        if eleccion == "c" or eleccion == "C":
            coms = personaje.obtenerComandos(personaje)
            if len(coms) > 0:
                print("Selecciona comando: ")
                i = 0
                for com in coms:
                    print("    ",i,". ",com)
                    i+=1
                el = input()
                el = int(el)
                if el < len(coms) and el >= 0:
                    coms[el].ejecutar(personaje)
                else:
                    print("Has introducido un índice incorrecto.")
            else:
                print("No hay comandos disponibles.")