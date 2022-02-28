#!/usr/bin/env python3

from os.path import basename, splitext
import tkinter as tk

# from tkinter import ttk


class About(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent, class_=parent.name)
        self.config()

        btn = tk.Button(self, text="Konec", command=self.close)
        btn.pack()

    def close(self):
        self.destroy()


class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "Směnárna"
    
    def __init__(self):
        super().__init__(className=self.name)
        v = tk.IntVar(self)
        self.title(self.name)
        self.lbl = tk.Label(self, text="Směnárna")
        self.lbl.pack()
        self.radioBtn1 = tk.Radiobutton( self, text="Nákup",variable=v, value=1)
        self.radioBtn1.pack()
        self.radioBtn2 = tk.Radiobutton( self, text="Prodej",variable=v, value=2)
        self.radioBtn2.pack()
        self.listBox = tk.Listbox(self)
        self.listBox.pack()
        self.bind("<Escape>", self.quit)
        self.btn = tk.Button(self, text="Quit", command=self.quit)
        self.btn.pack()
        self.listBoxFill()
        self.lbl2 = tk.Label(self, text="Kurz")
        self.lbl2.pack()
        listbox.bind( "<1>", None)
        listbox.bind( "<ButtonRelease-1>", klik)  # metoda se volá až po uvolnění myši
        



    def klik(param):
        souradnice="@"+str(param.x)+","+str(param.y)    
        print (listbox.get(souradnice))


    def quit(self, event=None):
        super().quit()


    def listBoxFill(self):
        f = open('listek.txt', 'r')
        slovnik = {}
        for line in f:
            self.listBox.insert(0,line.split()[0])
            slovnik[line.split()[0]] = (line.split()[1:])
        print(slovnik)    
        


app = Application()
app.mainloop()