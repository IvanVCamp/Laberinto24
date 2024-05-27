from Estado.Estado import Estado
import sys
sys.setrecursionlimit(150000)
class Muerto(Estado):
    
    def actua(unBicho):
        print(str(unBicho),' no puede actuar en tanto que está muerto.')

    def enteEsAtacadoPor(self,atacado,atacante):
        print(str(atacante), " no puede atacar a ningún enemigo porque está muerto.")

    def estaVivo(self):
        return False
    
    def esMuerto(self):
        return True
    
    def __str__(self):
        return "Lo contrario a vivo."