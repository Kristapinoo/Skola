from tkinter import *

# from pyparsing import matchPreviousExpr
kase = Tk() # definēšana
kase.title("Kases aparats") # loga nosaukums
#mansLogs.iconbitmap('ikona.ico') # ikona(obligāti jābūt ico, jābūt projekta mapītē)
kase.geometry("1000x600") # loga izmērs
# poga = Button(mansLogs, text="Sveiks", bg="black",fg="white" ) # pogas definēšana,(manslogs - kurā logā, teksts uz pogas, fons, teksta krāsa)
# poga.pack() 
def btnClick(number): # Lai raksta ciparus
    current = e.get()
    e.delete(0,END)
    newNumber= str(current)+str(number)
    e.insert(0,newNumber)
    return 0
 

def btnCommand(command):
    global num1
    global mathOp
    mathOp = command
    num1= float(e.get())
    if mathOp =="Kopā":
        ceks.insert(INSERT, f"Gala cena ir {num1}EUR\n")
    e.delete(0, END)
    return 0


def Equals():
    num2 = float(e.get())
    result = 0
    if mathOp =="Zāles":
        ceks.insert(INSERT, f"Zāles {num2}EUR \n")
        result= round(num1, 2) + round(num2, 2)
        
    elif mathOp=="Produkti":
        ceks.insert(INSERT, f"Produkti {num2}EUR\n")
        result=round(num1, 2)+ round(num2, 2)  

   # elif mathOp=="Kopā":
        
    
         

    else:
        result=0
    e.delete(0,END)
    e.insert(0,str(round(result, 2)))
    return 0
    
def Clear():
    e.delete(0,END)
    e.insert(0, 0)
    num1=0
    # mathOp=""
    return 0





poga0=Button(kase, text="0",width=5,padx="20",pady="10", font = ("Direct font format", 15), command=lambda:btnClick(0))
poga1=Button(kase, text="1",width=5,padx="20",pady="10", font = ("Direct font format", 15),command=lambda:btnClick(1))
poga2=Button(kase, text="2",width=5,padx="20",pady="10", font = ("Direct font format", 15),command=lambda:btnClick(2))
poga3=Button(kase, text="3",width=5,padx="20",pady="10", font = ("Direct font format", 15),command=lambda:btnClick(3))
poga4=Button(kase, text="4",width=5,padx="20",pady="10", font = ("Direct font format", 15),command=lambda:btnClick(4))
poga5=Button(kase, text="5",width=5,padx="20",pady="10", font = ("Direct font format", 15),command=lambda:btnClick(5))
poga6=Button(kase, text="6",width=5,padx="20",pady="10", font = ("Direct font format", 15),command=lambda:btnClick(6))
poga7=Button(kase, text="7",width=5,padx="20",pady="10", font = ("Direct font format", 15),command=lambda:btnClick(7))
poga8=Button(kase, text="8",width=5,padx="20",pady="10", font = ("Direct font format", 15),command=lambda:btnClick(8))
poga9=Button(kase, text="9",width=5,padx="20",pady="10", font = ("Direct font format", 15),command=lambda:btnClick(9))
pogaEquals=Button(kase, text="Apstiprināt",width = 27, padx="28",pady="10", font = ("Direct font format", 15),command=Equals)
pogaClear=Button(kase, text="Dzēst", width=5, padx="20",pady="10", font = ("Direct font format", 15),command=Clear)
pogaKomats=Button(kase, text=".",width=5,padx="20",pady="10", font = ("Direct font format", 15),command=lambda:btnClick("."))
pogaZales=Button(kase, text="Zāles",width=5,padx="20",pady="10", font = ("Direct font format", 15),command=lambda:btnCommand("Zāles"))
pogaProdukti=Button(kase, text="Produkti",width=5,padx="20",pady="10", font = ("Direct font format", 15),command=lambda:btnCommand("Produkti"))
pogaAtlaide=Button(kase, text="Atlaide",width=5,padx="20",pady="10", font = ("Direct font format", 15),command=lambda:btnCommand("Atlaide"))
pogaKopa=Button(kase, text="Kopā",width = 27, padx="28",pady="10", font = ("Direct font format", 15),command=lambda:btnCommand("Kopā"))
e=Entry(kase, font = ("Arial Black", 20))
e.insert(0, 0)
# ceks=Text(kase, width=20, font = ("Helvetica", 15))
# ceks.set(text)
ceks = Text(kase, font=("Direct font format", 15),  )
ceks.pack()
ceks.insert(INSERT, "                     ČEKS\n\n ",)










e.place(x = 50, y = 0)
ceks.place(x = 700, y = 0)

poga1.place(x = 50, y = 50)
poga2.place(x = 180, y = 50)
poga3.place(x = 310, y = 50)
pogaZales.place(x = 500, y = 50)

poga4.place(x = 50, y = 120)
poga5.place(x = 180, y = 120)
poga6.place(x = 310, y = 120)
pogaProdukti.place(x = 500, y = 120)

poga7.place(x = 50, y = 190)
poga8.place(x = 180, y = 190)
poga9.place(x = 310, y = 190)


poga0.place(x=50, y = 260)
pogaKomats.place(x = 180, y = 260)
pogaClear.place(x = 310, y = 260)

pogaEquals.place(x = 50, y = 330)

pogaKopa.place(x = 50, y = 400)

kase.mainloop()