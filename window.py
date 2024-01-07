from tkinter import *
from tkinter import ttk
class EmptyWindow:
    ''' Окно - > Заголовок, Цвет, Ширина, Высотра '''
    def __init__(self,title="window",bg_color="white", width=500,height=500 ):
        self.window = Tk()
        self.window.title = title
        self.window.configure(bg=bg_color)
        self.window.geometry(f"{width}x{height}")
        self.window.mainloop()



