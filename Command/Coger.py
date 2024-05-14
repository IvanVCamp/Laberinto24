from Command.Command import Comando


class Abrir(Comando):
    
    def ejecutar(self, obj):
        self.receiver.coger(obj)
    
    def esCoger(self):
        return True
    
    def __str__(self):
        return "Coger"