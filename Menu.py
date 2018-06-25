from tkinter import *

class Menu:
    def __init__(self):
        self.master = Tk()
        self.master.title("Othello: Menu")
        self.choices = {4,6,8,10,12,14,16}
        Label(self.master, text="Number of Rows").grid(row=0, column = 0)
        Label(self.master, text="Number of Columns").grid(row=1, column = 0)
        Button(self.master, text = "Submit", command = self.submit).grid(row = 3, column = 1)
        self.make_dropdowns()
        self.master.mainloop()

    def make_dropdowns(self):
        self.rowVar = IntVar(self.master)
        self.colVar = IntVar(self.master)
        self.rowVar.set(8)
        self.colVar.set(8)
        OptionMenu(self.master, self.rowVar, *self.choices).grid(row = 0, column = 1)
        OptionMenu(self.master, self.colVar, *self.choices).grid(row = 1, column = 1)
        
    def submit(self):
        self.master.destroy()
    
    def get_dimensions(self):
        return (self.rowVar.get(), self.colVar.get())
    