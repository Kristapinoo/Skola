import turtle

Toto = turtle.Turtle()
Toto.penup()
Toto.goto(-300, -150)
Toto.pendown()
Toto.speed(1)

Toto.fillcolor("red")    # māja
Toto.begin_fill()
Toto.forward(600)
Toto.left(90)
Toto.forward(300)
Toto.left(90)
Toto.forward(600)
Toto.left(90)
Toto.forward(300)
Toto.end_fill()

Toto.penup()            #durvis
Toto.left(90)
Toto.forward(150)
Toto.left(90)
Toto.pendown()
Toto.fillcolor("Brown")
Toto.begin_fill()
Toto.forward(170)
Toto.right(90)
Toto.forward(100)
Toto.right(90)
Toto.forward(170)
Toto.end_fill()

Toto.penup()
Toto.goto(-80, -85)
Toto.pendown()
Toto.dot(20)

Toto.penup()            #logs
Toto.goto(100, -50)
Toto.pendown()
Toto.left(90)
Toto.fillcolor("blue")
Toto.begin_fill()
for i in range(0, 4):
    Toto.forward(130)
    Toto.left(90)
Toto.pensize(3)
for i in range(0, 4):
    Toto.end_fill()
    Toto.forward(65)
    Toto.left(90)
    Toto.forward(130)
    Toto.left(90)
    Toto.forward(65)
    Toto.left(90)
Toto.pensize(1)

Toto.penup()        #jumts
Toto.goto(-300, 150)
Toto.pendown()
Toto.fillcolor("orange")
Toto.begin_fill()
Toto.left(30)
Toto.forward(346)
Toto.right(60)
Toto.forward(346)
Toto.end_fill()

Toto.backward(96)      #skurstenis
Toto.left(120)
Toto.fillcolor("red")
Toto.begin_fill()
Toto.forward(110)
Toto.left(90)
Toto.forward(50)
Toto.left(90)
Toto.forward(82)
Toto.end_fill()
Toto.penup()
Toto.goto(190, 330)
Toto.pendown()
Toto.pencolor("grey")
Toto.dot(35)
Toto.goto(195, 350)
Toto.dot(30)
Toto.goto(200, 365)
Toto.dot(25)
Toto.goto(210, 375)
Toto.dot(20)
turtle.done()