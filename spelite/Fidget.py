from turtle import *
from winsound import *

state = {'turn': 0}

def spinner():
    clear()
    angle = state['turn'] / 10
    right(angle)
    forward(100)
    dot(120, 'red')
    back(100)
    right(120)
    forward(100)
    dot(120, 'green')
    back(100)
    right(120)
    forward(100)
    dot(120, 'blue')
    back(100)
    right(120)
    update()

def animate():
    if state['turn'] > 0:
        #state['turn'] -= 1

    #spinner()
    #ontimer(animate, 20)

def flickl():
    state['turn'] += 15

def flickk():
    state['turn'] -= 10

def skana():
   PlaySound("uuuu.wav", SND_ALIAS) 

def stop():
    state['turn'] = 0

pen = Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 220)
pen.write("Kustības taustiņi ir ← un →, ", align="center", font=("Courier", 14, "normal"))
pen.goto(0, 200)
pen.write("lai apstādinātu kustību izmanto 'space'", align="center", font=("Courier", 14, "normal"))

setup(500, 500, 370, 0)
hideturtle()
tracer(False)
width(20)
onkey(flickk, 'Left')
onkey(flickl, 'Right')
#onkey(skana, 'space')
onkey(stop, 'space')
listen()
animate()
done()