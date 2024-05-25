from Builder.Builder import Director
from Ente.Character import Character
import pygame # type: ignore

class Interfaz():
    
    def __init__(self):
        self.windh = 1500
        self.windw = 900
        self.width = None
        self.height = None
        self.window = None
        self.juego = None
        self.hero = None
        self.heroM = None
        self.corazonesP = None
        self.npcP = {}
        self.bistec = {}
        self.armariosP = {}
        self.openC = None
        self.close = None
        self.btnOpen = None
        self.orInitialize = None
        self.rectBIn = None
        self.orBody = None
        self.orComd = []
        self.gatesP = {}
        self.mochila = {}
        self.katanasP = {}
        self.armaP = None
        self.bombasP = {}
        pygame.init()
        self.window = pygame.display.set_mode((self.windh,self.windw))
        pygame.display.set_caption("JUEGO LABERINTO 24")
    
    def startJuego(self,json,nombre):
        director = Director()
        director.procesar(json)
        self.juego = director.obtenerJuego()
        
        hero = Character()
        hero.name = nombre
        hero.subscribePosicion(self)
        hero.subscribeVida(self)
        
        self.juego.addCharacter(hero)
        self.hero = self.juego.hero

        h1= self.juego.getHab(1)
        h1.setPunto((0,0))
        h1.calcularPosicion()
        
        self.redimensionar()
        
        maxCord, maxOrd = float('-inf'), float('-inf')
        for hijo in self.juego.laberinto.hijos:
            punto = hijo.getPunto()
            if punto[0] > maxCord:
                maxCord = punto[0]
            if punto[1] > maxOrd:
                maxOrd = punto[1]

        maxCord += 1
        maxOrd += 1
        ajuste = 0.90
        self.width = int(self.windw / maxCord) * ajuste
        self.height = int(self.windw / maxOrd) * ajuste

        for hijo in self.juego.laberinto.hijos:
            pt = hijo.getPunto()
            x_real = pt[0] * self.width
            y_real = pt[1] * self.height
            hijo.setExtent((self.width, self.height))
            hijo.setPunto((x_real, y_real))

        self.drawMaze()


    def redimensionar(self):
        cordMin, ordMin = float('inf'), float('inf')

        for hijo in self.juego.laberinto.hijos:
            p = hijo.obtenerPunto()
            if p[0] < cordMin:
                cordMin = p[0]
            if p[1] < ordMin:
                ordMin = p[1]

        newCord, newOrd = abs(cordMin), abs(ordMin)

        for hijo in self.juego.laberinto.hijos:
            x, y = hijo.gePoint()
            hijo.setPunto((x + newCord, y + newOrd))

    
    def drawMaze(self):

        if self.juego is None:
            return

        def cargar_imagen(ruta, escala):
            return pygame.transform.scale(pygame.image.load(ruta), escala)

        def manejar_eventos():
            nonlocal running, visualMochila, visualCuerpo
            keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if keys[pygame.K_UP]:
                    self.hero.irAlNorte()
                if keys[pygame.K_DOWN]:
                    self.hero.irAlSur()
                if keys[pygame.K_RIGHT]:
                    self.hero.irAlEste()
                if keys[pygame.K_LEFT]:
                    self.hero.irAlOeste()
                if keys[pygame.K_b]:
                    self.juego.lanzarnpc()
                if keys[pygame.K_p]:
                    self.juego.opengates()
                if keys[pygame.K_a]:
                    self.hero.atacar()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if self.open.collidepoint(pos):
                        self.juego.opengates()
                    if self.close.collidepoint(pos):
                        self.juego.cerrargates()
                    if self.orInitialize.collidepoint(pos):
                        self.juego.lanzarnpc()
                    if self.rectBIn.collidepoint(pos):
                        visualMochila = not visualMochila
                        visualCuerpo = False
                    if self.openC.collidepoint(pos):
                        visualCuerpo = not visualCuerpo
                        visualMochila = False
                    for com in self.orComd:
                        if com[0].collidepoint(pos):
                            com[1].ejecutar(self.hero)

        def renderizar_objetos():
            self.window.blit(self.capaLaberinto, (0, 0))
            for gate in self.gatesP.values():
                if gate[1] == "abierta":
                    pygame.draw.rect(self.window, colorFondo, (gate[0][0] - 10, gate[0][1] - 10, 60, 60))
            self.window.blit(self.corazonesP, (self.windh - 450, 20))
            for bicho in self.npcP.values():
                if bicho[0] == '-Agresivo:':
                    self.window.blit(npcA, bicho[1])
                if bicho[0] == '-Perezoso:':
                    self.window.blit(npcP, bicho[1])
            for armario in self.armariosP.values():
                if armario[0] == 'abierto':
                    self.window.blit(armarioOpened, armario[1])
            for obj in self.mochila.values():
                if obj[0] == "Bistec":
                    self.window.blit(Bistec, obj[1])
                if obj[0] == "katana":
                    self.window.blit(ktn, obj[2])
            for bomba in self.bombasP.values():
                if bomba[0] == "Activa":
                    self.window.blit(bombaA, bomba[1])
                if bomba[0] == "Inactiva":
                    self.window.blit(bombaI, bomba[1])
            for katana in self.katanasP.values():
                self.window.blit(ktn, katana[1])
            for bist in self.bistec.values():
                self.window.blit(Bistec, bist)
            self.visualopengates()
            self.visualCerrargates()
            self.visualstartJuego()
            if visualMochila:
                self.visualComandos(self.hero.mochila)
                self.visualBMochila("Cerrar")
                self.visualopenCuerpo("open")
            elif visualCuerpo:
                self.visualBMochila("open")
                self.visualopenCuerpo("Cerrar")
                self.visualComandos(self.hero.cuerpo)
            else:
                self.visualComandos()
                self.visualBMochila("open")
                self.visualopenCuerpo("open")
            if self.armaP is not None:
                if self.armaP[0] == "katana":
                    self.window.blit(ktn, self.armaP[2])
                    self.window.blit(heroe, self.heroM)
            for armario in self.armariosP.values():
                if armario[0] == 'cerrado':
                    self.window.blit(armarioCerrao, armario[1])
            pygame.display.update()

        # Cargar imágenes
        heroe = cargar_imagen("GUI/img/prota.png", (self.windw // 12, self.windw // 12))
        colorFondo = (58, 66, 70)
        npcA = cargar_imagen("GUI/img/bicho-agresivo.png", (self.windw // 13, self.windw // 13))
        npcP = cargar_imagen("GUI/img/bicho-perezoso.png", (self.windw // 13, self.windw // 13))
        Bistec = cargar_imagen("GUI/img/Bistec.png", (self.windw // 15, self.windw // 15))
        ktn = cargar_imagen("GUI/img/katana.png", (self.windw // 20, self.windw // 20))
        bombaA = cargar_imagen("GUI/img/bomba_activa.png", (self.windw // 20, self.windw // 20))
        bombaI = cargar_imagen("GUI/img/bomba_inactiva.png", (self.windw // 20, self.windw // 20))
        armarioCerrao = cargar_imagen("GUI/img/closedwardrobe.png", (self.windw // 12, self.windw // 12))
        armarioOpened = cargar_imagen("GUI/img/openwardrobe.png", (self.windw // 12, self.windw // 12))

        visualMochila = False
        visualCuerpo = False
        running = True

        # Preparar la ventana y la capa de laberinto
        self.window.fill((0, 0, 0))
        self.capaLaberinto = pygame.Surface((self.windw, self.windh))
        self.btnOpen = pygame.Surface((200, 50))
        self.capaLaberinto.fill(colorFondo)

        # Inicializar visualización del laberinto
        self.juego.laberinto.aceptar(self)
        self.visualhero()
        self.visualcorazoneshero()
        self.hero.mochila.observarmochila(self)
        self.hero.cuerpo.agregarObservadoresCuerpo(self)
        self.visualmochila(self.hero.mochila)

        for npc in self.juego.npc:
            print(npc.corazones)
            npc.suscribirPosicion(self)
            npc.suscribirVida(self)
            self.visualnpc(npc)

        # Bucle principal del juego
        while not self.juego.fase.esFinal() and running:
            manejar_eventos()
            renderizar_objetos()

        # Finalizar NPCs al cerrar la ventana
        self.juego.terminarnpc()

        # Mostrar imágenes de final del juego
        heroe = cargar_imagen("GUI/img/prota.png", (self.windw // 2, self.windw // 2))
        npcA = cargar_imagen("GUI/img/bicho-agresivo.png", (self.windw // 2, self.windw // 2))
        npcP = cargar_imagen("GUI/img/bicho-perezoso.png", (self.windw // 2, self.windw // 2))

        while self.juego.fase.esFinal() and running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.window.fill(colorFondo)
            if self.juego.ganahero:
                self.window.blit(heroe, (100, 100))
                self.window.blit(pygame.font.Font(None, 100).render("Has ganado", True, (255, 255, 255)), (800, 500))
            else:
                self.window.blit(npcA, (100, 300))
                self.window.blit(npcP, (600, 300))
                self.window.blit(pygame.font.Font(None, 100).render("Has perdido", True, (255, 255, 255)), (1020, 90))
            pygame.display.update()

    
    def visualopengates(self):
        self.open = pygame.draw.rect(self.window, (255, 255, 0), (910, 80, 170, 50))
        self.window.blit(pygame.font.Font(None, 32).render("open gates", True, (0,0,0)),(920,90))
        
    def visualCerrargates(self):
        self.close = pygame.draw.rect(self.window, (255, 255, 0), (1090, 80, 180, 50))
        self.window.blit(pygame.font.Font(None, 32).render("Cerrar gates", True, (0,0,0)),(1100,90))

    def visualstartJuego(self):
        self.orInitialize = pygame.draw.rect(self.window, (255, 255, 0), (1280, 80, 160, 50))
        self.window.blit(pygame.font.Font(None, 32).render("start Juego", True, (0,0,0)),(1290,90))

    def visualBMochila(self,texto):
        self.rectBIn = pygame.draw.rect(self.window, (255, 255, 0), (1040, 750, 80, 50))
        self.window.blit(pygame.font.Font(None, 32).render("Mochila", True, (255,255,255)),(910,760))
        self.window.blit(pygame.font.Font(None, 32).render(texto, True, (0,0,0)),(1050,760))
    
    def visualopenCuerpo(self,texto):
        self.openC = pygame.draw.rect(self.window, (255, 255, 0), (1130, 750, 160, 50))
        self.window.blit(pygame.font.Font(None, 32).render(texto+" Cuerpo", True, (0,0,0)),(1140,760))
        
    def visualComandos(self,cont=None):
        a = 880
        b = 125
        self.orComd = []
        if cont is None:
            n = self.hero
        else:
            n = cont
        for c in n.getCommands(self.hero):
            ex = len(str(c))*12
            self.orComd.append((pygame.draw.rect(self.window, (255, 255, 0), (a, b, ex, 50)), c))
            self.window.blit(pygame.font.Font(None, 32).render(str(c), True, (0,0,0)),(a + 10,b + 10))
            b += 60


    def visualhero(self):
        if self.hero is None:
            return self

        contenedor = self.juego.hero.posicion
        ancho, alto = contenedor.getExtent()
        punto_x, punto_y = contenedor.getPunto()
        
        centro_x = punto_x + (ancho / 2) - 30
        centro_y = punto_y + (alto / 2) - 50

        if contenedor.esArmario():
            centro_x += 30
            centro_y += 50

        self.heroM = (centro_x, centro_y)
        self.visualCuerpo()

    def visualCuerpo(self):
        self.visualArma()
        self.visualDefensa()

    def visualArma(self):
        self.armaP = None
        arma = self.hero.cuerpo.obtenermDerecha()
        if arma is not None:
            pos_x = self.heroM[0] + 32
            pos_y = self.heroM[1] + 25
            if arma.eskatana():
                self.armaP = ("katana", (pos_x, pos_y))

    def visualDefensa(self):
        self.defensaP = None
        defensa = self.hero.cuerpo.obtenermIzquierda()
        if defensa is not None:
            pos_x = self.heroM[0] + 10
            pos_y = self.heroM[1] + 35
            if defensa.esEscudo():
                self.defensaP = ("Escudo", (pos_x, pos_y))

    def visualBicho(self, bicho):
        self.npcP[bicho.num] = ()
        contenedor = bicho.posicion
        ancho, alto = contenedor.getExtent()
        punto_x, punto_y = contenedor.getPunto()
        
        centro_x = punto_x + (ancho / 2) + 20
        centro_y = punto_y + (alto / 2) + 20
        
        self.npcP[bicho.num] = (str(bicho.modo), (centro_x, centro_y))

    def visualBistec(self, Bistec):
        self.bistec[str(Bistec)] = (-100, -100)
        if Bistec.padre.esHabitacion():
            contenedor = Bistec.padre
            ancho, alto = contenedor.getExtent()
            punto_x, punto_y = contenedor.getPunto()
            
            posicion_x = punto_x + ancho - 100
            posicion_y = punto_y + alto - 100
            
            self.bistec[str(Bistec)] = (posicion_x, posicion_y)


    def corazonesBicho(self,bicho):
        if bicho.corazones == 0:
            self.npcP.pop(bicho.num)

    def visualcorazoneshero(self):
        corazones_texto = f"corazones {self.hero}: {self.hero.corazones}"
        font = pygame.font.Font(None, 40)
        self.corazonesP = font.render(corazones_texto, True, (255, 255, 255))

    def visitarHabitacion(self,hab):
        self.drawContenedorRectangular(hab.forma,1)
    
    def visitarArmario(self,arm):
        arm.suscribirAbierto(self)
        self.visualArmario(arm)

    def visualArmario(self, arm):
        self.armariosP[arm.num] = ()
        contenedor = arm.padre
        punto_x, punto_y = contenedor.getPunto()
        
        nueva_pos_x = punto_x + 20
        nueva_pos_y = punto_y + 10
        
        arm.setExtent((0, 0))
        arm.setPunto((nueva_pos_x, nueva_pos_y))
        
        estado = "abierto" if arm.estaAbierto() else "cerrado"
        self.armariosP[arm.num] = (estado, (nueva_pos_x, nueva_pos_y))

    def visualgate(self, gate):
        self.gatesP[str(gate)] = ()
        punto_x, punto_y = 0, 0
        
        if gate.lado1.getPunto()[0] > gate.lado2.getPunto()[0]:
            punto_x = gate.lado1.getPunto()[0]
            punto_y = gate.lado1.getPunto()[1] + gate.lado1.getExtent()[1] / 2
        elif gate.lado2.getPunto()[0] > gate.lado1.getPunto()[0]:
            punto_x = gate.lado2.getPunto()[0]
            punto_y = gate.lado2.getPunto()[1] + gate.lado2.getExtent()[1] / 2
        else:
            if gate.lado1.getPunto()[1] > gate.lado2.getPunto()[1]:
                punto_x = gate.lado1.getPunto()[0] + gate.lado1.getExtent()[0] / 2
                punto_y = gate.lado1.getPunto()[1]
            else:
                punto_x = gate.lado2.getPunto()[0] + gate.lado2.getExtent()[0] / 2
                punto_y = gate.lado2.getPunto()[1]

        estado = "abierta" if gate.estaAbierta() else "cerrada"
        self.gatesP[str(gate)] = ((punto_x, punto_y), estado)

    def visualmochila(self, mochila):
        self.mochila = {}
        pos_x, pos_y = 910, 800

        for obj in mochila.hijos:
            if obj.esBistec():
                self.mochila[str(obj)] = ("Bistec", (pos_x, pos_y))
            elif obj.eskatana():
                material = obj.material
                tipo_katana = "madera" if material.esMadera() else "metal" if material.esMetal() else "diamante"
                self.mochila[str(obj)] = ("katana", tipo_katana, (pos_x, pos_y))
            elif obj.esEscudo():
                self.mochila[str(obj)] = ("Escudo", (pos_x, pos_y))
            
            pos_x += 70


    def visualObjeto(self,obj):
        if obj.esBistec():
            self.visualBistec(obj)
        if obj.eskatana():
            self.visualkatana(obj)
        if obj.esEscudo():
            self.visualEscudo(obj)

    def visitarEscudo(self,escudo):
        escudo.agregarObservadorPosicion(self)
        self.visualEscudo(escudo)

    def visitarBomba(self,bomba):
        bomba.agregarObservadoresActiva(self)
        self.visualBomba(bomba)

    def visitarBistec(self,Bistec):
        Bistec.agregarObservadorPosicion(self)
        if Bistec.padre.esmochila():
            self.visualBistec(Bistec)

    def visitarkatana(self,katana):
        katana.agregarObservadorPosicion(self)
        self.visualkatana(katana)
    
    def visualkatana(self, katana):
        self.katanasP[str(katana)] = (-100, -100)
        if katana.padre.esHabitacion():
            punto_x, punto_y = katana.padre.getPunto()
            extent_x = katana.padre.getExtent()[0]
            
            if katana.material.esMadera():
                pos_x = punto_x + 20
                pos_y = punto_y + extent_x - 100
                material = "madera"
            elif katana.material.esMetal():
                pos_x = punto_x + 120
                pos_y = punto_y + extent_x - 100
                material = "metal"
            elif katana.material.esDiamante():
                pos_x = punto_x + 220
                pos_y = punto_y + extent_x - 100
                material = "diamante"
            self.katanasP[str(katana)] = (material, (pos_x, pos_y))

    def visualEscudo(self, escudo):
        self.escudosP[str(escudo)] = (-100, -100)
        if escudo.padre.esHabitacion():
            punto_x, punto_y = escudo.padre.getPunto()
            extent_x = escudo.padre.getExtent()[0]
            
            pos_x = punto_x + 40
            pos_y = punto_y + extent_x - 300
            
            self.escudosP[str(escudo)] = (pos_x, pos_y)

    def visualBomba(self, bomba):
        self.bombasP[str(bomba)] = ("", (-100, -100))
        contenedor = bomba.padre
        extent_x = contenedor.getExtent()[0]
        punto_x, punto_y = contenedor.getPunto()
        
        pos_x = punto_x + extent_x - 200
        pos_y = punto_y + 100
        
        estado = "Activa" if bomba.activa else "Inactiva"
        self.bombasP[str(bomba)] = (estado, (pos_x, pos_y))


    def visitarPared(self,pared):
        pass # Son dibujadas junto al contenedor rectangular

    def visitargate(self,gate):
        if gate.lado1.esHabitacion() and gate.lado2.esHabitacion():
            gate.suscribirAbierto(self)
            self.visualgate(gate)

    def visitarTunel(self,tunel):
        pass#No se drawá, solo será jugado por consola.

    def drawContenedorRectangular(self, forma, escala):
        punto_x, punto_y = forma.punto
        ancho = forma.extent[0] / escala
        alto = forma.extent[1] / escala
        
        rectangulo = (punto_x, punto_y, ancho, alto)
        pygame.draw.rect(self.capaLaberinto, (255, 0, 0), rectangulo, 4)
