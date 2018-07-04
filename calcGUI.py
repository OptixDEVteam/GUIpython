from tkinter import *
from tkinter import ttk
import math
import time

root = Tk()
root.title("Calculator")
labelUser = ttk.Label(root)
symSense = StringVar()
num1 = StringVar()
num2 = StringVar()
evaluate = ttk.Button(root)
box1 = ttk.Entry(root)
box2 = ttk.Entry(root)
sym = ttk.Combobox(root)
goforward = ttk.Button(root)
answer = ttk.Label(root)
def calc():
    goforward.pack_forget()
    answer.pack_forget()
    symSense = StringVar()
    num1 = IntVar()
    num2 = IntVar()
    labelUser.config(text = "Calculator")
    labelUser.pack()
    box1.config(width = 30)
    sym.config(textvariable = symSense,value = ("*","/","+","-","exponent","sqrt"))
    box2.config(width = 30)
    box1.pack()
    sym.pack()
    box2.pack()
    evaluate.config(text = "Calculate", command = CalculateFinal)
    evaluate.pack()

def CalculateFinal():
    """
    box1.pack_forget()
    sym.pack_forget()
    box2.pack_forget()
    evaluate.pack_forget()
    """
    if sym.get() == "sqrt":
        answer.config(text = math.sqrt(float(box1.get())))
        answer.pack()
        answer.pack_forget()
        calc()
    elif sym.get() == "exponent":
        answer.config(text = int(box1.get())**int(box2.get()))
        answer.pack()
        answer.pack_forget()
        calc()
    elif sym.get() == "":
        sym.set("*")
    else:
        calcAssist = box1.get() + sym.get() + box2.get()
        answer.config(text = eval(calcAssist))
    answer.pack()
    goforward.config(text = "Continue", command = calc)
    goforward.pack()
calc()
