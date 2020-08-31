import tkinter as tk
import os
from interface import main_window
from database import init_db
from settings import load_api, config_path

# To do: create database configuration file to be used during second and later logins.
# It should be created on first login.

def first_start():
    for _ in range(20):
        if os.path.isfile(config_path) == False:
            print("First time, huh? Just follow the instructions.")
            os.makedirs(os.path.dirname(config_path), exist_ok=True)
            with open(config_path, "w") as f:
                f.write("first_start"+"="+"False")
            print("I will now create database, load API into your system and uncheck first start. Wait...")
            load_api()
            init_db()
            print("Done. Have fun!")
        else:
            check = open(config_path, "r").readline()
            if "False" not in check:
                pass
            else:
                break

if __name__ == "__main__":
    first_start()
    root = tk.Tk()
    main = main_window(root)
    title = root.title("Virus Total API Tool")
    main.pack(side="top", fill="both", expand=True)
    root.resizable(0, 0)
    root.mainloop()