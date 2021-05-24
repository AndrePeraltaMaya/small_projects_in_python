import tkinter as tk
from tkinter.ttk import *
import math 

class Calculator():
    def __init__(self):
        self.root = tk.Tk()#Creamos nuestro objeto Tk
        self.root.geometry('413x390')#El tamano de la ventana
        self.root.config(background="#D9E4F1",bd=-10)#Nuestro color de fondo
        self.root.title("Calculadora")#Agregamos un titulo
        self.root.iconbitmap("files/calculator.ico")#Agregamos un icono a la ventana
        self.root.resizable(0,0)#Desabilita el boton de maximizar

        imagenFondo = tk.PhotoImage(file="files//fondo.png")#Fondo
        iblImagen = tk.Label(self.root,image=imagenFondo).place(x=0,y=0)


        #Menús despegables



        #Salidas en pantalla e historial de calculos 


        self.output = tk.Label(self.root, text="0")
        self.output.place(x=377 , y= 149)
        self.output.config(bg="#FEFEFF", fg="black", font=("tahoma",16))
        self.texto = tk.StringVar() #La variable que contendra todo el texto de salida
        self.texto.set('0')
        self.output.config(textvariable = self.texto)

        self.pre_output = tk.Label(self.root, text=" ")
        self.pre_output.place(x = 382 , y= 134)
        self.pre_output.config(bg="#FEFEFF", fg="black", font=("tahoma",8))
        self.texto_pre = tk.StringVar() 
        self.texto_pre.set('')        
        self.pre_output.config(textvariable = self.texto_pre)

        self.pre_2 = tk.Label(self.root, text=" ")
        self.pre_2.place(x=382 , y= 111)
        self.texto_pre_2 = tk.StringVar()
        self.texto_pre_2.set('')        
        self.pre_2.config(bg="#E7F0FB", fg="grey", font=("tahoma",8),textvariable = self.texto_pre_2)

        self.pre_3 = tk.Label(self.root, text=" ")
        self.pre_3.place(x=382 , y= 94)
        self.texto_pre_3 = tk.StringVar()
        self.texto_pre_3.set('')        
        self.pre_3.config(bg="#E7F0FB", fg="grey", font=("tahoma",8),textvariable = self.texto_pre_3)

        self.pre_4 = tk.Label(self.root, text=" ")
        self.pre_4.place(x=382 , y= 77)
        self.texto_pre_4 = tk.StringVar()
        self.texto_pre_4.set('')        
        self.pre_4.config(bg="#E7F0FB", fg="grey", font=("tahoma",8),textvariable = self.texto_pre_4)

        self.pre_5 = tk.Label(self.root, text=" ")
        self.pre_5.place(x=382 , y= 60)
        self.texto_pre_5 = tk.StringVar()
        self.texto_pre_5.set('')        
        self.pre_5.config(bg="#E7F0FB", fg="grey", font=("tahoma",8),textvariable = self.texto_pre_5)



        self.block = False #Cuando hay un error
        #Funciones de agregado y eliminado:

        def click_boton(valor):
            '''Hace que se agregen los numeros en el output'''
            self.ultimo_signo = False

            if self.block:
                return 0

            if valor == ".":
                if "." in self.texto.get():
                    return 0
                if self.texto.get() == "0":
                    self.texto.set("0.")
                    self.output.config(textvariable = self.texto)
                    self.output.place(x=377 - (len(self.texto.get())-1)*11, y= 149)
                    return 0

            if self.virtual_output: #Si la salida es virtual
                self.virtual_output = False
                self.texto.set(valor)
                self.output.place(x=377 - (len(self.texto.get())-1)*11, y= 149)
            else:
                if valor == "0" and self.texto.get() == "0":#Si el usuario pone 0 cuando sólo hay un cero
                    pass
                elif valor != "0" and self.texto.get() == "0":#Si pone otro número cuando hay un cero
                    self.texto.set(valor)
                    self.output.config(textvariable = self.texto)
                    self.output.place(x=377 - (len(self.texto.get())-1)*11, y= 149)
                else:#Si el número en el output es diferente a 0
                    self.texto.set(self.texto.get() + valor)
                    self.output.place(x=377 - (len(self.texto.get())-1)*11, y= 149)
                    self.output.config(textvariable = self.texto)
                self.ultimo_signo = False

                

        def borrarElemento():
            if self.block:
                return 0
            if self.virtual_output == False: #Si la salida es virtual no hace nada

                if len(self.texto.get()) == 1:#Si sólo queda un número que borrar
                    self.texto.set("0")
                else:#Si son más de uno
                    self.texto.set(self.texto.get()[:-1])
                self.output.place(x=377 - (len(self.texto.get())-1)*11, y= 149)
                self.output.config(textvariable = self.texto)

        def CE_function():#Borra el output
            self.texto.set("0")
            self.output.config(bg="#FEFEFF", fg="black", font=("tahoma",16),textvariable = self.texto)             
            self.output.place(x=377 , y= 149)

            self.virtual_output = False
            self.block = False #Desbloquear el error



        def C_function():#Borra el output y el pre texto
            self.texto.set("0")
            self.output.config(bg="#FEFEFF", fg="black", font=("tahoma",16),textvariable = self.texto)            
            self.output.place(x=377 , y= 149)

            self.texto_pre.set("")
            self.pre_output.config(bg="#FEFEFF", fg="black", font=("tahoma",8),textvariable = self.texto_pre)             
            self.pre_output.place(x = 382 , y= 134)

            self.ultimo_signo = False
            self.virtual_output = False
            self.block = False#Desbloquear el error

        #Funciones aritmeticas
        self.ultimo_signo = False #Para que no haya dos signos aritmeticos juntos, ejemplo : */ 
        self.virtual_output = False 
        

        def operacion(type_):
            if self.block:
                return 0
            if self.ultimo_signo :#Si el ultimo caracter en el pre es un signo lo cambia por el nuevo
                self.texto_pre.set(self.texto_pre.get()[:-2] + type_ + " ")

            else: #Si al final del pre hay un número
                self.texto_pre.set(self.texto_pre.get() + self.texto.get() + " " + type_ + " ") 
            self.pre_output.config(textvariable = self.texto_pre)             
            self.pre_output.place(x = 382 - (len(self.texto_pre.get())-1)*(11/2) , y= 134)

            self.virtual_output = True
            self.ultimo_signo = True

        def resultado():
            if self.block:
                return 0

            result = ""

            try:
                result = str(eval(self.texto_pre.get() + self.texto.get()))
            except Exception as e:
            
                self.texto.set('No se puede dividir entre cero')
                print(eval(self.texto_pre.get() + self.texto.get()))        
                self.output.config(bg="#FEFEFF", fg="black", font=("tahoma",12),textvariable = self.texto)
                self.output.place(x=377 - (len(self.texto.get())-1)*(8.25) , y= 149)
                self.block = True
                return 0

            if self.texto_pre_5.get() == "":
                self.texto_pre_5.set(self.texto_pre.get() + self.texto.get())
                self.pre_5.place(x=382 - (len(self.texto_pre_5.get())-1)*(11/2) , y= 60)
                self.pre_5.config(textvariable = self.texto_pre_5)

            elif self.texto_pre_4.get() == "":
                self.texto_pre_4.set(self.texto_pre.get()+ self.texto.get())
                self.pre_4.place(x=382 - (len(self.texto_pre_4.get())-1)*(11/2) , y= 77)
                self.pre_4.config(textvariable = self.texto_pre_4)
                
            elif self.texto_pre_3.get() == "":
                self.texto_pre_3.set(self.texto_pre.get()+ self.texto.get())
                self.pre_3.place(x=382 - (len(self.texto_pre_3.get())-1)*(11/2) , y= 94)
                self.pre_3.config(textvariable = self.texto_pre_3)  

            elif self.texto_pre_2.get() == "":
                self.texto_pre_2.set(self.texto_pre.get()+ self.texto.get())
                self.pre_2.place(x=382 - (len(self.texto_pre_2.get())-1)*(11/2) , y= 111)
                self.pre_2.config(textvariable = self.texto_pre_2)


            else:
                self.texto_pre_5.set(self.texto_pre_4.get())
                self.pre_5.place(x=382 - (len(self.texto_pre_5.get())-1)*(11/2) , y= 60)
                self.pre_5.config(textvariable = self.texto_pre_5)                

                self.texto_pre_4.set(self.texto_pre_3.get())
                self.pre_4.place(x=382 - (len(self.texto_pre_4.get())-1)*(11/2) , y= 77)
                self.pre_4.config(textvariable = self.texto_pre_4)

                self.texto_pre_3.set(self.texto_pre_3.get())
                self.pre_3.place(x=382 - (len(self.texto_pre_3.get())-1)*(11/2) , y= 94)
                self.pre_3.config(textvariable = self.texto_pre_3)

                self.texto_pre_2.set(self.texto_pre.get()+ self.texto.get())
                self.pre_2.place(x=382 - (len(self.texto_pre_2.get())-1)*(11/2) , y= 111)
                self.pre_2.config(textvariable = self.texto_pre_2)


            self.texto.set(result)
            self.output.config(textvariable = self.texto)             
            self.output.place(x=377 - (len(self.texto.get())-1)*(11), y= 149)

            self.texto_pre.set("")
            self.pre_output.config(textvariable = self.texto_pre)             
            self.pre_output.place(x = 382 , y= 134)

            self.ultimo_signo = False
            self.virtual_output = False


        def negate():
            '''Cambio de signo'''
            if  eval(self.texto.get()) == 0:
                pass
            elif eval(self.texto.get()) > 0:
                self.texto.set("-"+self.texto.get())
                self.output.place(x=377 - (len(self.texto.get())-2)*(11) -8, y= 149)


            else:
                self.texto.set(self.texto.get()[1:])
                self.output.place(x = 377 - (len(self.texto.get())-1)*(11), y= 149) 

            self.output.config(textvariable = self.texto)

        def raiz():
            if self.ultimo_signo == True:
                self.texto_pre.set(self.texto_pre.get() + " math.sqrt(" + self.texto.get() + ")" )

            else:

                text_list = self.texto_pre.get().split(" ")

                self.texto_pre.set(" ".join(text_list[:-1])  + " math.sqrt(" + self.texto.get() + ")"  )

            self.pre_output.config(textvariable = self.texto_pre)             
            self.pre_output.place(x = 382 - (len(self.texto_pre.get())-1)*(11/2), y= 134)

            self.ultimo_signo = False
            self.virtual_output = True
            self.texto.set(" ") 



            #Mostramo el resultado hasta ese punto


        def reciproco():
            self.texto_pre.set("(1/" + self.texto.get() + ")")
            self.pre_output.config(textvariable = self.texto_pre)             
            self.pre_output.place(x = 382 - (len(self.texto_pre.get())-1)*(11/2), y= 134)
            self.virtual_output = True
            self.texto.set(" ") 
                       




		#Botones

        imagenBotonMC = tk.PhotoImage(file="files//imagenBotonMC.png")#Fondo
        BotonMC = tk.Button(self.root,command=lambda: null,bd=0, image=imagenBotonMC,background="#8B9BAD")
        BotonMC.place(x=209,y=188)

        imagenBotonMR = tk.PhotoImage(file="files//imagenBotonMR.png")#Fondo
        BotonMR = tk.Button(self.root,command=lambda: null,bd=0, image=imagenBotonMR,background="#8B9BAD")
        BotonMR.place(x=248 , y= 188)

        imagenBotonMS = tk.PhotoImage(file="files//imagenBotonMS.png")#Fondo
        BotonMS = tk.Button(self.root,command=lambda: null,bd=0, image=imagenBotonMS,background="#8B9BAD")
        BotonMS.place(x=287 , y= 188)

        imagenBotonMp = tk.PhotoImage(file="files//imagenBotonMp.png")#Fondo
        BotonMp = tk.Button(self.root,command=lambda: null,bd=0, image=imagenBotonMp,background="#8B9BAD")
        BotonMp.place(x=326 , y= 188)

        imagenBotonMm = tk.PhotoImage(file="files//imagenBotonMm.png")#Fondo
        BotonMm = tk.Button(self.root,command=lambda: null,bd=0, image=imagenBotonMm,background="#8B9BAD")
        BotonMm.place(x=365 , y= 188)

        #Segunda fila

        imagenBotonNull = tk.PhotoImage(file="files//imagenBotonNull.png")#Fondo
        BotonNull = tk.Button(self.root,command=lambda: null,bd=0, image=imagenBotonNull,background="#8B9BAD")
        BotonNull.place(x=14 , y= 220)

        imagenBotonInv = tk.PhotoImage(file="files//imagenBotonInv.png")#Fondo
        BotonInv = tk.Button(self.root,command=lambda: null,bd=0, image=imagenBotonInv,background="#8B9BAD")
        BotonInv.place(x=53 , y= 220)

        imagenBotonLn = tk.PhotoImage(file="files//imagenBotonLn.png")#Fondo
        BotonLn = tk.Button(self.root,command=lambda: null,bd=0, image=imagenBotonLn,background="#8B9BAD")
        BotonLn.place(x=92 , y= 220)

        imagenBotonParA = tk.PhotoImage(file="files//imagenBotonParA.png")#Fondo
        BotonParA = tk.Button(self.root,command=lambda: null,bd=0, image=imagenBotonParA,background="#8B9BAD")
        BotonParA.place(x=131 , y= 220)

        imagenBotonParC = tk.PhotoImage(file="files//imagenBotonParC.png")#Fondo
        BotonParC = tk.Button(self.root,command=lambda: null,bd=0, image=imagenBotonParC,background="#8B9BAD")
        BotonParC.place(x=170 , y= 220)

        imagenBotonflecha = tk.PhotoImage(file="files//imagenBotonflecha.png")#Fondo
        Botonflecha = tk.Button(self.root,command=lambda: borrarElemento(),bd=0, image=imagenBotonflecha,background="#8B9BAD")
        Botonflecha.place(x=209 , y= 220)

        imagenBotonCE = tk.PhotoImage(file="files//imagenBotonCE.png")#Fondo
        BotonCE = tk.Button(self.root,command=lambda: CE_function(),bd=0, image=imagenBotonCE,background="#8B9BAD")
        BotonCE.place(x=248 , y= 220)

        imagenBotonC = tk.PhotoImage(file="files//imagenBotonC.png")#Fondo
        BotonC = tk.Button(self.root,command=lambda: C_function(),bd=0, image=imagenBotonC,background="#8B9BAD")
        BotonC.place(x=287 , y= 220)

        imagenBotonMasMenos = tk.PhotoImage(file="files//imagenBotonMasMenos.png")#Fondo
        BotonMasMenos = tk.Button(self.root,command=lambda: negate(),bd=0, image=imagenBotonMasMenos,background="#8B9BAD")
        BotonMasMenos.place(x=326 , y= 220)

        imagenBotonRaiz = tk.PhotoImage(file="files//imagenBotonRaiz.png")#Fondo
        BotonRaiz = tk.Button(self.root,command=lambda: raiz(),bd=0, image=imagenBotonRaiz,background="#8B9BAD")
        BotonRaiz.place(x=365 , y= 220)


        #Tercer renglon


        imagenBotonInt = tk.PhotoImage(file="files//imagenBotonInt.png")#Fondo
        BotonInt = tk.Button(self.root,command=lambda: null,bd=0, image=imagenBotonInt,background="#8B9BAD")
        BotonInt.place(x=14 , y= 252)


        imagenBotonSinh = tk.PhotoImage(file="files//imagenBotonSinh.png")#Fondo
        BotonSinh = tk.Button(self.root,command=lambda: null,bd=0, image=imagenBotonSinh,background="#8B9BAD")
        BotonSinh.place(x=53 , y= 252)

        imagenBotonSin = tk.PhotoImage(file="files//imagenBotonSin.png")#Fondo
        BotonSin = tk.Button(self.root,command=lambda: null,bd=0, image=imagenBotonSin,background="#8B9BAD")
        BotonSin.place(x=92 , y= 252)

        imagenBotonX2 = tk.PhotoImage(file="files//imagenBotonX2.png")#Fondo
        BotonX2 = tk.Button(self.root,command=lambda: null,bd=0, image=imagenBotonX2,background="#8B9BAD")
        BotonX2.place(x=131 , y= 252)

        imagenBotonExcla = tk.PhotoImage(file="files//imagenBotonn!.png")#Fondo
        BotonExcla = tk.Button(self.root,command=lambda: null,bd=0, image=imagenBotonExcla,background="#8B9BAD")
        BotonExcla.place(x=170 , y= 252)

        imagenBoton7 = tk.PhotoImage(file="files//imagenBoton7.png")#Fondo
        boton7 = tk.Button(self.root,command=lambda: click_boton("7"),bd=0, image=imagenBoton7,background="#8B9BAD")
        boton7.place(x=209 , y= 252)

        imagenBoton8 = tk.PhotoImage(file="files//imagenBoton8.png")#Fondo
        boton8 = tk.Button(self.root,command=lambda: click_boton("8"),bd=0, image=imagenBoton8,background="#8B9BAD")
        boton8.place(x=248 , y= 252)

        imagenBoton9 = tk.PhotoImage(file="files//imagenBoton9.png")#Fondo       
        boton9 = tk.Button(self.root,command=lambda: click_boton("9"),bd=0, image=imagenBoton9,background="#8B9BAD")
        boton9.place(x=287 , y= 252)

        imagenBotonDiv = tk.PhotoImage(file="files//imagenBotonDiv.png")#Fondo
        BotonDiv = tk.Button(self.root,command=lambda: operacion("/"),bd=0, image=imagenBotonDiv,background="#8B9BAD")
        BotonDiv.place(x=326 , y= 252)

        imagenBotonPorcen = tk.PhotoImage(file="files//imagenBotonPorcen.png")#Fondo
        BotonPorcen = tk.Button(self.root,command=lambda: null,bd=0, image=imagenBotonPorcen,background="#8B9BAD")
        BotonPorcen.place(x=365 , y= 252)

