import re
from GuardarDatos import GuardarDatos

class Descomposicion:
    g=GuardarDatos()
    ident=""
    def descomponer(self,texto):
        
        state=0
        nombre=""
        lexema=""
        caracter=""
        seccion=""
        ident=""
        for i in texto:
            caracter=ord(i)
            
            if state==0:
                if caracter==61:
                    state=1
                else:
                    print("")   
            elif state==1:
                if caracter==39:
                    state=2  
                    
                else:
                    print("")          
            elif state==2:
                if caracter>=65 and caracter<= 90:
                    lexema+=i
                    state=3
                    print(i)
                 
                else:
                    print("")
                    
            elif state==3:
                if caracter>=97 and caracter<=122:
                    lexema+=i
                elif caracter==32:
                    
                    lexema+=i 
                    state=4
                     
                elif caracter==39:
                    print("")  
                    
                else:
                    state=4
                    print("")
                    
            elif state==4:
                if caracter>=65 and caracter<= 90:
                    lexema+=i
                    nombre=lexema
                    print(i)
                elif caracter==39:
                    print("")
                else:
                    state=5
                    lexema+=i
                    print("")   
            elif state==5:
                
                if caracter>=97 and caracter<=122:
                    lexema+=i
                    nombre=lexema
                elif caracter==39:
                    print("")  
                    state=6
                else:
                    
                    print("")
            elif state==6:
                if caracter==39:
                    state=7
                    
                else:
                    print("")   
            elif state==7:
                if caracter>=65 and caracter<=90 or caracter>=97 and caracter<=122:
                    seccion+=i
                    
                else:
                    
                    state=8
            elif state==8:
                if caracter==39:
                    state=9
                else:
                    print("")   
            elif state==9:
                if caracter==58:
                    state=10
                else:
                    print("")    
            elif state==10:
                if caracter==91:
                    state=11
                else:
                    print("") 
            elif state==11:
                if caracter==39:
                    state=12
                else:
                    print("")
            elif state==12:
                if caracter>=65 and caracter<=90 or caracter>=97 and caracter<=122:
                    ident+=i
                    print(i)
                    
                else:
                    
                    state=13 
            elif state==13:
                if caracter==39:
                    state=14
                else:
                    print("") 
            elif state==14:
                if caracter==59:
                    print("")
                else:
                    print("")                  
            else:
                print("")                       
        print(lexema)
        print("nombre del restuarante: "+nombre)
        print("Seccion-"+seccion+"-")
        print("Identificador-"+ident)

    
    def automata1(self, texto):
        nombrePrincipal=""
        state=0
        caracter=""
        caracter1=""
        lexema=""
        lexema2=""
        ident=[]
        state1=0
        lexema3=""
        seccion=[]
        #Obtener Sección
        for i in texto:
            caracter1=ord(i)
            if state1==0:
                if caracter1==61:
                    state1=1
                else:       
                    print("")
            elif state1==1:
                if caracter1>=65 and caracter1<=90 or caracter1>=97 and caracter1<=122 :
                    lexema2+=i
                    state1=2
                else:
                    print("")      
            elif state1==2:
                if caracter1!=39:
                    lexema2+=i
                    nombrePrincipal=lexema2
                    
                    print("")
                elif caracter1==39:
                    state1=3
                else:
                    state1=0
                    print("") 
           
            elif state1==3:
                if caracter1>=65 and caracter1<=90 or caracter1>=97 and caracter1<=122 or caracter1==95:
                    lexema3+=i
                    state1=4
                else:
                    print("") 
            elif state1==4:
                if caracter1!=39 and caracter1!=58:
                    if caracter1!=59:

                        lexema3+=i
                    
                else:
                    state1=5
                    print("")            
            elif state1==5:
                if i=="\n" :
                    lexema3=lexema3+";"
                    state1=3 
                    print("")
                else:
                    
                       
                    print("")   
                     
            else:
                print("")  
        # Obtener Id
        # 

        secc=""
        sec=""
        secc=lexema3.split(";")    
        print(secc)  
        ids=""
        #recorre la lista
        for j in secc:
            if re.search(r"[A-Z]",j):
                seccion.append(j)
                sec=j
                print(j)
            else:
                    print(j)
                    ids=j
            
            self.g.guardarDatos(sec,ids,"nombre","precio","descripcion")
        #self.g.imprimir()    
        #prints 
        print(seccion)                     
        print("Secciones "+lexema3+".")
        print("Nombre Principal"+nombrePrincipal)                    
        #Obtener ID
        '''for i in texto:
            caracter=ord(i)
            if state==0:
                if caracter==91:
                    state=1
                    
                else:
                    print("") 
            elif state==1:
                if caracter!=59:
                    lexema+=i
                elif caracter==32:
                    print()    
                else:
                    state=2
                    print("")  
            elif state==2:
                if caracter==59:
                    state=0
                    print("")
                else:
                    
                    print("")    
            else:
                print("")               
        print("identificcar:"+lexema)
        ident.append(lexema)
        print(ident)'''
        
    def automataIds(self,cadena):
        
        estado=0
        pos=0
        lexema=""
        longitud=len(cadena)
        caracter=""
        error=""

        while pos<longitud:
            caracter=ord(cadena[pos])
            if estado==0:
                if pos==longitud-1 and caracter>=97 and caracter<=122:
                    letra=chr(caracter)
                    lexema+=str(letra)
                    pos+=1
                    
                    #print("True")

                elif caracter>=97 and caracter<=122: 
                    letra=chr(caracter)
                    lexema+=str(letra)
                    pos+=1
                    
                    estado=1

                else:
                    
                   
                    error+=cadena[pos]
                    estado=2
            elif estado==1:
                if pos==(longitud-1):
                    #lexema+=cadena[pos]
                    pos+=1
                    #print("True")
                    
                elif (caracter==95) or (caracter>=97 and caracter<=122) or (caracter>=48 and caracter<=57): 
                    letra=chr(caracter)
                    lexema+=str(letra)
                    pos+=1  
                    
                else:
                    
                    
                    error+=cadena[pos]
                    estado=2
                    
               
            elif estado==2:
                if caracter==91 or caracter==32 or caracter>=33 and caracter<=47 :
                    estado=1
                    pos+=1
                else:
                    break
                       
            else:
                print("")  
        
        if lexema!="" :
            return lexema
            #print("-"+lexema+"-")
            
        #print(error)    
        # 
    #Automata para seccion
    #      
    def automataSeccion(self,texto):
        pos=0
        estado=0
        lexema=""
        caracter=""
        longitud=len(texto)
        error=""
        secciones=""
        while pos<longitud:
            caracter=ord(texto[pos])
            if estado==0:
                if caracter==39:
                    pos+=1
                    estado=1
                    
                else:
                    error+=texto[pos]
                    pos+=1
            elif estado==1:
                if caracter>=65 and caracter <=90 or caracter>=97 and caracter<=122  or caracter>=48 and caracter<=57:
                    lexema+=texto[pos]     
                    pos+=1
                  
                elif caracter==32:
                    pos+=1
                    
                    
                else:
                    error+=texto[pos]
                    estado=2
            elif estado==2:
                if caracter==58:
                    lexema+=texto[pos]
                    #secciones=lexema+":"
                    pos+=1
                else:
                    
                    
                    pos+=1
            elif caracter==3:
                if caracter!=58:
                    
                    pos+=1
                    
                else:
                    pos+=1          
            else:

                print("")    
        #print("-"+lexema+"--")
        
        return lexema                 


    def automaFd(self,texto):
   
       
        state=0
        pos=0
        buffer=""
        fin=len(texto)
        caracter=0
        error=""
        while pos<fin:
            caracter=ord(texto[pos])
            
            if state==0:
                
                if caracter==61:
                    
                    
                    pos+=1
                    state=1
                    #print("True")
                    
                else:
                    error=texto[pos]
                    pos+=1
                   
                    #print("error")
                    
            elif state==1 :

                if caracter==39:
                    
                    pos+=1
                    state=2
                    #print("TRUE")
                else:
                    error=texto[pos]
                    pos+=1
               
            elif state==2:
                
                if caracter>=65 and caracter <=90 or caracter>=97 and caracter<=122 or caracter==32 or caracter>=48 and caracter<=57:
                    
                    buffer+=texto[pos]
                    pos+=1
                    
                elif caracter==39:
                    pos+=1
                else:
                    error+=texto[pos]
                    break
            elif state==3:
                buffer+=texto[pos]
                pos+=0
                state=0
                

            else:

                print("")
         
        
        if buffer!="":
            #print("-"+buffer+"-")
            #nombre=buffer
            return buffer
        
