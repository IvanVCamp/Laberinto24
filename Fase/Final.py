from Fase.Fase import Fase

class Final(Fase):
    
    def agregarPersonaje(self, ch, game):
        print("[¡!] El juego ya ha terminado. No puedes introducir más personajes [¡!]")

    def lanzarBichos(self,juego):
        print("[¡!] El juego ya ha terminado. No puedes introducir más antagonistas [¡!]")
        
    def esFinal(self):
        return True
    