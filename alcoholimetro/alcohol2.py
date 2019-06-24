from tkinter import *
from tkinter import ttk

class Alcoholimetro(ttk.Frame):
    def __init__(self, parent, **kwargs):
        ttk.Frame.__init__(self, parent, height=kwargs["height"], width=kwargs["width"])
           
        

        self.redOFFpng = PhotoImage(file= "images/redOFF.png")
        self.labelRedOff = Label(self, image=self.redOFFpng)
        self.labelRedOff.place(x=380, y=140)

        self.greenOFFpng = PhotoImage(file= "images/greenOFF.png")
        self.labelGreenOff = Label(self, image=self.greenOFFpng)
        self.labelGreenOff.place(x=310, y=140)

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
        btn_calcular.place (y=58, x=330)

        btn_anyadir = ttk.Button(self, command=self.anyadir, text= "Añadir")
        btn_anyadir.place (y=25, x=330)
        
        ##self.bebidas.get = contadorbebida
        
        self.grados = StringVar()
        self.horas = StringVar()

        ###self.volumen.get =volumenA

        
    def anyadir(self):
        print("añadiendo otra bebida")

    ##def calcular(self):
    ##    print("calculando el grado de alcoholemia")


    def calcular(volumen, graduacion):

        gramos = (self.volumen_entry.get() * self.grados_entry.get) * 0.8 / 100
        print (gramos)
        ai= (gramos/10)*3
        return ai
    print (calcular)
    
    def gramosAlcohol(volumenA, graduacionA):
        graduacionA = self.grados_entry(get)
        volumenA = self.volumen_entry.get()
        gramos = (self.volumen * self.grados) * 0.8 / 100
        ai= (gramos/10)*3
        return ai
    print (gramosAlcohol)
    ##self.alcoReal= gramosAlcohol(señf.volumen_entry, self.grados_entry) - 0.15 * self.horas_entry

    
##gramosAlcohol(1000, 12)

##print ("Llevas {} gramos de Alcohol en sangre".format(gramosAlcohol(1000, 12)))


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