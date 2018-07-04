# imports
import time
from tkinter import *
from tkinter import ttk
# objects
root = Tk()
rootP = Tk()
timer = []
title = Label(root, text = "Timer")
colon1 = Label(root, text = ":")
colon2 = Label(root, text = ":")
hours = Entry(root, width = 5)
minutes = Entry(root, width = 5)
seconds = Entry(root, width = 5)
startO = ttk.Button(rootP, text = "Start")
clearO = ttk.Button(rootP, text = "Clear")
hoursTi = Label(root)
minutesTi = Label(root)
secondsTi = Label(root)
# functions
def main():
    startO.config(command = start)
    clearO.config(command = clear)
    title.grid(row = 0, column = 2)
    hours.grid(row = 1, column = 0)
    colon1.grid(row = 1, column = 1)
    minutes.grid(row = 1, column = 2)
    colon2.grid(row = 1, column = 3)
    seconds.grid(row = 1, column = 4)
    startO.pack()
    clearO.pack()
def clear():
    delAll()
    main()
def start():
    if hours.get() == "":
        hours.insert(0, "0")
    if minutes.get() == "":
        minutes.insert(0, "0")
    if seconds.get() == "":
        seconds.insert(0, "0")
    timer = [int(hours.get()), int(minutes.get()), int(seconds.get())]
    delAll()
    hoursTi.grid(row = 0, column = 0)
    colon1.grid(row = 0, column = 1)
    minutesTi.grid(row = 0, column = 2)
    colon2.grid(row = 0, column = 3)
    secondsTi.grid(row = 0, column = 4)
    while timer[0] + timer[1] + timer[2] > 0:
        if timer[-3] > 0 and timer[-2] == 0 and timer[-1] == 0:
            timer[-1] = 59
            timer[-2] = 59
            timer[-3] -= 1
        elif timer[-2] > 0 and timer[-1] == 0:
            timer[-2] -= 1
            timer[-1] = 59
        else:
            timer[-1] -= 1
        print(timer)
        root.update()
        hoursTi.config(text = timer[-3])
        minutesTi.config(text = timer[-2])
        secondsTi.config(text = timer[-1])
        root.update()
        time.sleep(1)
        root.update()
    delAll()
    title = Label(root, text = "Time Done!", foreground = "red")
    title.grid(row = 0, column = 2)
def delAll():
    for child in root.winfo_children():
        child.grid_forget()
if __name__ == "__main__":
    main()
