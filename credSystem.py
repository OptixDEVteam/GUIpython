# imports
from tkinter import *
from tkinter import ttk
import time
import hashlib
import random

# make windows
TopLevel = Tk()
TopLevel.title("Bank")
notebook = ttk.Notebook(TopLevel)
notebook.pack()
output = Label(TopLevel, text = "Set Bank Code")
input_ = Entry(TopLevel, show="*")
output.pack()
input_.pack()
end = ttk.Button(TopLevel)


root = Frame(notebook)
add = Frame(notebook)
bank = Frame(notebook)
loan = Frame(notebook)
produce = Frame(notebook)
notebook.add(root, text = "Transfer")
notebook.add(add, text = "Add Account")
notebook.add(bank, text = "Bank")
notebook.add(loan, text = "Loan")
notebook.add(produce, text = "Store")

# vars
people = {"bank":999999999999999999999999999}
codes = {}
def setCode():
    codes["bank"] = hashlib.sha1(bytes(input_.get(), 'utf-8')).hexdigest()
    output.config(text = "")
    cont.pack_forget()
    input_.pack_forget()
items = {}
history = []
loans = []

# gui objects
cont = Button(TopLevel, text = "Go", command = setCode)
cont.pack()
"""root"""
fromL = Label(root)
fromB = ttk.Combobox(root)
toB = ttk.Combobox(root)
toL = Label(root)
fromCodeL = Label(root)
fromCode = Entry(root, show="*")
toCodeL = Label(root)
toCode = Label(root)
arrow1 = Label(root)
arrow2 = Label(root)
transfer = ttk.Button(root)
amountL = Label(root)
amount = Entry(root)
end = ttk.Button(root)

"""add"""
personL = Label(add)
person = Entry(add)
code = Entry(add, show="*")
codeL = Label(add)
addB = ttk.Button(add)
"""bank"""
bankOps = ttk.Notebook(bank)
withdraw = Frame(bankOps)
deposit = Frame(bankOps)
see = Frame(bankOps)

bankOps.add(withdraw,text = "Withdraw")
titleW = Label(withdraw)
codeLW = Label(withdraw)
codeW = Entry(withdraw, show="*")
accountW = ttk.Combobox(withdraw)
amountLW = Label(withdraw)
amountW = Entry(withdraw)
submitW = Button(withdraw)

bankOps.add(see,text = "See Account")
titleS = Label(see)
account = ttk.Combobox(see)
openAccount = ttk.Button(see)

bankOps.add(deposit,text = "Deposit")
titleD = Label(deposit)
accountD = ttk.Combobox(deposit)
bankCodeL = Label(deposit)
bankCode = Entry(deposit, show="*")
amountLD = Label(deposit)
amountD = Entry(deposit)
submitD = Button(deposit)

"""loans"""
loanAmount = Entry(loan)
loanAmountL = Label(loan)
loanReciever = ttk.Combobox(loan)
loanSubmit = Button(loan)
loanCode = Entry(loan, show="*")
loanCodeL = Label(loan)
loanPayBack = ttk.Combobox(loan)

"""produce"""
storeOps = ttk.Notebook(produce)
proCalc = Frame(storeOps)
store = Frame(storeOps)
addItems = Frame(storeOps)

storeOps.add(proCalc, text = "Plot Yield")
baseL = Label(proCalc)
base = Entry(proCalc)
produceGo = Button(proCalc)
boosterL = Label(proCalc)
booster = Entry(proCalc)

storeOps.add(store, text = "Store")
itemList = ttk.Combobox(store)
itemBuy = Button(store)
itemClear = Button(store)

storeOps.add(addItems, text = "Add Items")
addNameL = Label(addItems)
addName = Entry(addItems)
addPriceL = Label(addItems)
addPrice = Entry(addItems)
addSellerL = Label(addItems)
addSeller = ttk.Combobox(addItems)
addCodeL = Label(addItems)
addCode = Entry(addItems, show="*")
addDescriptionL = Label(addItems)
addDescription = Entry(addItems)
addSubmit = Button(addItems)

