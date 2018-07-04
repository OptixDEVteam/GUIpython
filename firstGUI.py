from tkinter import *
from tkinter import ttk
root = Tk()
button = ttk.Button(root, text = "Click Here!")
button.pack()
def callback():
    print("it works")
button.config(command = callback)
    
