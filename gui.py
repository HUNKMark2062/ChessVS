from tkinter import *
import os

root = Tk()
root.title("Simple Chess")
root.option_add("*Font", "Times 20")
root.geometry("640x480")

title = Label(root, text="Simple Chess", bg="blue", fg="black")
title.pack(fill=X, pady=40)

def _exit():
    os._exit(0)

game1 = Button(root, text="Play against Stockfish", width=20)
game2 = Button(root, text="Play online", width=20)
settings = Button(root, text="Settings", width=20)
exit = Button(root, text="Exit", command=_exit, width=20)

game1.pack(side=TOP, pady=20)
game2.pack(side=TOP, pady=20)
settings.pack(side=TOP, pady=20)
exit.pack(side=TOP, pady=20)

root.mainloop()