#cuarto

        imagenBotondms = tk.PhotoImage(file="files//imagenBotondms.png")#Fondo
        Botondms = tk.Button(self.root,command=lambda: null,bd=0, image=imagenBotondms,background="#8B9BAD")
        Botondms.place(x=14 , y= 284)

        imagenBotonCosh = tk.PhotoImage(file="files//imagenBotonCosh.png")#Fondo
        BotonCosh = tk.Button(self.root,command=lambda: null,bd=0, image=imagenBotonCosh,background="#8B9BAD")
        BotonCosh.place(x=53 , y= 284)

        imagenBotonCos = tk.PhotoImage(file="files//imagenBotonCos.png")#Fondo
        BotonCos = tk.Button(self.root,command=lambda: null,bd=0, image=imagenBotonCos,background="#8B9BAD")
        BotonCos.place(x=92 , y= 284)

        imagenBotonXY = tk.PhotoImage(file="files//imagenBotonXY.png")#Fondo
        BotonXY = tk.Button(self.root,command=lambda: null,bd=0, image=imagenBotonXY,background="#8B9BAD")
        BotonXY.place(x=131 , y= 284)

        imagenBotonyraizx = tk.PhotoImage(file="files//imagenBotonyraizx.png")#Fondo
        Botonyraizx = tk.Button(self.root,command=lambda: null,bd=0, image=imagenBotonyraizx,background="#8B9BAD")
        Botonyraizx.place(x=170 , y= 284)

        imagenBoton4 = tk.PhotoImage(file="files//imagenBoton4.png")#Fondo
        boton4 = tk.Button(self.root,command=lambda: click_boton("4"),bd=0, image=imagenBoton4,background="#8B9BAD")
        boton4.place(x=209 , y= 284)

        imagenBoton5 = tk.PhotoImage(file="files//imagenBoton5.png")#Fondo
        boton5 = tk.Button(self.root,command=lambda: click_boton("5"),bd=0, image=imagenBoton5,background="#8B9BAD")
        boton5.place(x=248 , y= 284)

        imagenBoton6 = tk.PhotoImage(file="files//imagenBoton6.png")#Fondo
        boton6 = tk.Button(self.root,command=lambda: click_boton("6"),bd=0, image=imagenBoton6,background="#8B9BAD")
        boton6.place(x=287 , y= 284)

        imagenBotonProducto = tk.PhotoImage(file="files//imagenBotonProducto.png")#Fondo
        BotonProducto = tk.Button(self.root,command=lambda: operacion("*"),bd=0, image=imagenBotonProducto,background="#8B9BAD")
        BotonProducto.place(x=326 , y= 284)

        imagenBoton1x = tk.PhotoImage(file="files//imagenBoton1x.png")#Fondo
        Boton1x = tk.Button(self.root,command=lambda: reciproco(),bd=0, image=imagenBoton1x,background="#8B9BAD")
        Boton1x.place(x=365 , y= 284)

