import tkinter as tk
import tkinter.scrolledtext as stxt
from database import insert_report, init_db, extract_report, search_database, query_scan_id, extract_report_by_id
from settings import change_api
import time

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

       url_box = stxt.ScrolledText(self, 
       fg="white", 
       bg="gray15",
       insertofftime=0,
       width=40,
       height=40,
       wrap="none",
       insertbackground="white",
       )

       result_box = stxt.ScrolledText(self, 
       fg="white", 
       bg="gray15",
       insertofftime=0,
       width=80,
       height=40,
       wrap="none",
       state="disabled"
       )

       instruction = dlabel(self, 
       text="""URLs to check goes into the left box. Result will appear in the right box.
Acceptable format is <domain name>.<extension>. Do not use protocol prefix.
URLs not found in the database will be copied to Domain scan page.""",
       justify="left"
       )

       def get_urls():
          urls = url_box.get("1.0", "end-1c").split("\n")
          result_box.configure(state="normal")
          result_box.delete(1.0, tk.END)
          for _ in urls:
              if _ == "" or " " in _:
                  pass
              else:
                  _ = "http://" + _
                  insert_report(_)
                  report = extract_report(_) + "\n"
                  result_box.insert(tk.END, str(report))
                  result_box.update()
          result_box.configure(state="disabled")


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

       url_box = stxt.ScrolledText(self, 
       fg="white", 
       bg="gray15",
       insertofftime=0,
       width=40,
       height=40,
       wrap="none",
       insertbackground="white",
       )

       result_box = stxt.ScrolledText(self, 
       fg="white", 
       bg="gray15",
       insertofftime=0,
       width=80,
       height=40,
       wrap="none",
       state="normal"
       )

       instruction = dlabel(self, 
       text="""URLs to check goes into the left box. Result will appear in the right box.
Acceptable format is <domain name>.<extension>. Do not use protocol prefix.
Be patient. Scanning takes one minute.""",
       justify="left"
       )

       def get_urls():
            urls = url_box.get("1.0", "end-1c").split("\n")
            result_box.configure(state="normal")
            result_box.delete(1.0, tk.END)
            id_list = []
            for _ in urls:
                if _ == "" or " " in _:
                    pass
                else:
                    _ = "http://" + _
                    resource_id = query_scan_id(_)
                    id_list.append(resource_id)
                    result_box.insert(tk.END, "Scan request sent for... " + str(_) + "\n")
                    result_box.update()
            result_box.insert(tk.END, "Now, wait a minute. Literally.")
            for _ in range(60):
                result_box.delete(1.0, tk.END)
                result_box.insert(tk.END, str(60 - _) + " seconds to go...")
                time.sleep(1)
                result_box.update()
            result_box.delete(1.0, tk.END)
            result_box.update()
            for _ in id_list:
                insert_report(_)
                report = extract_report_by_id(_)
                result_box.insert(tk.END, str(report) + "\n")
                result_box.update()
            result_box.configure(state="disabled")

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

class history_page(page):
   def __init__(self, *args, **kwargs):
       page.__init__(self, *args, **kwargs)

       instrucion = dlabel(self, 
       text='Insert domain to search for and click on "Seek & Destroy" button.')

       result_box = stxt.ScrolledText(self, 
       fg="white", 
       bg="gray15",
       insertofftime=0,
       width=100,
       height=40,
       wrap="none",
       insertbackground="white",
       state="disabled"
       )

       search_phrase = tk.Entry(self,
       width=64,
       bg="gray15",
       fg="white"
       ) 

       def seek_and_destroy():
           keyword = search_phrase.get()
           forbidden_dictionary = ["", "DROP", "*", "NULL", " ", "-", "'", '"']
           if keyword in forbidden_dictionary:
                result_box.configure(state="normal")
                result_box.delete(1.0, tk.END)
                result_box.insert(tk.END, "Really?")
                result_box.configure(state="disabled")
           else:
                result = search_database(keyword)
                result_box.configure(state="normal")
                result_box.delete(1.0, tk.END)
                for _ in result:
                    if _ in result_box.get(1.0, tk.END):
                        pass
                    else:
                        _ = _ + "\n"
                        result_box.configure(state="normal")
                        result_box.insert(tk.END, _)
                        result_box.configure(state="disabled")


       b1_search = dbutton(self,
       text="Seek & Destroy!",
       command=seek_and_destroy
       )

       instrucion.pack(side="top", pady=(10, 0))
       search_phrase.pack(side="top", pady=(10, 0))
       b1_search.pack(side="top", pady=(10, 0))
       result_box.pack(side="top", pady=(10, 0))


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
            warning_window.resizable(0, 0)
            dlabel(warning_window, text="""This action will erase the database (if it exists), and create a new one.
PROCEED WITH CAUTION. THINK ABOUT BACKING UP THE BASE.
Do you still want to do this?"""
            ).pack(padx=20, pady=25)

            def close_warning_window():
                warning_window.destroy()

            b1_no = dbutton(warning_window, text="No", command=close_warning_window)
            b2_yes = dbutton(warning_window, text="Yes", command=lambda:[init_db(), close_warning_window()])    

            b1_no.pack(side="right", padx=30)
            b2_yes.pack(side="left", padx=30)

        def open_change_api_window():
            change_window = tk.Tk()
            change_window["bg"] = "gray15"
            change_window.title("Change API Key")
            change_window.geometry("510x100")
            change_window.resizable(0, 0)

            def close_change_api_window():
                change_window.destroy()

            api_entry = tk.Entry(change_window, bg="gray15", fg="white", width=65, show="*") 
            api_entry.grid(column=1, row=0, padx=(10,0), pady=(20, 0))

            api_label = dlabel(change_window, text="Enter API Key:")
            api_label.grid(column=0, row=0, padx=(10,0), pady=(20, 0))

            api_change = dbutton(change_window, text="Change!", command=lambda:[change_api(api_entry.get()), close_change_api_window()])
            api_change.grid(column=1, row=1, pady=(10, 10))

        b1_reset_database = dbutton(self, 
        text="Reset database",
        command=open_warning_window
        )

        b2_change_api = dbutton(self,
        text="Change API Key",
        command=open_change_api_window
        )

        b3_placeholder = dbutton(self,
        text="Just a placeholder."
        )

        b4_placeholder = dbutton(self,
        text="Also just a placeholder."
        )

        b1_reset_database.grid(column=0, row=1, padx=(450, 300), pady=(250, 10))
        b2_change_api.grid(column=0, row=2, padx=(450, 300), pady=(0, 10))
        b3_placeholder.grid(column=0, row=3, padx=(450, 300), pady=(0, 10))
        b4_placeholder.grid(column=0, row=4, padx=(450, 300), pady=(0, 10))

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
        container.config(height='800', width='1000')
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
        b4 = dbutton(buttonframe, text="Search history", command=p4.lift)
        b5 = dbutton(buttonframe, text="Settings", command=p5.lift)

        b1_get_report.pack(side="left", padx=(125,10), pady=(10,0))
        b2.pack(side="left", padx=(0, 10), pady=(10,0))
        b3.pack(side="left", padx=(0, 10), pady=(10,0))
        b4.pack(side="left", padx=(0, 10), pady=(10,0))
        b5.pack(side="left", padx=(0,125), pady=(10,0))

        p1.show()