import tkinter as tk

# Here I extend Button and other classes of tkinter to define their properties.
# "dbutton" stands for default button.
class dbutton(tk.Button):
    def __init__(self, *args, **kwargs):
        tk.Button.__init__(self, *args, **kwargs)
        self["activebackground"] = "red"
        self["bg"] = "black"
        self["fg"] = "white"
        self["width"] = "20"
        self["height"] = "2"

# dlabel stand for default label.
class dlabel(tk.Label):
    def __init__(self, *args, **kwargs):
        tk.Label.__init__(self, *args, **kwargs)
        self["bg"] = "black"
        self["fg"] = "white"

# Here is a single page.
class page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self["bg"] = "black"
    def show(self):
        self.lift()

# Here are other pages.
class reports_page(page):
   def __init__(self, *args, **kwargs):
       page.__init__(self, *args, **kwargs)

class scans_page(page):
   def __init__(self, *args, **kwargs):
       page.__init__(self, *args, **kwargs)

class history_page(page):
   def __init__(self, *args, **kwargs):
       page.__init__(self, *args, **kwargs)

class files_scan(page):
    def __init__(self, *args, **kwargs):
        page.__init__(self, *args, **kwargs)
        label = dlabel(self, text='This feature will be available in v2.0.\nWhen it"s done.™')
        label.pack(side="top", fill="both", expand=True)

class config_page(page):
    def __init__(self, *args, **kwargs):
        page.__init__(self, *args, **kwargs)

