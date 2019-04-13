# Inicio
from threading import Thread
from tkinter import *
import logging

def generic_button_test():
    print("Boton presionado")

class BinGenerator:
    
    def __init__(self):
        self.strings00 = []
        self.strings01 = []
        
    def binary_strings00(self,n,str_ant):
        if (n == 0):
            self.strings00.append(str_ant)
        else:
            if (str_ant == ""):
                self.binary_strings00(n-1,str_ant+"0")
            else:
                if (str_ant[-1] != "0"):
                    self.binary_strings00(n-1,str_ant+"0")
            self.binary_strings00(n-1,str_ant+"1")

    def binary_strings01(self,n,str_ant):
        if (n == 0):
            self.strings01.append(str_ant)
        else:
            if (str_ant == ""):
                self.binary_strings01(n-1,str_ant+"1")
            else:
                if (str_ant[-1] != "0"):
                    self.binary_strings01(n-1,str_ant+"1")
            self.binary_strings01(n-1,str_ant+"0")


    def get_binaries00(self,length):
        self.strings00 = []
        self.binary_strings00(length,"")
        return self.strings00

    def get_binaries01(self,length):
        self.strings01 = []
        self.binary_strings01(length,"")
        return self.strings01

class Aplication:
    """generate GUI"""

    def __init__(self):
        self.root_window = Tk()

    def addLabel(self, label_text, anchor_in=CENTER, he_in=20, wd_in=100, bcg="white"):
        label = Label(self.root_window, text=label_text, anchor=anchor_in, height=he_in, width=wd_in, bg=bcg)
        #label.pack()
        return label

    def addButton(self, function=generic_button_test, label_text="ACTION", anchor_in=CENTER, he_in=10, wd_in=100,
                  bcg="white"):
        btn = Button(self.root_window, command=function, text=label_text, anchor=anchor_in, height=he_in, width=wd_in, bg=bcg)
        #btn.pack()
        return btn

    def addEntry(self):
        ent = Entry(self.root_window)
        #ent.pack()
        return ent

    def addCanvas(self, he_in=400, wd_in=400, bcg="white"):
        canvas = Canvas(self.root_window, width=wd_in, height=he_in, bg=bcg)
        canvas.pack()
        return canvas

    def addList(self, elements=["item1","item2"]):
        listbox = Listbox(self.root_window)
        for x in elements:
            listbox.append (x)
        listbox.pack()
        return listbox

    def calc_binaries(self):

        self.list00.delete(0, END)
        elements = BinGenerator().get_binaries00(int(self.input_n.get()))
        for x in elements:
            self.list00.insert (END,x)

        self.list01.delete(0, END)
        elements = BinGenerator().get_binaries01(int(self.input_n.get()))
        for z in elements:
            self.list01.insert (END,z)
        #self.pack()        

    def generate(self):
        self.root_window.mainloop()
        self.root_window.destroy()

    def startpage(self):
        self.root_window.title("Proyecto computacional 2019 - 01 | cadenas binarias")
        self.root_window.geometry("400x300")
        self.addLabel("CADENAS BINARIAS",he_in=2,wd_in=100)
        self.len_label = self.addLabel("Longitud:",he_in=2,wd_in=30)
        self.tt1 = self.addLabel("no contienen 00:",he_in=2,wd_in=30)
        self.tt2 = self.addLabel("no contienen 01:",he_in=2,wd_in=30)
        self.input_n = self.addEntry()
        self.start_btn = self.addButton(wd_in = 20, he_in = 3, label_text="COMENZAR", function=self.calc_binaries)
        self.list00 = Listbox(self.root_window)
        self.list01 = Listbox(self.root_window)


        self.len_label.grid(row=0, column=0, columnspan=1)
        self.input_n.grid(row=1, column=0, columnspan=1)
        self.start_btn.grid(row=0, column=1, columnspan=1, rowspan=2)
        self.tt1.grid(row=2, column=0, columnspan=1)
        self.tt2.grid(row=2, column=1, columnspan=1)
        self.list00.grid(row=3, column=0, columnspan=1,rowspan=1)
        self.list01.grid(row=3, column=1, columnspan=1,rowspan=1)


        #self.root_window.pack()


# Genera la interfaz de usuario
def gen_gui_loader():
    logging.debug("hilo de vtn lanzado")

    wd = Aplication()
    wd.startpage()
    wd.generate()


# Brute code

print(BinGenerator().get_binaries00(3))
print(BinGenerator().get_binaries01(3))


# Establece un hilo paralelo para la ejecución de la interfaz de usuario
try:
    graph_sc = Thread(target=gen_gui_loader, name="sc_window_initializer")
    graph_sc.start()
except Exception:
    raise TypeError("Error en el hilo de vtn principal")
finally:
    print("principal_thread_end")



# FIN