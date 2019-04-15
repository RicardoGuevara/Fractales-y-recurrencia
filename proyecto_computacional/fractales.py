
from threading import Thread
from tkinter import *
import logging
import time


# just to debug something ( -_-)
def generic_button_test():
    print("Boton presionado")


class Haferman_section:
    """generate a haferman area"""

    def __init__(self, color = "white"):
        self.color = color
        if (color == "white"):
            self.sons = [[0,0,0],[0,0,0],[0,0,0]]
        else:
            self.sons = [[1,0,1],[0,1,0],[1,0,1]]
        
    def draw_me(self, x0, y0, panel = Canvas(), w = "600"):
        for i in self.sons:
            for j in i:
                if (j == 0):
                    panel.create_rectangle(x0,y0,x0+w,y0+w,fill="black")
                else:
                    panel.create_rectangle(x0,y0,x0+w,y0+w,fill="white")
                




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
        #canvas.pack()
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
        self.area1 += wc*wc

    def fill_carpet2(self, cuad,n):
        w = cuad[2]-cuad[0]
        wc = w/3
        if (n != 0):
            self.fill_carpet2([cuad[0], cuad[1], cuad[0]+wc, cuad[1]+wc], n-1)
            #self.fill_carpet2([cuad[0]+wc, cuad[1], cuad[0]+wc*2, cuad[1]+wc], n-1)
            self.fill_carpet2([cuad[0]+wc*2, cuad[1], cuad[0]+w, cuad[1]+wc], n-1)
            #self.fill_carpet2([cuad[0], cuad[1]+wc, cuad[0]+wc, cuad[1]+wc*2], n-1)
            #self.fill_carpet2([cuad[0]+wc, cuad[1]+wc, cuad[0]+wc*2, cuad[1]+wc*2], n-1)
            #self.fill_carpet2([cuad[0]+wc*2, cuad[1]+wc, cuad[0]+w, cuad[1]+wc*2], n-1)
            self.fill_carpet2([cuad[0], cuad[1]+wc*2, cuad[0]+wc, cuad[1]+w], n-1)
            #self.fill_carpet2([cuad[0]+wc, cuad[1]+wc*2, cuad[0]+wc*2, cuad[1]+w], n-1)
            self.fill_carpet2([cuad[0]+wc*2, cuad[1]+wc*2, cuad[0]+w, cuad[1]+w], n-1)

        self.panel2.create_rectangle(cuad[0]+wc, cuad[1], cuad[0]+wc*2, cuad[1]+wc, fill="black")
        self.panel2.create_rectangle(cuad[0], cuad[1]+wc, cuad[0]+wc, cuad[1]+wc*2, fill="black")
        self.panel2.create_rectangle(cuad[0]+wc, cuad[1]+wc, cuad[2]-wc, cuad[3]-wc, fill="black")
        self.panel2.create_rectangle(cuad[0]+wc*2, cuad[1]+wc, cuad[0]+w, cuad[1]+wc*2, fill="black")
        self.panel2.create_rectangle(cuad[0]+wc, cuad[1]+wc*2, cuad[0]+wc*2, cuad[1]+w, fill="black")
        self.area2 += (wc*wc)*5

    def carpets(self):
        self.area1 = 0
        self.area2 = 0
        self.panel.create_rectangle(0, 0, 600, 600, fill="black")
        self.fill_carpet([0, 0, 600, 600],int(self.input_n.get())-1)
        self.panel2.create_rectangle(0, 0, 600, 600, fill="white")
        self.fill_carpet2([0, 0, 600, 600],int(self.input_n.get())-1)
        self.def1 = (self.area1*100)/(600*600)
        self.def2 = (self.area2*100)/(600*600)
        self.lb3 = self.addLabel("Sombreado:   "+str(self.def1)+" %",he_in=2,wd_in=80)
        self.lb4 = self.addLabel("Sombreado:   "+str(self.def2)+" %",he_in=2,wd_in=80)
        self.lb3.grid(row=3, column=0, columnspan=3, rowspan=1)
        self.lb4.grid(row=3, column=3, columnspan=3, rowspan=1)

    def startpage(self):
        self.root_window.title("Fractal - Sierspinski / Ricardo Guevara")
        self.root_window.geometry("1220x750")

        self.len_label = self.addLabel("# DE PASOS RECURSIVOS:",he_in=2,wd_in=30)
        self.lb1 = self.addLabel("Sierpínski Carpet",he_in=2,wd_in=80)
        self.lb2 = self.addLabel("Cantor Square Fractal",he_in=2,wd_in=80)
        self.lb3 = self.addLabel("Sombreado:   ",he_in=2,wd_in=80)
        self.lb4 = self.addLabel("Sombreado:   ",he_in=2,wd_in=80)
        self.input_n = self.addEntry()
        self.start_btn = self.addButton(wd_in = 20, he_in = 3, label_text="COMENZAR", function=self.carpets)
        self.panel = self.addCanvas(he_in=600, wd_in=600, bcg="black")
        self.panel2 = self.addCanvas(he_in=600, wd_in=600, bcg="white")

        self.len_label.grid(row=0, column=0, columnspan=2, rowspan=1)
        self.input_n.grid(row=0, column=1, columnspan=2, rowspan=1)
        self.start_btn.grid(row=0, column=2, columnspan=2, rowspan=1)
        self.lb1.grid(row=1, column=0, columnspan=3, rowspan=1)
        self.lb2.grid(row=1, column=3, columnspan=3, rowspan=1)
        self.panel.grid(row=2, column=0, columnspan=3, rowspan=1)
        self.panel2.grid(row=2, column=3, columnspan=3, rowspan=1)
        self.lb3.grid(row=3, column=0, columnspan=3, rowspan=1)
        self.lb4.grid(row=3, column=3, columnspan=3, rowspan=1)



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