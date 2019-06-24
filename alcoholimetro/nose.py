

from tkinter import *
from tkinter import ttk

class Alcoholimetro(ttk.Frame):
    def __init__(self, parent, **kwargs):
        ttk.Frame.__init__(self, parent, height=kwargs["height"], width=kwargs["width"])

                 
        self.redpng = PhotoImage(file= "images/redOFF.png")
        self.labelRed = Label(self, image=self.redpng)
        self.labelRed.place(x=380, y=140)

        self.greenpng = PhotoImage(file= "images/greenOFF.png")
        self.labelGreen = Label(self, image=self.greenpng)
        self.labelGreen.place(x=310, y=140)

        self.bebidas = StringVar()
        self.volumen = StringVar()
        self.grados = StringVar()
        self.horas = StringVar()

        bebidas_lbl = ttk.Label(self, text= "Bebidas:", width=11, anchor=W)
        bebidas_lbl.place(x=25, y=20)
        bebidas_lbl.config(font = ("Arial", 14))
        self.bebidas_entry = ttk.Entry(self, width=30, textvariable=self.bebidas)
        self.bebidas_entry.place(x=110, y=24)

        volumen_lbl = ttk.Label(self, text= "Volumen:", width=11, anchor=W)
        volumen_lbl.place(x=25, y=54)
        volumen_lbl.config(font = ("Arial", 14))
        self.volumen_entry = ttk.Entry(self, width=30, textvariable=self.volumen)
        self.volumen_entry.place(x=110, y=58)

        grados_lbl = ttk.Label(self, text= "Grados:", width=11, anchor=W)
        grados_lbl.place(x=25, y=88)
        grados_lbl.config(font = ("Arial", 14))
        self.grados_entry = ttk.Entry(self, width=30, textvariable=self.grados)
        self.grados_entry.place(x=110, y=92)
        
        horas_lbl = ttk.Label(self, text= "Horas:", width=11, anchor=W)
        horas_lbl.place(x=25, y=122)
        horas_lbl.config(font = ("Arial", 14))
        self.horas_entry = ttk.Entry(self, width=30, textvariable=self.horas)
        self.horas_entry.place(x=110, y=126)

        btn_calcular = ttk.Button(self, command=self.calcular, text= "Calcular")
        #btn_calcular = ttk.Button(self, command=self.calcular, text= "Calcular")
        btn_calcular.place (y=38, x=333)

        #btn_anyadir = ttk.Button(self, command=self.anyadir, text= "Añadir")
        #btn_anyadir.place (y=25, x=330)

    def calcular(self):
      
        self.volumen = self.volumen.get()
        self.volumen = int(self.volumen)
        self.graduacion = self.grados.get()
        self.graduacion = int(self.graduacion) 
        self.horas = self.horas.get()
        self.horas = int(self.horas)
        #gramos = (volumen x graduacion x 0.8)/100
        self.gramos = (self.volumen * self.graduacion) * 0.8 / 100 
        self.aR = StringVar()
        # ai = ube.0.3   ## aqui paso directamente los gramos a UBE
        ai= (self.gramos/10)*0.3
        aRprov = float(ai) - 0.15 * int(self.horas)
        bebidas = float(self.bebidas.get())
        self.aR = aRprov * bebidas
        self.aRround = round(self.aR, 2) 
        self.aRround_lbl  = ttk.Label(self, text = self.aRround, width=6, anchor=CENTER)
        self.aRround_lbl.place(x= 318, y= 85)
        self.aRround_lbl.config(font = ("Arial", 26))
        
        if self.aR >= 0.5:
            self.redpng = PhotoImage(file= "images/redON.png")
            self.labelRed = Label(self, image=self.redpng)
            self.labelRed.place(x=380, y=140)
            ####Intento poner un texto (TTK LABEL NO PUEDO CAMBIAR COLOR FUENTE)
            #noConduces_lbl = ttk.Label(self, text= "No puedes conducir:", width=20, anchor=W)
            #noConduces_lbl.place(x=50, y=150)
            #noConduces_lbl.config(font = ("Arial", 14))
            #noConduces_lbl.config(fg="red")

            ## Prueba de una label en vez de un ttk.Label
            noConduces_lbl = Label(self, text= "No puedes conducir", width=20, anchor=CENTER)
            noConduces_lbl.place(x=65, y=160)
            noConduces_lbl.config(font = ("Arial", 14))
            noConduces_lbl.config(fg="red")

        else:

            self.greenpng = PhotoImage(file= "images/greenON.png")
            self.labelGreen = Label(self, image=self.greenpng)
            self.labelGreen.place(x=310, y=140)

            conduces_lbl = Label(self, text= "Ok, puedes conducir", width=20, anchor=CENTER)
            conduces_lbl.place(x=65, y=160)
            conduces_lbl.config(font = ("Arial", 14))
            conduces_lbl.config(fg="green")


        print(round(self.aR, 3))
        return (self.aRround)
    
    


class MainApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        ##self.configure(background="colorquequiera")
        self.title("Alcoholimetro")
        self.geometry("450x200")
        self.alcoholimetro = Alcoholimetro(self, bg="#F4FFFF", height=200, width=450, )
        self.alcoholimetro.place(x=0, y=0)
        self.configure(background= "#F5679e") #Esto es el color de fondo, pero no del tk.frame. Por eso no va

    def start(self):
        self.mainloop()

if __name__ == "__main__":
    miAlcoholimetro = MainApp()
    miAlcoholimetro.start()