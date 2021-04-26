import webbrowser
from GuardarDatos import GuardarDatos
from Archivo import Archivo
class generaHtml:

    def generar_archivo(self):
        titulo=""
        nombre=""
        cont=1
        fi=open('Menu.html','w')
        tituloP=""
        tituloP="<h1 id=\"Titulo\">"+Archivo.nompreP[0]+"</h1>"
        #print(Archivo.nombrePrinc)
        for i in Archivo.seccion:
            
            titulo+="<h1 id=\"Titulo\">"+i+"</h1>"
            for dato in GuardarDatos.datos:
                
                if i==dato.seccion:
                    precio=f"{float(dato.precio):.2f}"
                    titulo+="<h2 id=\"seccion\">"+str(cont)+". "+dato.nombre+"    Q."+precio+"</h2>"
                    titulo+="<h2 id=\"seccion\">"+dato.descripcion+"</h2>"
                #nombre+="<h2 id=\"seccion\">"+dato.nombre+"</h2>"
                    cont+=1
        cuerpo="""<!DOCTYPE html>
                <html lang="en">

                    <head>
                <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Reporte de Datos</title>
            <style>
            body {
            margin: 0;
            padding: 0;
            background: linear-gradient(45deg, black, #094d68, #065377, rgb(3, 88, 128), rgb(12, 12, 12));
            background-size: cover;
            font-family: sans-serif;
            height: 100vh;
            }
            </style>
            </head>

            <body>

            <style>
            #Titulo {
            color: aliceblue;
            text-align: center;
            font-variant-caps: petite-caps;
            text-transform: capitalize;
            font-size: 35pt;

            }
            #seccion{
            color: aliceblue;
            margin: 27pt;
            
            
            font-size: 28pt;

            }

            

          
            h3{
            color: rgb(144, 190, 233);
            margin: 33pt;
            
            font-size: 17pt;
            }
            </style>
            
            
            """+tituloP+"""
            """+titulo+"""
            
            """+nombre+"""
            <h3> </h3>
            </body>

            </html> """            

        fi.write(cuerpo)
        fi.close()
        webbrowser.open_new_tab('Menu.html')