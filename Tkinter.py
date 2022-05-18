from tkinter import *

# from pyparsing import matchPreviousExpr
kase = Tk() # definēšana
kase.title("Kases aparats") # loga nosaukums
#mansLogs.iconbitmap('ikona.ico') # ikona(obligāti jābūt ico, jābūt projekta mapītē)
#kase.geometry("1000x600") # loga izmērs
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

poga0=Button(kase, text="0",padx="20",pady="10", font = ("Direct font format", 15), command=lambda:btnClick(0))
poga1=Button(kase, text="1",padx="20",pady="10", font = ("Direct font format", 15),command=lambda:btnClick(1))
poga2=Button(kase, text="2",padx="20",pady="10", font = ("Direct font format", 15),command=lambda:btnClick(2))
poga3=Button(kase, text="3",padx="20",pady="10", font = ("Direct font format", 15),command=lambda:btnClick(3))
poga4=Button(kase, text="4",padx="20",pady="10", font = ("Direct font format", 15),command=lambda:btnClick(4))
poga5=Button(kase, text="5",padx="20",pady="10", font = ("Direct font format", 15),command=lambda:btnClick(5))
poga6=Button(kase, text="6",padx="20",pady="10", font = ("Direct font format", 15),command=lambda:btnClick(6))
poga7=Button(kase, text="7",padx="20",pady="10", font = ("Direct font format", 15),command=lambda:btnClick(7))
poga8=Button(kase, text="8",padx="20",pady="10", font = ("Direct font format", 15),command=lambda:btnClick(8))
poga9=Button(kase, text="9",padx="20",pady="10", font = ("Direct font format", 15),command=lambda:btnClick(9))
pogaAdd=Button(kase, text="+",padx="20",pady="10", font = ("Direct font format", 15),command=lambda:btnCommand("+"))
#pogaSub=Button(kase, text="-",padx="20",pady="10", font = ("Direct font format", 15),command=lambda:btnCommand("-"))
#pogaEquals=Button(kase, text="=",padx="30",pady="10", font = (40),command=Equals)
pogaClear=Button(kase, text="C",padx="20",pady="10", font = (40),command=Clear)

atstarpe0=Label(kase, text=" ", padx="20")
atstarpe1=Label(kase, text=" ", pady="10")
atstarpe2=Label(kase, text=" ", pady="10") 
e=Entry(kase, width=20, font = ("Arial Black", 20))
ceks=Entry(kase, width=20)

e.grid(row=0, column=1, columnspan=4)
atstarpe0.grid(row=0, column=6, columnspan=2)
ceks.grid(row=0, column=8, columnspan=3)

atstarpe1.grid(row=1, column=0)

poga1.grid(row=2, column=1)
poga2.grid(row=2, column=2)
poga3.grid(row=2, column=3)

atstarpe2.grid(row=3, column=0)

poga4.grid(row=4, column=1)
poga5.grid(row=4, column=2)
poga6.grid(row=4, column=3)

poga7.grid(row=4, column=0)
poga8.grid(row=4, column=1)
poga9.grid(row=4, column=2)

poga0.grid(row=5, column=0)
pogaAdd.grid(row=5, column=1)
#pogaSub.grid(row=5, column=2)

#pogaClear.grid(row=4, column=3)





kase.mainloop()
