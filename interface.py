import tkinter as tk
from database import insert_report, init_db, extract_report

# Here I extend Button and other classes of tkinter to define their properties.
# "dbutton" stands for default button.
class dbutton(tk.Button):
    def __init__(self, *args, **kwargs):
        tk.Button.__init__(self, *args, **kwargs)
        self["activebackground"] = "red"
        self["bg"] = "gray15"
        self["fg"] = "white"
        self["width"] = "20"
        self["height"] = "2"

# dlabel stand for default label.
class dlabel(tk.Label):
    def __init__(self, *args, **kwargs):
        tk.Label.__init__(self, *args, **kwargs)
        self["bg"] = "gray15"
        self["fg"] = "white"

# Here is a single page.
class page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self["bg"] = "gray15"
    def show(self):
        self.lift()

# Here are other pages.
class reports_page(page):
   def __init__(self, *args, **kwargs):
       page.__init__(self, *args, **kwargs)

       url_box = tk.Text(self, 
       fg="white", 
       bg="gray15",
       insertofftime=0,
       width=40,
       height=40,
       wrap="none",
       insertbackground="white",
       )

       result_box = tk.Text(self, 
       fg="white", 
       bg="gray15",
       insertofftime=0,
       width=40,
       height=40,
       wrap="none"
       )

       instruction = dlabel(self, 
       text="""Insert URL to get the report for into the left frame, then click the button. Skip protocol and WWW, use newline as separator.
Results shall be displayed in the second column. There is no URL limit other than defined by your API.
Double click on result to jump to VirusTotal web app for details.""",
       justify="left"
       )

       def get_urls():
          urls = url_box.get("1.0", "end-1c").split("\n")
          result_box.delete(1.0, tk.END)
          print(urls)
          for _ in urls:
              if _ == "" or " " in _:
                  pass
              else:
                  _ = "https://" + _
                  insert_report(_)
                  report = extract_report(_) + "\n"
                  result_box.insert(tk.END, str(report))


       b1_get_report = dbutton(self, 
       text="Get the report!",
       command=get_urls
       )

       instruction.pack(side="top",
       pady=15
       )

       b1_get_report.pack(side="bottom",
       padx=20,
       pady=20
       )

       url_box.pack(side="left", 
       padx=20
       )

       result_box.pack(side="right",
       padx=20
       )

class scans_page(page):
   def __init__(self, *args, **kwargs):
       page.__init__(self, *args, **kwargs)

       label = dlabel(self, 
       text='This feature will be available in v2.0.\nWhen it"s done.™')
       label.pack(side="top", fill="both", expand=True)

class history_page(page):
   def __init__(self, *args, **kwargs):
       page.__init__(self, *args, **kwargs)

class files_scan(page):
    def __init__(self, *args, **kwargs):
        page.__init__(self, *args, **kwargs)

        label = dlabel(self, 
        text='This feature will be available in v2.0.\nWhen it"s done.™')
        label.pack(side="top", fill="both", expand=True)

class config_page(page):
    def __init__(self, *args, **kwargs):
        page.__init__(self, *args, **kwargs)

        def open_warning_window():
            warning_window = tk.Tk()
            warning_window["bg"] = "gray15"
            warning_window.title("You absolute madman!")
            warning_window.geometry("400x180")
            dlabel(warning_window, text="""This action will erase the database (if it exists), and create a new one.
PROCEED WITH CAUTION. THINK ABOUT BACKING UP THE BASE.
Do you still want to do this?"""
            ).pack(padx=20, pady=25)

            def close_warning_window():
                warning_window.destroy()
            
            b1_no = dbutton(warning_window, text="No", command=close_warning_window)
            b2_yes = dbutton(warning_window, text="Yes", command=lambda:[init_db(), close_warning_window()])

            b1_no.pack(side="left", padx=30)
            b2_yes.pack(side="right", padx=30)

        b1_reset_database = dbutton(self, 
        text="Reset database",
        command=open_warning_window
        )

        b1_reset_database.grid(column=0, row=2,)

# Here is the main window (that includes navbar at the top).
class main_window(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = reports_page(self)
        p2 = scans_page(self)
        p3 = files_scan(self)
        p4 = history_page(self)
        p5 = config_page(self)

        buttonframe = tk.Frame(self)
        buttonframe["bg"] = "gray15"
        container = tk.Frame(self)
        container.config(height='800')
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p4.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p5.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1_get_report = dbutton(buttonframe, text="URL report", command=p1.lift)
        b2 = dbutton(buttonframe, text="URL scan", command=p2.lift)
        b3 = dbutton(buttonframe, text="File scan", command=p3.lift)
        b4 = dbutton(buttonframe, text="History", command=p4.lift)
        b5 = dbutton(buttonframe, text="Settings", command=p5.lift)

        b1_get_report.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")
        b4.pack(side="left")
        b5.pack(side="left")

        p1.show()