#Prueba
    def automataSeccion1(self,texto):
        pos=0
        estado=0
        lexema=""
        caracter=""
        longitud=len(texto)
        error=""
        secciones=""
        while pos<longitud:
            caracter=ord(texto[pos])
            if estado==0:
                if caracter==39:
                    pos+=1
                    estado=8
                elif caracter==32:
                    pos+=1 
                else:
                    error+=texto[pos]
                    pos+=1
            elif estado==8:
                if caracter==32:
                    pos+=1
                    estado=1
                else:
                    pos+=1             
            elif estado==1:
                if caracter>=65 and caracter <=90 or caracter>=97 and caracter<=122:
                    lexema+=texto[pos]     
                    pos+=1
                  
                elif caracter==39:
                    pos+=1
                
                else:
                    error+=texto[pos]
                    estado=2
            elif estado==2:
                if caracter==32:
                    lexema+=texto[pos]
                    pos+=1
                     
                else:
                     
                    error+=texto[pos]  


            elif estado==3:
                if caracter>=65 and caracter <=90 or caracter>=97 and caracter<=122 or caracter>=48 and caracter<=57 and caracter==35:
                    lexema+=texto[pos]  
                    pos+=1
                  
                elif caracter==39:
                    pos+=1
                elif caracter==93:
                    pos+=1  
                elif caracter==32:
                    pos+=1      
                else:

                     estado=4

            elif estado==4:
            
                    #lexema+=texto[pos]
                    estado=0
                    #secciones=lexema+":"
                        
               
                    
                    
                    pos+=1
                
            else:

                print("")    
        #print("-"+lexema+"--")
        
        return lexema 
    
        

    #Obtener nombre
    def nombre(self,texto):
        end=len(texto)
        buffer=""
        caracter=""
        pos=0
        estado=0
        error=""
        while pos<end:
            caracter=ord(texto[pos])
            if estado==0:
                if caracter==91:
                    pos+=1
                    estado=1
                elif caracter==32:
                    pos+=1
                else:
                    error+=texto[pos]    
                    pos+=1
            elif estado==1:
                if caracter==39:
                    pos+=1
                    estado=2
                    
                else:
                    error+=texto[pos]
                    
                    pos+=1
            elif estado==2:
                if caracter!=39:

                    buffer+=texto[pos]
                    pos+=1
                    
                else:
                    estado=3
                    pos+=1
            elif estado==3:
                
                pos+=1        
            else:
                print("")                    
        #print("nombre"+buffer+".")
        if buffer!="":
            return buffer
        

    #obtener descripcion
    def descripcion(self,texto):
        end=len(texto)
        buffer=""
        caracter=""
        pos=0
        estado=0
        error=""
        while pos<end:
            caracter=ord(texto[pos])
            if estado==0:
                if caracter==91:
                    pos+=1
                    estado=8
                elif caracter==32:
                    pos+=1
                else:
                    error+=texto[pos]    
                    pos+=1
            elif estado==8:
                if caracter==59:
                    pos+=1
                    estado=9
                else:
                    error+=texto[pos]      
                    pos+=1   
            elif estado==9:
                if caracter==59:
                    pos+=1
                    estado=1
                else:
                    pos+=1               
            elif estado==1:
                if caracter==39:
                    pos+=1
                    estado=2
                    
                else:
                    error+=texto[pos]
                    
                    pos+=1
            elif estado==2:
                if caracter!=39:

                    buffer+=texto[pos]
                    pos+=1
                    
                else:
                    estado=3
                    pos+=1
            elif estado==3:
                if caracter!=93 and texto[pos]!="\n":
                    buffer+=texto[pos]
                    estado=0
                    pos+=1 
                else:
                    error+=texto[pos]
                    pos+=1           
            else:
                print("")                    
        #print("des-"+buffer+".")
        if buffer!="":
            return buffer
    
    #Precio
    def AutomaPrecio(self,texto):
        buffer=""
        caracter=""
        end=len(texto)
        pos=0
        estado=0
        error=""
        while pos<end:
            caracter=ord(texto[pos])
            if estado==0:
                if caracter==91:
                    pos+=1
                    estado=1
                elif caracter==32:
                    pos+=1    
                else:    
                    error+=texto[pos]
                    pos+=1
            elif estado==1:
                if caracter==59:
                    pos+=1
                    estado=8
                else:
                    pos+=1
            elif estado==8:
                if caracter==59:
                    pos+=1
                    estado=2
                else:
                    pos+=1     
            elif estado==2:
                if caracter>=48 and caracter<=57:
                    buffer+=texto[pos]
                    pos+=1
                    estado=3
                elif caracter==32:
                    pos+=1
                else:
                    error+=texto[pos]
                    pos+=1
            elif estado==3:
                if caracter>=48 and caracter<=57:
                    buffer+=texto[pos]
                    pos+=1
                elif caracter==46:
                    buffer+=texto[pos]
                    pos+=1
                    estado=4
                else:
                    pos+=1
                    estado=0
            elif estado==4:
                if caracter>=48 and caracter<=57:
                    buffer+=texto[pos]
                    estado=5
                    pos+=1
                elif caracter==32:
                    pos+=1
                elif caracter==59:
                    break    
                else:
                    error+=texto[pos]
                    pos+=1
            elif estado==5:
                if caracter>=48 and caracter<=57:
                    buffer+=texto[pos]
                    estado=6
                    pos+=1
                elif caracter==32:
                    pos+=1
                else:
                    error+=texto[pos]
                    pos+=1
            elif estado==6:
                pos+=1
                estado=0  

            else:
                print("")                 
        #print("numero:"+buffer+".")
        if buffer!="":
            return buffer

                        









    