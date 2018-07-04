import os
import os.path
import threading
import inspect
import time
from tkinter import *
from tkinter import ttk
root = Tk()
def saveF():
    completeName = os.path.join(input_path.get(), filename.get()+ "." + file_ending.get())         
    open(completeName, "w").write(text.get("1.0", "end"))
    print(" ")
    time.sleep(1.2)
    print("OPERATION COMPLETE")
    text.delete("1.0","end")
    filename.delete("0","end")
    file_ending.delete("0","end")
filenameL = ttk.Label(root, text = "Filename")
filename = ttk.Entry(root)
endingL = ttk.Label(root, text = "File Ending(leave off dot)")
file_ending = ttk.Entry(root)
pathL = ttk.Label(root, text = "File Path")
input_path = ttk.Entry(root)
text = Text(root, width = 50, height = 20, wrap = "word")
submit = ttk.Button(root, text = "Submit", command = saveF)
filenameL.pack()
filename.pack()
endingL.pack()
file_ending.pack()
pathL.pack()
input_path.pack()
text.pack()
submit.pack()
file_ending.insert(0,"txt")


Cpath = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
print(Cpath)
if input_path.get == "":
    input_path = Cpath

