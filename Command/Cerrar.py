from Command.Command import Comando


class Abrir(Comando):
    
    def ejecutar(self, obj):
        self.receiver.close(obj)
    
    def esCerrar(self):
        return True
    
    def __str__(self):
        return "Ciérrese"