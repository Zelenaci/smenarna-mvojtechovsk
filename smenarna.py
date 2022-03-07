#!/usr/bin/env python3

from cgitb import text
from os.path import basename, splitext
import tkinter as tk

from setuptools import Command
import numpy

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
        self.v = tk.IntVar(self)
        self.title(self.name)
        self.lbl = tk.Label(self, text="Směnárna")
        self.lbl.pack()
        self.radioBtn1 = tk.Radiobutton( self, text="Nákup",variable=self.v, value=1)
        self.radioBtn1.pack()
        self.radioBtn2 = tk.Radiobutton( self, text="Prodej",variable=self.v, value=2)
        self.radioBtn2.pack()
        self.v.set(1)
        self.listBox = tk.Listbox(self)
        self.listBox.pack()
        self.listBox.bind("<ButtonRelease-1>", self.onClick)
        self.bind("<Escape>", self.quit)
        self.listBoxFill()
        self.lbl2 = tk.Label(self, text="Kurz")
        self.lbl2.pack()
        self.amount = tk.IntVar()
        self.price = tk.StringVar()
        self.vysledek = tk.IntVar()
        self.amountLbl= tk.Label(self, textvariable= self.amount) 
        self.amountLbl.pack()
        self.priceLbl= tk.Label(self, textvariable= self.price) 
        self.priceLbl.pack()  
        self.entry = tk.Entry(self) 
        self.entry.pack()
        self.vysledekLbl= tk.Label(self, textvariable= self.vysledek) 
        self.vysledekLbl.pack()
        self.btn = tk.Button(self, text="Quit", command=self.quit)
        self.btn.pack()
        self.bind("<ButtonRelease>", self.vypocetFce)
        


    def vypocetFce(self,event=None):  
        e= int(self.entry.get())
        a = int(self.amount.get())
        p = float(self.price.get().replace(",","."))
        self.vysledekVar = float(numpy.ceil(e*p/a))   
        self.vysledek.set(self.vysledekVar)
    

    def onClick(self, event):
        index = self.listBox.curselection()[0]
        f = open("listek.txt")
        self.lines = f.readlines()
        self.amountVar = self.lines[index].split()[1]
        self.amount.set(self.amountVar)
        if self.v.get() == 1: 
            self.priceVar = self.lines[index].split()[3] 
        else:
            self.priceVar = self.lines[index].split()[2] 
        self.price.set(self.priceVar)
      
  
        


    def quit(self, event=None):
        super().quit()


    def listBoxFill(self):
        f = open('listek.txt', 'r')
        slovnik = {}
        for line in f:
            self.listBox.insert(tk.END,line.split()[0])
            slovnik[line.split()[0]] = (line.split()[1:])
         
        


app = Application()
app.mainloop()