# functions
def pprint(string):
    output.config(text = string)
def AddPerson():
    people[person.get()] = 0
    codes[person.get()] = hashlib.sha1(bytes(code.get(), 'utf-8')).hexdigest()
    fromB.config(values = list(people.keys()))
    toB.config(values = list(people.keys()))
    accountW.config(values = list(people.keys()))
    addSeller.config(values = list(people.keys()))
    accountD.config(values = list(people.keys()))
    account.config(values = add(list(people.keys()), "all"))
    loanReciever.config(values = add(list(people.keys()), "bank", "remove"))
    history.append({"type":"new person","time":time.strftime("%I:%M %d/%m/%Y"), "person":person.get()})
    clearA()
def transferMoney():
    if int(amount.get()) < 1:
        raise ValueError("Number to low must be over zero")
    elif hashlib.sha1(bytes(fromCode.get(), 'utf-8')).hexdigest() == codes[fromB.get()]:
        if people[fromB.get()] - int(amount.get()) > -10:
            people[fromB.get()] -= int(amount.get())
            people[toB.get()] += int(amount.get())
            history.append({"type":"transfer","time":time.strftime("%I:%M %d/%m/%Y"), "from":fromB.get(), "to":toB.get(), "amount":amount.get()})
        else:
            raise ValueError("Account balance to low for transfer")
    else:
        raise ValueError("Security code incorrect")
    clearA()
def showAcount():
    if account.get() == "all":
        pprint(people)                  
    else:
        his = []
        for i in range(len(history)):
            try:
                if history[i]["to"] == account.get() or history[i]["from"] == account.get() or history[i]["person"] == account.get() or history[i]["reciever"] == account.get():
                    his.append(str(history[i]))
            except:
                1 == 1
        pprint("history:\n"+ "\n".join(his)+"\nbalance:"+str(people[account.get()]))
def clearA():
    fromB.set("")
    toB.set("")
    account.set("")
    code.delete(0, END)
    person.delete(0, END)
    amount.delete(0, END)
    fromCode.delete(0, END)
    loanCode.delete(0, END)
    loanAmount.delete(0, END)
    loanReciever.set("")
    bankCode.delete(0, END)
    amountD.delete(0, END)
    amountW.delete(0, END)
    codeW.delete(0, END)
    itemBuy.config(text = "Details", command = itemDetails)
    addName.delete(0, END)
    addPrice.delete(0, END)
    addSeller.set("")
    addCode.delete(0, END)
    addDescription.delete(0, END)
def add(list_, object_, type_="add"):
    if type_ == "add":
        add = list_
        add.append(object_)
        return add
    else:
        add = list_
        add.pop(add.index(object_))
        return add
def loanRecord():
    if loanPayBack.get() == "Get loan":
        if checkLoans(loanReciever.get()) == False:
            if hashlib.sha1(bytes(loanCode.get(), 'utf-8')).hexdigest() == codes[loanReciever.get()]:
                interest = random.randint(10,50)*10**-2
                loans.append({"reciever":loanReciever.get(), "amount":loanAmount.get(), "interest":interest, "moneyDue":round(int(loanAmount.get())*interest+int(loanAmount.get()), 0)})
                history.append({"type":"loan","reciever":loanReciever.get(), "amount":loanAmount.get(), "interest":interest, "moneyDue":int(loanAmount.get())*interest+int(loanAmount.get())})
                people[loanReciever.get()] += int(loanAmount.get())
                people["bank"] -= int(loanAmount.get())
                pprint("Loan Filed - Money Transfered")
            else:
                raise ValueError("Security code incorrect")
        else:
            pprint("Pay off previous loan before getting a new one")
            raise RuntimeError("Pay off previous loan before getting a new one")
    elif loanPayBack.get() == "Pay off loan":
        if people[loanReciever.get()] - int(loanAmount.get()) >= 10:
            if hashlib.sha1(bytes(loanCode.get(), 'utf-8')).hexdigest() == codes[loanReciever.get()]:
                index = 0
                for i in range(len(loans)):
                    if loans[i]["reciever"] == loanReciever.get():
                        index = i
                people[loanReciever.get()] -= int(loanAmount.get())
                loans[index]["moneyDue"] -= int(loanAmount.get())
                pprint("money due:"+ str(loans[index]["moneyDue"]))
                if loans[index]["moneyDue"] <= 0:
                    pprint("loan payed off!")
                    loans[index]["reciever"] = "loan payed"
            else:
                raise ValueError("Security code incorrect")
        else:
            pprint("You do not have sufficient money")
    elif loanPayBack.get() == "See loan":
        index = 0
        for i in range(len(loans)):
            if loans[i]["reciever"] == loanReciever.get():
                index = i
        pprint("loan:"+ str(loans[index]))
    else:
        raise ValueError("Loan management box does not contain an accepted value")
    clearA()
