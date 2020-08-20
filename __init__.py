import tkinter as tk
from interface import MainView

# And here an app is called.
if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    title = root.title("Virus Total API Tool")
    main.pack(side="top", fill="both", expand=True)
    root.mainloop()