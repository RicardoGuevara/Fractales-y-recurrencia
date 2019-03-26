# Ricardo G. Payán // Ecuaciones y fractales
from threading import Thread
from tkinter import *
import logging
import time


# just to debug something ( -_-)
def debugSomething():
    print("it founds well ( -_-)")


class Aplication:
    'generate GUI'

    def __init__(self):
        self.root_window = Tk()

    def addLabel(self, label_text, anchor_in=CENTER, he_in=20, wd_in=100, bcg="white"):
        Label(self.root_window, text=label_text, anchor=anchor_in, height=he_in, width=wd_in, bg=bcg).pack()

    def addButton(self, function=debugSomething, label_text="ACTION", anchor_in=CENTER, he_in=20, wd_in=100,
                  bcg="white"):
        Button(self.root_window, command=function, text=label_text, anchor=anchor_in, height=he_in, width=wd_in,
               bg=bcg).pack()

    def addEntry(self):
        Entry(self.root_window).pack()

    def addCanvas(self, he_in=400, wd_in=400, bcg="white"):
        canvas = Canvas(self.root_window, width=wd_in, height=he_in, bg=bcg)
        return canvas

    def generate(self):
        self.root_window.mainloop()
        self.root_window.destroy()

    # def startpage(self):
    # self.root_window.title("prueba de ventanas / Ricardo Guevara")
    # self.root_window.geometry("500x500")
    # self.addLabel("Funciona",he_in=2,wd_in=100)
    # self.addCanvas()
    # self.addButton(wd_in=20,he_in=5)
    # self.addButton(wd_in=50,he_in=5,label_text="Generar una entrada de texto",function=self.addEntry)


class Sierspinski_carpet(Aplication):
    """generate Sierspinski_carpet panel"""

    def fill_carpet(self, cuad,n):
        w = cuad[2]-cuad[0]
        wc = w/3
        if (n != 0):
            self.fill_carpet([cuad[0], cuad[1], cuad[0]+wc, cuad[1]+wc], n-1)
            self.fill_carpet([cuad[0]+wc, cuad[1], cuad[0]+wc*2, cuad[1]+wc], n-1)
            self.fill_carpet([cuad[0]+wc*2, cuad[1], cuad[0]+w, cuad[1]+wc], n-1)
            self.fill_carpet([cuad[0], cuad[1]+wc, cuad[0]+wc, cuad[1]+wc*2], n-1)
            #self.fill_carpet([cuad[0]+wc, cuad[1]+wc, cuad[0]+wc*2, cuad[1]+wc*2], n-1)
            self.fill_carpet([cuad[0]+wc*2, cuad[1]+wc, cuad[0]+w, cuad[1]+wc*2], n-1)
            self.fill_carpet([cuad[0], cuad[1]+wc*2, cuad[0]+wc, cuad[1]+w], n-1)
            self.fill_carpet([cuad[0]+wc, cuad[1]+wc*2, cuad[0]+wc*2, cuad[1]+w], n-1)
            self.fill_carpet([cuad[0]+wc*2, cuad[1]+wc*2, cuad[0]+w, cuad[1]+w], n-1)

        self.panel.create_rectangle(cuad[0]+wc, cuad[1]+wc, cuad[2]-wc, cuad[3]-wc, fill="red")
            
    def startpage(self):
        self.root_window.title("Fractal - Sierspinski / Ricardo Guevara")
        self.root_window.geometry("650x650")
        self.addLabel("Sierspinski carpet", he_in=2, wd_in=100)
        self.panel = self.addCanvas(he_in=600, wd_in=600, bcg="black")
        self.fill_carpet([0, 0, 600, 600],5)
        self.panel.pack()


class Haferman_carpet(Aplication):
    """generate Sierspinski_carpet panel"""

    def fill_carpet(self, cuad,n):
        w = cuad[2]-cuad[0]
        wc = w/3
        if (n != 0):
            self.fill_carpet([cuad[0], cuad[1], cuad[0]+wc, cuad[1]+wc], n-1)
            self.fill_carpet([cuad[0]+wc, cuad[1], cuad[0]+wc*2, cuad[1]+wc], n-1)
            self.fill_carpet([cuad[0]+wc*2, cuad[1], cuad[0]+w, cuad[1]+wc], n-1)
            self.fill_carpet([cuad[0], cuad[1]+wc, cuad[0]+wc, cuad[1]+wc*2], n-1)
            #self.fill_carpet([cuad[0]+wc, cuad[1]+wc, cuad[0]+wc*2, cuad[1]+wc*2], n-1)
            self.fill_carpet([cuad[0]+wc*2, cuad[1]+wc, cuad[0]+w, cuad[1]+wc*2], n-1)
            self.fill_carpet([cuad[0], cuad[1]+wc*2, cuad[0]+wc, cuad[1]+w], n-1)
            self.fill_carpet([cuad[0]+wc, cuad[1]+wc*2, cuad[0]+wc*2, cuad[1]+w], n-1)
            self.fill_carpet([cuad[0]+wc*2, cuad[1]+wc*2, cuad[0]+w, cuad[1]+w], n-1)

        self.panel.create_rectangle(cuad[0]+wc, cuad[1]+wc, cuad[2]-wc, cuad[3]-wc, fill="red")
            
    def startpage(self):
        self.root_window.title("Fractal - Sierspinski / Ricardo Guevara")
        self.root_window.geometry("650x650")
        self.addLabel("Sierspinski carpet", he_in=2, wd_in=100)
        self.panel = self.addCanvas(he_in=600, wd_in=600, bcg="black")
        self.fill_carpet([0, 0, 600, 600],5)
        self.panel.pack()



# Genera la interfaz de usuario
def sc_gui_loader():
    logging.debug("hilo de vtn lanzado")

    scwd = Sierspinski_carpet()
    scwd.startpage()
    scwd.generate()

def gen_gui_loader():
    logging.debug("hilo de vtn lanzado")

    scwd = Aplication()
    scwd.startpage()
    scwd.generate()


# Brute code

# Establece un hilo paralelo para la ejecución de la interfaz de usuario
try:
    graph_sc = Thread(target=sc_gui_loader, name="sc_window_initializer")
    graph_sc.start()
except Exception:
    raise TypeError("i seriously want to die")
finally:
    print("principal_thread_end")



# FIN