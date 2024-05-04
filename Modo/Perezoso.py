from Modo.Modo import Modo
import time

class Perezoso(Modo):
    
    def atacar(self,unBicho):
        unBicho.atacar()
        unBicho.cambiarModo()
    
    def dormir(self):
        time.sleep(6)
    
    def esPerezoso(self):
        return True
    
    def __str__(self):
        return "¡An-da-luuuuu-ces, le-van-taaaoos!"