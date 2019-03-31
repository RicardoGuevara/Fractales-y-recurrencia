# Ricardo G. Payán // Ecuaciones y fractales
from threading import Thread
from tkinter import *
import logging

def generic_button_test():
    print("Boton presionado")

class Aplication:
    """generate GUI"""

    def __init__(self):
        self.root_window = Tk()

    def addLabel(self, label_text, anchor_in=CENTER, he_in=20, wd_in=100, bcg="white"):
        Label(self.root_window, text=label_text, anchor=anchor_in, height=he_in, width=wd_in, bg=bcg).pack()

    def addButton(self, function=generic_button_test, label_text="ACTION", anchor_in=CENTER, he_in=20, wd_in=100,
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

    def startpage(self):
        self.root_window.title("prueba de ventanas / Ricardo Guevara")
        self.root_window.geometry("500x500")
        self.addLabel("Funciona",he_in=2,wd_in=100)
        self.addCanvas()
        self.addButton(wd_in=20,he_in=5)
        self.addButton(wd_in=50,he_in=5,label_text="Generar una entrada de texto",function=self.addEntry)




# Genera la interfaz de usuario
def gen_gui_loader():
    logging.debug("hilo de vtn lanzado")

    scwd = Aplication()
    scwd.startpage()
    scwd.generate()


# Brute code

# Establece un hilo paralelo para la ejecución de la interfaz de usuario
try:
    graph_sc = Thread(target=gen_gui_loader, name="sc_window_initializer")
    graph_sc.start()
except Exception:
    raise TypeError("Error en el hilo de vtn principal")
finally:
    print("principal_thread_end")



# FIN