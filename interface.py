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

# Here is the main window (that includes navbar at the top).
class MainWindow(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = reports_page(self)
        p2 = scans_page(self)
        p3 = files_scan(self)
        p4 = history_page(self)
        p5 = config_page(self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        container.config(height='800')
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p4.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p5.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = dbutton(buttonframe, text="URL report", command=p1.lift)
        b2 = dbutton(buttonframe, text="URL scan", command=p2.lift)
        b3 = dbutton(buttonframe, text="File scan", command=p3.lift)
        b4 = dbutton(buttonframe, text="Logs", command=p4.lift)
        b5 = dbutton(buttonframe, text="Settings", command=p5.lift)

        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")
        b4.pack(side="left")
        b5.pack(side="left")

        p1.show()
