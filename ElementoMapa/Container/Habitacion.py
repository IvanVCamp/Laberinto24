from ElementoMapa.Container.Container import Container

class Habitacion(Container):

    def entrar(self, obj):
        obj.setPosicion(self)
        print(str(obj)," se encuentra ahora en ",self.ref)
    
    def aceptar(self, vst):
        print("Visitar habitación ", str(self.num))
        vst.visitarHabitacion(self)
        for ch in self.objChildren:
            ch.aceptar(vst)
        self.form.aceptar(vst)

    def esHabitacion(self):
        return True
    
    def __str__(self):
        info= "La habitación " + str(self.ref) +" donde tenemos que " + str(self.form) 
        
        if len(self.objChildren)>0:
            dt = info + "\n [DETALLE DE LOS HIJOS]:"
            for n in self.objChildren:
                dt = dt + "\n["+str(n)+"]"
        return dt