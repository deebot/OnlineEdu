import tkinter as tk
from tkinter import ttk

class View(tk.Tk):
    def __init__(self,controller):
        super().__init__()
        self.controller=controller

    def main(self):
        print("In main of view")
        self.geometry("680x400")
        self.mainloop()



if __name__ == '__main__':
    pass