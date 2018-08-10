from tkinter import *

if __name__ == "__main__":
    root = Tk();
    root.title("new window");
    Label(root, text = "your button here").pack(pady=10);
    Button(root, text = "He's a nice button").pack(side=LEFT);
    Button(root, text = "It's a bad Button").pack(side=LEFT);
    root.mainloop();