def checkLoans(person):
    status = 0
    status1 = False
    for i in loans:
        if i["reciever"] == person:
            status = 1
            status1 = True
    return status1
def calcProduce():
    plotVal = int(base.get())
    boosterVal = int(booster.get())
    rand = random.randint(1,2)
    while rand == 1:
        plotVal += 1
        rand = random.randint(1,2)
    rand = random.randint(1,2)
    while rand == 1:
        boosterVal += 1
        rand = random.randint(1,2)
    pprint("Plot Value:"+ str(plotVal), "\nBooster Value:", str(boosterVal))
    clearA()
def withdrawSubmit():
    if hashlib.sha1(bytes(codeW.get(), 'utf-8')).hexdigest() == codes[accountW.get()] and people[accountW.get()] - int(amountW.get()) > -10:
        pprint("transaction approved for $"+amountW.get()+"\nto be recieved by "+accountW.get())
        people[accountW.get()] -= int(amountW.get())
        history.append({"type":"withdraw","time":time.strftime("%I:%M %d/%m/%Y"), "from":accountW.get(), "amount":amountW.get()})
    else:
        raise ValueError("Security code incorrect")
    clearA()
def depositSubmit():
    if hashlib.sha1(bytes(bankCode.get(), 'utf-8')).hexdigest() == codes["bank"]:
        pprint("transaction approved for $"+amountD.get()+"\nadded to "+accountD.get())
        people[accountD.get()] += int(amountD.get())
        history.append({"type":"deposit","time":time.strftime("%I:%M %d/%m/%Y"), "to":accountD.get(), "amount":amountD.get()})
    else:
        raise ValueError("Security code incorrect")
    clearA()
def itemDetails():
    pprint("name: {}\nprice: {}\nseller: {}\ndescription: {}\n\n".format(itemList.get(), items[itemList.get()]["price"],items[itemList.get()]["seller"],items[itemList.get()]["description"]))
def newItem():
    if hashlib.sha1(bytes(addCode.get(), 'utf-8')).hexdigest() == codes[addSeller.get()]:
        items[addName.get()] = {"price":addPrice.get(), "seller":addSeller.get(), "description":addDescription.get()}
        pprint("Item Added")
    else:
        raise ValueError("Security code incorrect")
    itemList.config(values = list(items.keys()))
    clearA()
def log():
    if hashlib.sha1(bytes(input("Bank Code: "), 'utf-8')).hexdigest() == codes["bank"]:
        open("log "+time.strftime("%c"),"w").write(time.strftime("%c")+"\n\npeople:\n"+str(people)+"\n\nhashed codes:\n"+str(codes)+"\n\nstore items:\n"+str(items)+"\n\nloans:\n"+str(loans)+"\n\nhistory:\n"+str(history))
        print("saved")
        if input("shutdown (Y/N)? ").lower() == "y":
            exit()
    else:
        print("INCORRECT CODE")
