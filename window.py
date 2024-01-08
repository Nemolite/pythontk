from tkinter import *
from tkinter import ttk
class Window:
    ''' Иницилизация '''
    def __init__(self, title="window", bg_color="white", width=500, height=500):
        self.window = Tk()
        self.window.title(title)
        self.window.configure(bg=bg_color)
        self.window.geometry(f"{width}x{height}")


    def display_db_table(self,table='таблицы'):
        self.window.title(f"Данные из {table}")
        self.window.mainloop()






