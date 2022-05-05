from tkinter import *

# from pyparsing import matchPreviousExpr
mansLogs = Tk() # definēšana
mansLogs.title("kalkulatora logs") # loga nosaukums
#mansLogs.iconbitmap('ikona.ico') # ikona(obligāti jābūt ico, jābūt projekta mapītē)
mansLogs.geometry("600x600") # loga izmērs
# poga = Button(mansLogs, text="Sveiks", bg="black",fg="white" ) # pogas definēšana,(manslogs - kurā logā, teksts uz pogas, fons, teksta krāsa)
# poga.pack() 

def btnClick(number):
    current = e.get()
    e.delete(0,END)
    newNumber= str(current)+str(number)
    e.insert(0,newNumber)
    return 0

def btnCommand(command):
    global num1
    global mathOp
    mathOp = command
    num1= int(e.get())
    e.delete(0, END)
    return 0

def Equals():
    num2 = int(e.get())
    result = 0
    if mathOp =="+":
        result= num1 + num2
    elif mathOp=="-":
        result=num1-num2
    else:
        result=0
    e.delete(0,END)
    e.insert(0,str(result))
    return 0

def Clear():
    e.delete(0,END)
    num1=0
    mathOp=""
    return 0

e=Entry(mansLogs, width=20,font = ("Arial Black", 24))

poga0=Button(mansLogs, text="0",padx="50",pady="25", command=lambda:btnClick(0))
poga1=Button(mansLogs, text="1",padx="50",pady="30", command=lambda:btnClick(1))
poga2=Button(mansLogs, text="2",padx="50",pady="30", command=lambda:btnClick(2))
poga3=Button(mansLogs, text="3",padx="50",pady="30", command=lambda:btnClick(3))
poga4=Button(mansLogs, text="4",padx="50",pady="30", command=lambda:btnClick(4))
poga5=Button(mansLogs, text="5",padx="50",pady="30", command=lambda:btnClick(5))
poga6=Button(mansLogs, text="6",padx="50",pady="30", command=lambda:btnClick(6))
poga7=Button(mansLogs, text="7",padx="50",pady="30", command=lambda:btnClick(7))
poga8=Button(mansLogs, text="8",padx="50",pady="30", command=lambda:btnClick(8))
poga9=Button(mansLogs, text="9",padx="50",pady="30", command=lambda:btnClick(9))
pogaAdd=Button(mansLogs, text="+",padx="50",pady="25", command=lambda:btnCommand("+"))
pogaSub=Button(mansLogs, text="-",padx="50",pady="25", command=lambda:btnCommand("-"))
pogaEquals=Button(mansLogs, text="=",padx="50",pady="30", command=Equals)
pogaClear=Button(mansLogs, text="C",padx="50",pady="30", command=Clear)

poga7.grid(row=4, column=0)
poga8.grid(row=4, column=1)
poga9.grid(row=4, column=2)

poga4.grid(row=3, column=0)
poga5.grid(row=3, column=1)
poga6.grid(row=3, column=2)

poga1.grid(row=2, column=0)
poga2.grid(row=2, column=1)
poga3.grid(row=2, column=2)

poga0.grid(row=5, column=0)
pogaAdd.grid(row=5, column=1)
pogaSub.grid(row=5, column=2)

#pogaEquals.grid(row=1, column=3, rowspan=3)
#pogaClear.grid(row=4, column=3)
e.grid(row=0, column=0, columnspan=3)





mansLogs.mainloop()

