from graphviz import Digraph
from Archivo import Archivo
from GuardarDatos import GuardarDatos
class Grafica:
    
    def generar_grafica(self):
        
        g=Digraph(format="pdf")
        nombrePrinciapal=Archivo.nompreP[0]
        datos=""
        for i in Archivo.seccion:
            g.edge(nombrePrinciapal,i)
            for dato in GuardarDatos.datos:
                
                if i==dato.seccion:
                    precio=f"{float(dato.precio):.2f}"
                    datos=dato.nombre+" Q."+precio+"  "+dato.descripcion
                    
                    
                    g.edge(i,datos)

        g.render(view=True)

                    
 