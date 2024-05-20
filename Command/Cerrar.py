from Command.Command import Command


class Abrir(Command):
    
    def ejecutar(self, obj):
        self.receiver.close(obj)
    
    def esCerrar(self): 
        return True
    
    def __str__(self):
        return "Un '¡Ciérrate, sésamo!' en toda regla."