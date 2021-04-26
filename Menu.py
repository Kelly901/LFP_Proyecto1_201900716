from Archivo import Archivo
from generaHtml import generaHtml
from Grafica import Grafica
ge=generaHtml()
archivo=Archivo()
grafica=Grafica()
class Menu:

    def menu(self):

        print("Proyecto 1 LFP")
        print("Sección A+ \n KElly Mischel Herrera Espino")
        print("Carnet 201900716")

        print("1. Cargar Menu")
        print("2. Cargar Orden")
        print("3. Generar Menu")
        print("4. Generar Factura")
        print("5. Generar Arbol")

        print("6. Salir")

        opcion=input("Ingrese su opcion-> ")
        self.opciones(opcion)
        
    def opciones(self,opcion):
        

        if opcion=="1":
            print("Cargar Menu")
            archivo.texto()
            print(" ")
            
            
            self.menu()
            
           
        elif opcion=="2":
            print("Cargar Orden")
            print(" ")
            self.menu()
        elif opcion=="3":
            print("Generar Menu")
            ge.generar_archivo()
            print(" ")
            self.menu()
        elif opcion=="4":
            print("Generar Factura")
            print(" ")
            self.menu()
        elif opcion=="5":
            print("Generar arbol")
            grafica.generar_grafica()
            print(" ")
            self.menu()
        elif opcion=="6":
            print("bye")
        else:
            print("La opcion "+opcion+" no existe")
            print("Escoja otra opcion->")   
            print(" ")
            self.menu()                        

m=Menu()
m.menu()