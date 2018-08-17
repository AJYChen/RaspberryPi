#!usr/bin/python3.5

from tkinter import *

def createWindow(window):
     xf = Frame(window, relief=GROOVE, borderwidth=2);
     Label(xf, text = "這是LED控制區").pack(pady=10,padx = 100);
     Button(xf, text = "LED CLOSE").pack(side=LEFT, expand = YES, fill = X);
     Button(xf, text = "LED OPEN").pack(side=LEFT,expand = YES, fill = X);
     xf.pack(pady=10, padx = 10);


if __name__ == "__main__":
    root = Tk();
    root.title("new window");
    createWindow(root);
    root.mainloop();

