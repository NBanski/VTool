import tkinter as tk
from interface import main_window
# from settings import first_start

# And here an app is called.
if __name__ == "__main__":
    root = tk.Tk()
    main = main_window(root)
    title = root.title("Virus Total API Tool")
    main.pack(side="top", fill="both", expand=True)
    root.resizable(0, 0)
    root.mainloop()