# gui object attributes
"""TopLevel"""
notebook.pack()
end.config(text = "Close", command = log)
"""root"""
fromL.config(text = "From")
toL.config(text = "To")
fromB.config(values = list(people.keys()))
toB.config(values = list(people.keys()))
fromCodeL.config(text = "Securty Code")
toCode.config(text = "Not Needed", foreground = "green")
toCodeL.config(text = "Securty Code")
arrow1.config(text = "-->")
arrow2.config(text = "-->")
transfer.config(text = "Transfer", command = transferMoney)
amountL.config(text = "Amount")
"""add"""
addB.config(text = "Add", command = AddPerson)
personL.config(text = "Name")
codeL.config(text = "Security Code")
"""bank"""
titleW.config(text = "Withdraw")
titleS.config(text = "See Account")
titleD.config(text = "Deposit")
amountLW.config(text = "Amount")
amountLD.config(text = "Amount")
codeLW.config(text = "Security Code")
bankCodeL.config(text = "Bank Security Code")
accountW.config(values = list(people.keys()))
accountD.config(values = list(people.keys()))
account.config(values = add(list(people.keys()), "all"))
submitW.config(text = "Submit", command = withdrawSubmit)
submitD.config(text = "Submit", command = depositSubmit)
openAccount.config(text = "Open Account", command = showAcount)
"""loan"""
loanCodeL.config(text = "Security Code")
loanAmountL.config(text = "Loan Amount")
loanReciever.config(values = add(list(people.keys()), "bank", "remove"))
loanSubmit.config(text = "Submit", command = loanRecord)
loanPayBack.config(values = ["Pay off loan", "Get loan", "See loan"], width = 9)
"""produce"""
baseL.config(text = "Base Produce Value")
produceGo.config(text = "Go", command = calcProduce)
boosterL.config(text = "Base Booster Value")

itemList.config(values = list(items.keys()))
itemBuy.config(text = "Details", command = itemDetails)
itemClear.config(text = "Clear", command = clearA)
addNameL.config(text = "Item Name")
addPriceL.config(text = "Item Price")
addSellerL.config(text = "Item Seller")
addSeller.config(values = list(people.keys()))
addCodeL.config(text = "Security Code")
addDescriptionL.config(text = "Item Description")
addSubmit.config(text = "Submit", command = newItem)


# geometry managers
"""root"""
fromL.grid(row = 0, column = 0)
arrow1.grid(row = 0, column = 1)
toL.grid(row = 0, column = 2)
fromB.grid(row = 1, column = 0)
arrow2.grid(row = 1, column = 1)
toB.grid(row = 1, column = 2)
fromCodeL.grid(row = 2, column = 0)
toCodeL.grid(row = 2, column = 2)
fromCode.grid(row = 3, column = 0)
toCode.grid(row = 3, column = 2)
amountL.grid(row = 4, column = 1)
amount.grid(row = 5, column = 1)
transfer.grid(row = 6, column = 1)
end.grid(row = 8, column = 3)
"""add"""
personL.pack()
person.pack()
codeL.pack()
code.pack()
addB.pack()
"""bank"""
bankOps.pack()

titleS.pack()
account.pack()
openAccount.pack()

titleD.pack()
accountD.pack()
bankCodeL.pack()
bankCode.pack()
amountLD.pack()
amountD.pack()
submitD.pack()

titleW.pack()
accountW.pack()
codeLW.pack()
codeW.pack()
amountLW.pack()
amountW.pack()
submitW.pack()

"""loan"""
loanReciever.pack()
loanCodeL.pack()
loanCode.pack()
loanAmountL.pack()
loanAmount.pack()
loanPayBack.pack()
loanSubmit.pack()
"""produce"""
storeOps.pack()
baseL.pack()
base.pack()
boosterL.pack()
booster.pack()
produceGo.pack()
itemList.pack()
itemBuy.pack()
itemClear.pack()
addNameL.grid(row = 0,column = 0)
addPriceL.grid(row = 1,column = 0)
addSellerL.grid(row = 2,column = 0)
addCodeL.grid(row = 3,column = 0)
addDescriptionL.grid(row = 4,column = 0)
addName.grid(row = 0,column = 1)
addPrice.grid(row = 1,column = 1)
addSeller.grid(row = 2,column = 1)
addCode.grid(row = 3,column = 1)
addDescription.grid(row = 4,column = 1)
addSubmit.grid(row = 5,column = 1)
