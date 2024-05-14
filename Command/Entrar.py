from Command.Command import Comando


class Abrir(Comando):
    
    def ejecutar(self, obj):
        self.receiver.entrar(obj)
    
    def esEntrar(self):
        return True
    
    def __str__(self):
        return "¡Entrando!"