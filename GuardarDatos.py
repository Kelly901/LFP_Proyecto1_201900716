from Datos import Datos
class GuardarDatos:
    datos=[]

    def guardarDatos(self,id,seccion,identificador,nombre,precio,descripcion):
        self.datos.append(Datos(id,seccion,identificador,nombre,precio,descripcion))
        return True


    def imprimir(self):

        for d in self.datos:
            print(str(d.id)+d.seccion+" id: "+d.identificador+" "+d.nombre+" "+d.precio+" "+d.descripcion)    