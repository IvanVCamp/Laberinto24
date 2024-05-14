from Command.Command import Comando


class Abrir(Comando):
    
    def ejecutar(self, obj):
        self.receiver.usar(obj)
    
    def esUsar(self):
        return True
    
    def __str__(self):
        return "Utilícese"