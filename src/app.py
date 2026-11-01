import tkinter as tk

class App(tk.Tk):
    def __init__(self, title: str):
        super().__init__()
        self.title(title)


    def start(self):
        self.mainloop()
