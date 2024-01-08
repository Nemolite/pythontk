import tkinter
from tkinter import *
from tkinter import ttk
class Window:
    ''' Иницилизация '''
    def __init__(self, title="window", bg_color="white", width=500, height=500):
        self.window = Tk()
        self.window.title(title)
        self.window.configure(bg=bg_color)
        self.window.geometry(f"{width}x{height}")


    def display_db_table(self,arr_table,table='таблицы'):
        print(arr_table)
        self.window.title(f"Данные из {table}")
        self.table = ttk.Treeview()
        self.table['columns'] = [1,2,3]
        for row in arr_table:
            self.table.insert('',END,values=row)
        self.table.pack()
        self.window.mainloop()






