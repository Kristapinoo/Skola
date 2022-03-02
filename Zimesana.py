import turtle, random # zīmēšanas imports

krasa=["red", "green", "blue"]
Toto = turtle.Turtle() # Piesaista kursoru pie zīmēšanas
Toto.shape("turtle") # kāda forma kursoram. (turtle, circle, arrow, classic, square, triangle)
Toto.speed(10) # norāda cik ātri uzzīmēs
Toto.color("red") # krāsa aplim
Toto.circle(100) # uzzīmē apli
Toto.color(random.choice(krasa)) # no mūsu saraksta uz random izvēlēsies krāsu
Toto.circle(50, steps=2) #Cik ir pie steps skaitlis, tik stūra figūru uzzīmēs
Toto.forward(200) # uzzīmē kursora virzienā noteiktu skaitu.
Toto.right(90) # var norādīt uz kuru pusi pagriežas. Iekavās norāda cik grādus
Toto.forward(200)
Toto.right(90)
Toto.forward(200)
Toto.right(90)
Toto.forward(200)
Toto.right(90)
Toto.backward(30) # Dodas atpakaļgaitā attiecīgi kursora virzienam.
for i in range(0, 12): # Izveidos skaistu zīmējumu ar random krāsām
    Toto.circle(100)
    Toto.circle(100, steps=4)
    Toto.right(30)
    Toto.color(random.choice(krasa))
Toto.circle(100)
Toto.penup() # paceļ kursoru, jeb nekas nezīmējas līdz noliek atpakaļ
Toto.forward(200)
Toto.pendown() # Noliek kursoru un zīmē atkal visu līdz pacēļ atpakaļ augšā
Toto.circle(75)
Toto.penup()
Toto.forward(100)
Toto.pendown()
Toto.circle(50)