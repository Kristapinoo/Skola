from turtle import *
from winsound import *
from os import *

state = {'turn': 0}
skaits = 0

def spinner():
    """Draw fidget spinner."""
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

def skaits():
    speed(0)
    color("black")
    penup()
    hideturtle()
    goto(0, 250)
    write("Modeli esi pārvietojis", align="center", font=("Courier", 16, "normal"))
def animate():
    """Animate fidget spinner."""
    if state['turn'] > 0:
        state['turn'] -= 1

    spinner()
    ontimer(animate, 20)


def flickl():
    """Flick fidget spinner to the right."""
    state['turn'] += 10
def flickk():
    """Flick fidget spinner to the left."""
    state['turn'] -= 10

def skana():
   PlaySound("uuuu.wav", SND_ALIAS) 

def stop():
    state['turn'] = 0



setup(420, 550, 370, 0)
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
# uzspiežot taustiņu spacebar, modelis pilnīgi apstājas
# paplašināju logu, lai varētu skaitītāju ievietot