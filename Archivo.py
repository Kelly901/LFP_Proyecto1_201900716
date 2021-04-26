from tkinter import filedialog as FileDialog
from Descoposicion import Descomposicion
from GuardarDatos import GuardarDatos
import re
descom=Descomposicion()
guardar=GuardarDatos()
class Archivo:
    litaIds=[]   
    seccion=[]
    nombrePrinc="" 
    nompreP=[]            
    def texto(self):
        fichero=FileDialog.askopenfilename(title="Abrir un fichero")
        fi=open(fichero,mode='r',encoding="utf-8")
        
        mensaje=fi.readlines()
        #Nombre principal
    
        #NOMBER
        nombre=[]
        nombreTemp=[]
        #Seccion
        listaTemp=[]
        
        #Seccion
        seccionTemp=[]
        #Decripcion
        temDescripcion=[]
        descripcion=[]
        #Precio
        precioTemp=[]
        precio=[]
        #IDS
        idTemp=[]
        ids=[]

        for i in mensaje:
            if i!="\n":
               
                #nombre.append(descom.automaFd(i))
                nombreTemp.append(descom.nombre(i))
                temDescripcion.append(descom.descripcion(i))
                #escom.automataSeccion1(i)
                listaTemp.append(descom.automataSeccion(i))
                #descom.AutomaPrecio(i)
                precioTemp.append(descom.AutomaPrecio(i))
                idTemp.append(descom.automataIds(i))
                self.nompreP.append(descom.automaFd(i))
        #print(nompreP)        
        #print(nombre[0])  
        # Nombre Principal
        self.nombrePrinc=self.nompreP[0]
        #print(self.nombrePrinc)
        #       
        #print(listaTemp) 
       
        #print("_________________")
        contador=[]
        cont=0
        for i in range(1,int(len(listaTemp))):
            if re.search(r':',listaTemp[i]):
                #print(str(cont)+listaTemp[i])
                self.seccion.append(listaTemp[i])
                print(cont)
                cont+=1
            else: 
                contador.append(cont-1)   
                #print(str(cont-1)+listaTemp[i])
       # print(contador)        
        #print("_______________________")
        #print(self.seccion)        
        #Este for es de descripcion
        for i in temDescripcion:
            if i!=None:
                descripcion.append(i)
        #Print de descripcion
        #print("____________________________")
        #print(descripcion)

        #Nombre 
        for i in nombreTemp:
            if i!=None:
                nombre.append(i)
        #print nombre
        #print("____________________")
        #print(nombre)

        #Precio
        for i in precioTemp:
            if i!=None:
                precio.append(i)
        #Print precio
        #print("___________________________")
        #print(precio)   
        #print("_______________")  

        for i in range(1,int(len(idTemp))):
            if idTemp[i]!=None:
                ids.append(idTemp[i])  
        #print(ids)
        #Guardar en un arreglo de objetos
        cont1=0
        for i in contador:

            guardar.guardarDatos(i,self.seccion[i],ids[cont1],nombre[cont1],precio[cont1],descripcion[cont1])
            cont1+=1
        guardar.imprimir()
        '''print(self.litaIds)

        listaIds1=[]
        for i in self.litaIds:
            if i!=None:
                print("..")
                listaIds1.append(i)
        print(listaIds1)        
        #print(mensaje)

        for i in mensaje:
            if i!="\n":
                descom.automataSeccion(i)'''
        #print("_____________________________")
        #print(mensaje)            

