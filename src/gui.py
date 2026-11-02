import tkinter as tk
from tkinter import ttk

class Gui(ttk.Frame):
    ICON = "📈"

    ENTRY_FIELD_CONFIGS = [
        ("RRP (incl. tax)", "$"),
        ("RRP (excl. tax)", "$"),
        ("Cost Price", "$"),
        ("Gross Profit", "$"),
        ("Gross Margin", "%"),
        ("Markup", "%")
    ]

    TITLE_FONT = ("Arial", 16, "bold")
    TITLE_ICON_FONT = ("Arial", 20, "bold")
    STANDARD_FONT = ("Arial", 11)
    
    def __init__(self, master, title: str, **kwargs):
        super().__init__(master, **kwargs)

        self.define_widgets(title)
        self.position_widgets()


    def define_widgets(self, title: str):
        self.title_frame = ttk.Frame(self)
        self.title_label = ttk.Label(self.title_frame, font=Gui.TITLE_FONT, text=title)
        self.title_icon_label = ttk.Label(self.title_frame, font=Gui.TITLE_ICON_FONT, text=Gui.ICON)

        self.entry_fields_frame = ttk.LabelFrame(self, padding=(0, 10))
        self.entry_fields: list[EntryField] = []
        for config in Gui.ENTRY_FIELD_CONFIGS:
            entry_field = EntryField(self.entry_fields_frame, config[0], config[1])
            self.entry_fields.append(entry_field)

        self.clear_button = ttk.Button(self, text="Clear", command=self.clear_form, padding=10)


    def position_widgets(self):
        self.title_frame.grid(column=0, row=0, padx=10, pady=5)
        self.title_label.grid(column=0, row=0, pady=(0, 10))
        self.title_icon_label.grid(column=0, row=1)

        self.entry_fields_frame.grid(column=0, row=1, padx=10, pady=5)
        
        for i in range(len(self.entry_fields)):
            self.entry_fields[i].grid(column=0, row=i, sticky="e", padx=10, pady=5)

        self.clear_button.grid(column=0, row=2)


    def clear_form(self):
        for entry_field in self.entry_fields:
            entry_field.entry_var.set("")


class EntryField(ttk.Frame):
    def __init__(self, master, title: str, sign: str = "$", **kwargs):
        super().__init__(master, **kwargs)

        self.grid_columnconfigure(2, minsize=20) # Align columns

        self.define_widgets(title, sign)
        self.position_widgets()


    def define_widgets(self, title: str, sign: str):
        self.text_label = ttk.Label(self, font=Gui.STANDARD_FONT, text=title)

        self.entry_var = tk.StringVar(self)
        self.entry = ttk.Entry(self, textvariable=self.entry_var)

        self.sign_label = ttk.Label(self, font=Gui.STANDARD_FONT, text=sign)


    def position_widgets(self):
        self.text_label.grid(column=0, row=0, sticky="w")
        self.entry.grid(column=1, row=0, sticky="ew")
        self.sign_label.grid(column=2, row=0, sticky="w")
