from turtle import *
from winsound import *
from os import *

state = {'turn': 0}


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


def animate():
    """Animate fidget spinner."""
    if state['turn'] > 0:
        state['turn'] -= 1

    spinner()
    ontimer(animate, 20)


def flickl():
    """Flick fidget spinner."""
    state['turn'] += 10
def flickk():
    state['turn'] -= 10

def skana():
   PlaySound('uuuu.wav', SND_LOOP) 



setup(420, 420, 370, 0)
hideturtle()
tracer(False)
width(20)
onkey(flickk, 'Left')
onkey(flickl, 'Right')
#onkey(skana, 'space')
listen()
animate()
done()