# Ja vēlas ielikt skaņu, tad tajai skaņai vajag būt vienā folder ar failu
import turtle
import winsound   # Atļauj veikt darbības ar operētājsistēmu

screen = turtle.Screen()
screen.title("PongPing") # loga nosaukums
screen.bgcolor("black") # loga fona krāsa
screen.setup(800, 600) # loga izmērs
screen.tracer(0) #pāatrināt spēli varēs

#Rezultāts
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Bumba
bumba = turtle.Turtle()
bumba.speed(0)
bumba.shape("square")
bumba.color("white")
bumba.penup()
bumba.goto(0, 0)
bumba.dx = 0.1     # delta kustības ziņā
bumba.dy = 0.1

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier", 24, "normal")) # teksts, kuru rādīs, centrā, ar custom fontu, izmēru un stilu(bold, italic)


def paddle_a_up():
    y = paddle_a.ycor() #ycor() - atgriež y vērtību, kur tieši tagad atrodas
    y += 20
    paddle_a.sety(y) # definē jauno y vietu
    
def paddle_a_down():
    y = paddle_a.ycor()
    y -=20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y +=20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -=20
    paddle_b.sety(y)

screen.listen()
screen.onkeypress(paddle_a_up, "w")
screen.onkeypress(paddle_a_down, "s")
screen.onkeypress(paddle_b_up, "Up")
screen.onkeypress(paddle_b_down, "Down")


#Main spēles kods
while True:
    screen.update()



    # Bumbas kustība
    bumba.setx(bumba.xcor() + bumba.dx)
    bumba.sety(bumba.ycor() + bumba.dy)

    # Border checking
    if bumba.ycor() > 290:
        bumba.sety(290)
        bumba.dy *= -1
        #winsound.PlaySound("faila_nosaukums.formāts", winsound.SND_ASYNC) # Skaņas ievietošana, aiz faila tas kods nozīmē, ka skaņai skanot viss neapstāsies
    
    if bumba.ycor() < -290:
        bumba.sety(-290)
        bumba.dy *= -1
        #winsound.PlaySound("faila_nosaukums.formāts", winsound.SND_ASYNC)

    if bumba.xcor() > 390:
        bumba.goto(0, 0)
        bumba.dx *= -1
        score_a += 1
        pen.clear()     # izdzēsīs iepriekšējo cipari, savādāk zīmē pāri tam
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal")) # Šajā gadījumā ar to .format atjaunos rezultātu pēc iegūtā punkta
        #winsound.PlaySound("faila_nosaukums.formāts", winsound.SND_ASYNC)

    if bumba.xcor() < -390:
        bumba.goto(0, 0)
        bumba.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        #winsound.PlaySound("faila_nosaukums.formāts", winsound.SND_ASYNC)

    if bumba.xcor() > 340 and bumba.xcor() < 350 and (bumba.ycor() < paddle_b.ycor() + 40 and bumba.ycor() > paddle_b.ycor() -40): #norāda, laukumu pret kuru atsitīsies pilnā garumā
        bumba.setx(340)
        bumba.dx *= -1

    if bumba.xcor() < -340 and bumba.xcor() > -350 and (bumba.ycor() < paddle_a.ycor() + 40 and bumba.ycor() > paddle_a.ycor() -40):
        bumba.setx(-340)
        bumba.dx *= -1