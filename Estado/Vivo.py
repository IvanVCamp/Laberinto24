from Estado.Estado import Estado

class Vivo(Estado):
    __instancia = None

    def actua(self,unBicho):
        unBicho.puedeActuar()

    def enteEsAtacadoPor(self,victima,agresor):
        victima.puedeSerAtacadoPor(agresor)

    def estaVivo(self):
        return True
    
    def esVivo(self):
        return True
    
    def __str__(self):
        return "Lo contrario a muerto."