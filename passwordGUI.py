from tkinter import *
from tkinter import ttk
import pickle
import base64
import time
import math
import os.path

root = Tk()
root.title("Sign In")
text = Text(root)
savetext = Button(root)
def Eprint():
    print(E1.get())
def Save():
    pickle.dump(E1.get(), open( E2.get()+".p", "wb" ))
def Signup():
    pickle.dump( base64.b64encode(bytes(E1.get(), 'utf-8')), open( "Username.p", "wb" ) )
    pickle.dump( base64.b64encode(bytes(E2.get(), 'utf-8')), open( "Password.p", "wb" ) )
    pickle.dump( "1", open( "signedUp.p", "wb" ) )
    print("Signed Up")
def Signin():
    if pickle.load( open( "Username.p", "rb" ) ) == base64.b64encode(bytes(E1.get(), 'utf-8')) and pickle.load( open( "Password.p", "rb" ) ) == base64.b64encode(bytes(E2.get(), 'utf-8')):
        print("ACCESS GRANTED")
    else:
        print("ACCESS DENIED")
        time.sleep(1)
        exit()
def openfile():
    savetext.config(text = "Save", command = saveit)
    text.pack()
    text.set(pickle.load( open( E1.get()+".p", "rb" ) ))
    savetext.pack()
def saveit():
    pickle.dump( text.get("1.0", "end"), open( E1.get()+".p", "wb" ) )
labelPass = Label(root, text = "Entry 1")
E1 = ttk.Entry(root, width = 20)
labelUser = Label(root, text = "Entry 2")
E2 = ttk.Entry(root, width = 20)
submit = Button(root, text = "Print", command = Eprint)
save = Button(root, text = "Save", command = Save)
signupB = Button(root, text = "Sign Up", command = Signup)
signinB = Button(root, text = "Sign In", command = Signin)
openB = Button(root, text = "Open", command = openfile)

labelPass.pack()
E1.pack()
labelUser.pack()
E2.pack()
submit.pack()
save.pack()
openB.pack()



if pickle.load( open( "signedUp.p", "rb" ) ) == "1":
    signinB.pack()
else:
    signupB.pack()

    
