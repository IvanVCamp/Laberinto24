from Fase.Fase import Fase

class Final(Fase):
    
    def agregarPersonaje(self, ch, game):
        print("[¡!] El juego ya ha terminado. No puedo meter más personajes [¡!]")

    def lanzarBichos(self,juego):
        print("[¡!] El juego ya ha terminado. No puedo meter más antagonistas [¡!]")
        
    def esFinal(self):
        return True
    