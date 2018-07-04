from tkinter import *
import pickle
root = Tk()
root.title("pickle editor")
filename = Entry(root)
text = Text(root, wrap="word")
save = Button(root, text="Save")
open_ = Button(root, text="Open")
def openfile():
    pickle.load(open(filename.get(),"rb"))
    text.delete("1.0","end")
    text.insert("1.0",pickle.load(open(filename.get(),"rb")))
    print("file opened")
def savefile():
    filesave = list(text.get("1.0","end"))
    for i in range(0,len(filesave)):
        if filesave[i] == "\n":
            filesave.pop(i)
    filesave = "".join(filesave)
    pickle.dump(filesave,open(filename.get(),"wb"))
    text.delete("1.0","end")
    print("file saved")
save.config(command = savefile)
open_.config(command = openfile)
filename.pack()
text.pack()
save.pack()
open_.pack()
