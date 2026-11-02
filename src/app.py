import tkinter as tk
from gui import Gui

class App(tk.Tk):
    def __init__(self, title: str):
        super().__init__()

        self.title(title)

        self.gui = Gui(self, title)
        self.gui.pack(padx=10, pady=10, expand=True)

        self.mainloop()
