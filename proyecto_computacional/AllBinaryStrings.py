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
        self.strings00_01 = []
        self.strings00_11 = []
        self.strter00 = []
        self.strter22 = []
        self.cuatcreciente = []
        
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

    def binary_strings00_01(self,n,str_ant):
        if (n == 0):
            self.strings00_01.append(str_ant)
        else:
            if (str_ant == ""):
                self.binary_strings00_01(n-1,str_ant+"1")
            elif (str_ant[-1] != "0"):
                self.binary_strings00_01(n-1,str_ant+"1")
                self.binary_strings00_01(n-1,str_ant+"0")

    def binary_strings00_11(self,n,str_ant):
        if (n == 0):
            self.strings00_11.append(str_ant)
        else:
            if (str_ant == ""):
                self.binary_strings00_11(n-1,str_ant+"1")
                self.binary_strings00_11(n-1,str_ant+"0")
            elif (str_ant[-1] == "1"):
                self.binary_strings00_11(n-1,str_ant+"0")
            elif (str_ant[-1] == "0"):
                self.binary_strings00_11(n-1,str_ant+"1")

    def ternary_strings00(self,n,str_ant):
        if (n == 0):
            self.strter00.append(str_ant)
        else:
            if (str_ant == ""):
                self.ternary_strings00(n-1,str_ant+"0")
            else:
                if (str_ant[-1] != "0"):
                    self.ternary_strings00(n-1,str_ant+"0")
            self.ternary_strings00(n-1,str_ant+"1")
            self.ternary_strings00(n-1,str_ant+"2")

    def ternary_strings22(self,n,str_ant):
        if (n == 0):
            self.strter22.append(str_ant)
        else:
            if (str_ant == ""):
                self.ternary_strings22(n-1,str_ant+"2")
            else:
                if (str_ant[-1] != "2"):
                    self.ternary_strings22(n-1,str_ant+"2")
            self.ternary_strings22(n-1,str_ant+"1")
            self.ternary_strings22(n-1,str_ant+"0")
    
    def cuaternary_creciente(self,n,str_ant):
        if (n == 0):
            self.cuatcreciente.append(str_ant)
        else:
            if (str_ant == ""):
                    self.cuaternary_creciente(n-1,str_ant+"0")
                    self.cuaternary_creciente(n-1,str_ant+"1")
                    self.cuaternary_creciente(n-1,str_ant+"2")
            else:    
                if (str_ant[-1] != "3"):
                    self.cuaternary_creciente(n-1,str_ant+"2")
                if (str_ant[-1] != "2" and str_ant[-1] != "3"):
                    self.cuaternary_creciente(n-1,str_ant+"1")
                if (str_ant[-1] != "1" and str_ant[-1] != "2" and str_ant[-1] != "3"):
                    self.cuaternary_creciente(n-1,str_ant+"0")
            self.cuaternary_creciente(n-1,str_ant+"3")

    def get_binaries00(self,length):
        self.strings00 = []
        self.binary_strings00(length,"")
        return self.strings00

    def get_binaries01(self,length):
        self.strings01 = []
        self.binary_strings01(length,"")
        return self.strings01

    def get_binaries00_01(self,length):
        self.strings00_01 = []
        self.binary_strings00_01(length,"")
        return self.strings00_01

    def get_binaries00_11(self,length):
        self.strings00_11 = []
        self.binary_strings00_11(length,"")
        return self.strings00_11

    def get_ternaries00(self,length):
        self.strter00 = []
        self.ternary_strings00(length,"")
        return self.strter00

    def get_ternaries22(self,length):
        self.strter22 = []
        self.ternary_strings22(length,"")
        return self.strter22

    def get_cuatcrec(self,length):
        self.cuatcreciente = []
        self.cuaternary_creciente(length,"")
        return self.cuatcreciente

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

    def formatResults(self):
        self.recbi00 = self.addLabel("binarias sin 00:   "+str(self.bingen.strings00.__len__()),he_in=1,wd_in=50)
        self.recbi01 = self.addLabel("binarias sin 01:   "+str(self.bingen.strings01.__len__()),he_in=1,wd_in=50)
        self.recbi00_01 = self.addLabel("binarias sin 00 ni 01:   "+str(self.bingen.strings00_01.__len__()),he_in=1,wd_in=50)
        self.recbi00_11 = self.addLabel("binarias sin 00 ni 11:   "+str(self.bingen.strings00_11.__len__()),he_in=1,wd_in=50)
        self.recte00 = self.addLabel("ternarias sin 00:   "+str(self.bingen.strter00.__len__()),he_in=1,wd_in=50)
        self.recte22 = self.addLabel("ternarias sin 22:   "+str(self.bingen.strter22.__len__()),he_in=1,wd_in=50)
        self.reccuat = self.addLabel("cuaternarias crecientes:   "+str(self.bingen.cuatcreciente.__len__()),he_in=1,wd_in=50)

        self.recbi00.grid(row=6, column=1, columnspan=2,rowspan=1)
        self.recbi01.grid(row=7, column=1, columnspan=2,rowspan=1)
        self.recbi00_01.grid(row=8, column=1, columnspan=2,rowspan=1)
        self.recbi00_11.grid(row=9, column=1, columnspan=2,rowspan=1)
        self.recte00.grid(row=10, column=1, columnspan=2,rowspan=1)
        self.recte22.grid(row=11, column=1, columnspan=2,rowspan=1)
        self.reccuat.grid(row=12, column=1, columnspan=2,rowspan=1)


    def calc_binaries(self):

        self.list00.delete(0, END)
        elements = self.bingen.get_binaries00(int(self.input_n.get()))
        for x in elements:
            self.list00.insert (END,x)

        self.list01.delete(0, END)
        elements = self.bingen.get_binaries01(int(self.input_n.get()))
        for z in elements:
            self.list01.insert (END,z)

        self.list00_01.delete(0, END)
        elements = self.bingen.get_binaries00_01(int(self.input_n.get()))
        for z in elements:
            self.list00_01.insert (END,z)

        self.list00_11.delete(0, END)
        elements = self.bingen.get_binaries00_11(int(self.input_n.get()))
        for z in elements:
            self.list00_11.insert (END,z)

        self.lister00.delete(0, END)
        elements = self.bingen.get_ternaries00(int(self.input_n.get()))
        for z in elements:
            self.lister00.insert (END,z)

        self.lister22.delete(0, END)
        elements = self.bingen.get_ternaries22(int(self.input_n.get()))
        for z in elements:
            self.lister22.insert (END,z)

        self.cuatcreciente.delete(0, END)
        elements = self.bingen.get_cuatcrec(int(self.input_n.get()))
        for z in elements:
            self.cuatcreciente.insert (END,z)

        self.formatResults()

    def generate(self):
        self.root_window.mainloop()
        self.root_window.destroy()

    def startpage(self):
        self.bingen = BinGenerator()
        self.root_window.title("Proyecto computacional 2019 - 01 | cadenas binarias")
        self.root_window.geometry("700x750")
        self.addLabel("CADENAS BINARIAS",he_in=2,wd_in=100)
        self.len_label = self.addLabel("LONGITUD:",he_in=2,wd_in=30)
        self.separador = self.addLabel("",he_in=2,wd_in=100, bcg="BLUE")
        self.tt1 = self.addLabel("binarias sin 00:",he_in=2,wd_in=30)
        self.tt2 = self.addLabel("binarias sin 01:",he_in=2,wd_in=30)
        self.tt3 = self.addLabel("binarias sin 00 ni 01:",he_in=2,wd_in=30)
        self.tt4 = self.addLabel("binarias sin 00 ni 11:",he_in=2,wd_in=30)
        self.tt5 = self.addLabel("ternarias sin 00:",he_in=2,wd_in=30)
        self.tt6 = self.addLabel("ternarias sin 22:",he_in=2,wd_in=30)
        self.tt7 = self.addLabel("cuaternaria creciente:",he_in=2,wd_in=30)
        self.input_n = self.addEntry()
        self.start_btn = self.addButton(wd_in = 20, he_in = 3, label_text="COMENZAR", function=self.calc_binaries)
        self.list00 = Listbox(self.root_window)
        self.list01 = Listbox(self.root_window)
        self.list00_01 = Listbox(self.root_window)
        self.list00_11 = Listbox(self.root_window)
        self.lister00 = Listbox(self.root_window)
        self.lister22 = Listbox(self.root_window)
        self.cuatcreciente = Listbox(self.root_window)

        self.len_label.grid(row=0, column=0, columnspan=1, rowspan=1)
        self.input_n.grid(row=0, column=1, columnspan=1, rowspan=1)
        self.start_btn.grid(row=0, column=2, columnspan=1, rowspan=1)
        self.separador.grid(row=1, column=0, columnspan=3, rowspan=1)
        self.tt1.grid(row=2, column=0, columnspan=1)
        self.tt2.grid(row=2, column=1, columnspan=1)
        self.tt3.grid(row=2, column=2, columnspan=1)
        self.tt4.grid(row=4, column=0, columnspan=1)
        self.tt5.grid(row=4, column=1, columnspan=1)
        self.tt6.grid(row=4, column=2, columnspan=1)
        self.tt7.grid(row=6, column=0, columnspan=1)
        self.list00.grid(row=3, column=0, columnspan=1,rowspan=1)
        self.list01.grid(row=3, column=1, columnspan=1,rowspan=1)
        self.list00_01.grid(row=3, column=2, columnspan=1,rowspan=1)
        self.list00_11.grid(row=5, column=0, columnspan=1,rowspan=1)
        self.lister00.grid(row=5, column=1, columnspan=1,rowspan=1)
        self.lister22.grid(row=5, column=2, columnspan=1,rowspan=1)
        self.cuatcreciente.grid(row=7, column=0, columnspan=1,rowspan=7)

        self.formatResults()

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