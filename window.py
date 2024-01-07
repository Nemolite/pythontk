from tkinter import *
from tkinter import ttk
class Window:
    ''' Иницилизация '''
    def __init__(self):
        self.window = Tk()
        self.window.title("Мой проект")
        self.window.geometry("500x500")

    def show(self):
        btn = ttk.Button(text="Button")
        btn.pack()
        self.window.title("Мой проект2")
        self.window.mainloop()