#Quinto

        imagenBotonpi = tk.PhotoImage(file="files//imagenBotonpi.png")#Fondo
        Botonpi = tk.Button(self.root,command=lambda: click_boton("3.14159265"),bd=0, image=imagenBotonpi,background="#8B9BAD")
        Botonpi.place(x=14 , y= 316)

        imagenBotonTanh = tk.PhotoImage(file="files//imagenBotonTanh.png")#Fondo
        BotonTanh = tk.Button(self.root,command=lambda: null,bd=0, image=imagenBotonTanh,background="#8B9BAD")
        BotonTanh.place(x=53 , y= 316)

        imagenBotontan = tk.PhotoImage(file="files//imagenBotontan.png")#Fondo
        Botontan = tk.Button(self.root,command=lambda: null,bd=0, image=imagenBotontan,background="#8B9BAD")
        Botontan.place(x=92 , y= 316)

        imagenBotonx3 = tk.PhotoImage(file="files//imagenBotonx3.png")#Fondo
        Botonx3 = tk.Button(self.root,command=lambda: null,bd=0, image=imagenBotonx3,background="#8B9BAD")
        Botonx3.place(x=131 , y= 316)

        imagenBoton3raizx = tk.PhotoImage(file="files//imagenBoton3raizx.png")#Fondo
        Boton3raizx = tk.Button(self.root,command=lambda: null,bd=0, image=imagenBoton3raizx,background="#8B9BAD")
        Boton3raizx.place(x=170 , y= 316)

        imagenBoton1 = tk.PhotoImage(file="files//imagenBoton1.png")#Fondo
        boton1 = tk.Button(self.root,command=lambda: click_boton("1"),bd=0, image=imagenBoton1,background="#8B9BAD")
        boton1.place(x=209 , y= 316)

        imagenBoton2 = tk.PhotoImage(file="files//imagenBoton2.png")#Fondo
        boton2 = tk.Button(self.root,command=lambda: click_boton("2"),bd=0, image=imagenBoton2,background="#8B9BAD")
        boton2.place(x=248 , y= 316)

        imagenBoton3 = tk.PhotoImage(file="files//imagenBoton3.png")#Fondo
        boton3 = tk.Button(self.root,command=lambda: click_boton("3"),bd=0, image=imagenBoton3,background="#8B9BAD")
        boton3.place(x=287 , y= 316)


        imagenBotonResta = tk.PhotoImage(file="files//imagenBotonResta.png")#Fondo
        BotonResta = tk.Button(self.root,command=lambda: operacion("-"),bd=0, image=imagenBotonResta,background="#8B9BAD")
        BotonResta.place(x=326 , y= 316)

        imagenBotonIgual = tk.PhotoImage(file="files//imagenBotonIgual.png")#Fondo
        BotonIgual = tk.Button(self.root,command=lambda: resultado(),bd=0, image=imagenBotonIgual,background="#8B9BAD")
        BotonIgual.place(x=365 , y= 316)
        #sexto

        imagenBotonFE = tk.PhotoImage(file="files//imagenBotonFE.png")#Fondo
        BotonFE = tk.Button(self.root,command=lambda: null,bd=0, image=imagenBotonFE,background="#8B9BAD")
        BotonFE.place(x=14 , y= 348)

        imagenBotonEXP = tk.PhotoImage(file="files//imagenBotonEXP.png")#Fondo
        BotonEXP = tk.Button(self.root,command=lambda: null,bd=0, image=imagenBotonEXP,background="#8B9BAD")
        BotonEXP.place(x=53 , y= 348)

        imagenBotonMod = tk.PhotoImage(file="files//imagenBotonMod.png")#Fondo
        BotonMod = tk.Button(self.root,command=lambda: null,bd=0, image=imagenBotonMod,background="#8B9BAD")
        BotonMod.place(x=92 , y= 348)

        imagenBotonLog = tk.PhotoImage(file="files//imagenBotonLog.png")#Fondo
        BotonLog = tk.Button(self.root,command=lambda: null,bd=0, image=imagenBotonLog,background="#8B9BAD")
        BotonLog.place(x=131 , y= 348)

        imagenBoton10x = tk.PhotoImage(file="files//imagenBoton10x.png")#Fondo
        Boton10x = tk.Button(self.root,command=lambda: null,bd=0, image=imagenBoton10x,background="#8B9BAD")
        Boton10x.place(x=170 , y= 348)

        imagenBoton0 = tk.PhotoImage(file="files//imagenBoton0.png")#Fondo
        Boton0 = tk.Button(self.root,command=lambda: click_boton("0"),bd=0, image=imagenBoton0,background="#8B9BAD")
        Boton0.place(x=209 , y= 348)

        imagenBotonPunto = tk.PhotoImage(file="files//imagenBotonPunto.png")#Fondo
        BotonPunto = tk.Button(self.root,command=lambda: click_boton("."),bd=0, image=imagenBotonPunto,background="#8B9BAD")
        BotonPunto.place(x=287 , y= 348)

        imagenBotonSuma = tk.PhotoImage(file="files//imagenBotonSuma.png")#Fondo
        BotonSuma = tk.Button(self.root,command=lambda: operacion("+"),bd=0, image=imagenBotonSuma,background="#8B9BAD")
        BotonSuma.place(x=326 , y= 348)




        self.root.mainloop()

if __name__ == '__main__':
	root=Calculator()