import tkinter as tk
import os
from interface import main_window
from database import init_db
from settings import load_api, config_path

# To do: create database configuration file to be used during second and later logins.
# It should be created on first login.

def first_start():
    for _ in range(50):
        if os.path.isfile(config_path) == False:
            os.makedirs(os.path.dirname(config_path), exist_ok=True)
            with open(config_path, "w") as f:
                f.write("")
        else:
            with open(config_path, "a+") as f:
                data = f.readline()
                if "False" not in data:
                    load_api()
                    init_db()
                    with open(config_path, "w") as f:
                        f.write("first_start"+"="+"False")
                break
                    

first_start()

if __name__ == "__main__":
    root = tk.Tk()
    main = main_window(root)
    title = root.title("Virus Total API Tool")
    main.pack(side="top", fill="both", expand=True)
    root.resizable(0, 0)
    root.mainloop()