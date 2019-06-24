from tkinter import *
from tkinter import ttk

class Alcoholimetro(ttk.Frame):
    def __init__(self, parent, **kwargs):
        ttk.Frame.__init__(self, parent, height=kwargs["height"], width=kwargs["width"])
           
        self.dicBebidas = {"Tequila" : 60, "Pisco" : 44, "Whisky" : 40, "Coñac" : 40}
        self.bebidaSeleccionada = StringVar()
        self.listaBebidas= []
        self.listaBebidas = self.dicBebidas.keys()
        self.bebidaSeleccionada.set(self.dicBebidas.keys(0) #Esto coloca "Cerveza por defecto en el OptionMenu"
        
        self.menuBebidas = OptionMenu(self, self.bebidaSeleccionada, *self.dicBebidas.keys())
        self.menuBebidas.config(width = 14, font =( "Arial, 10"))
        self.menuBebidas.place(x=120, y=45) #Posicion del menu

        self.redOFFpng = PhotoImage(file= "images/redOFF.png")
        self.labelRedOff = Label(self, image=self.redOFFpng)
        self.labelRedOff.place(x=380, y=140)

        self.greenOFFpng = PhotoImage(file= "images/greenOFF.png")
        self.labelGreenOff = Label(self, image=self.greenOFFpng)
        self.labelGreenOff.place(x=310, y=140)

        ##self.bebidas = StringVar()
        self.volumen = StringVar()
        self.grados = StringVar()
        self.horas = StringVar()

        bebidas_lbl = ttk.Label(self, text= "Bebidas:", width=11, anchor=W)
        bebidas_lbl.place(x=25, y=50)
        bebidas_lbl.config(font = ("Arial", 14))
        #self.bebidas_entry = ttk.Entry(self, width=30, textvariable=self.bebidas)
        #self.bebidas_entry.place(x=80, y=50)

        volumen_lbl = ttk.Label(self, text= "Volumen:", width=11, anchor=W)
        volumen_lbl.place(x=25, y=80)
        volumen_lbl.config(font = ("Arial", 14))
        self.volumen_entry = ttk.Entry(self, width=30, textvariable=self.volumen)
        self.volumen_entry.place(x=110, y=84)

        grados_lbl = ttk.Label(self, text= "Grados:", width=11, anchor=W)
        grados_lbl.place(x=25, y=110)
        grados_lbl.config(font = ("Arial", 14))
        self.grados_entry = ttk.Entry(self, width=30, textvariable=self.grados)
        self.grados_entry.place(x=110, y=114)

        horas_lbl = ttk.Label(self, text= "Horas:", width=11, anchor=W)
        horas_lbl.place(x=25, y=140)
        horas_lbl.config(font = ("Arial", 14))
        self.horas_entry = ttk.Entry(self, width=30, textvariable=self.horas)
        self.horas_entry.place(x=110, y=144)

        btn_calcular = ttk.Button(self, command=self.calcular, text= "Calcular")
        btn_calcular.place (y=58, x=330)
        
        


    def calcular(self):
        print("calculando el grado de alcoholemia")



class MainApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        ##self.configure(background="colorquequiera")
        self.title("Alcoholimetro")
        self.geometry("450x200")
        self.alcoholimetro = Alcoholimetro(self, bg="#F4FFFF", height=200, width=450, )
        self.alcoholimetro.place(x=0, y=0)
        self.configure(background= "#F5679e") #Esto es el color de fondo, pero no del tk.frame

    def start(self):
        self.mainloop()

if __name__ == "__main__":
    miAlcoholimetro = MainApp()
    miAlcoholimetro.start()