from tkinter import *

if __name__ == "__main__":
    root = Tk()
    root.title("New Window")
    for item in [RAISED,SUNKEN,FLAT,SOLID,GROOVE,RIDGE]:
        f = Frame(root, borderwidth = 2, relief = item)
        Label(f, text = item, width = 10).pack(side = LEFT)
        f.pack(side = RIGHT, padx = 5, pady = 5)

    root.mainloop()
