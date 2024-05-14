from Command.Command import Comando


class Abrir(Comando):
    
    def ejecutar(self, obj):
        self.receiver.abrir(obj)
    
    def esAbrir(self):
        return True
    
    def __str__(self):
        return "Abrir"