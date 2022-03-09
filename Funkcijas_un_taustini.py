import turtle
turtle.setup(1080, 720) # nomainda standarta loga izmēru uz izvēlēto
screen = turtle.Screen() # izveido logu, bet nav nenodzēšams kursors 0, 0 koordinātēs
screen.bgcolor("gray")
Toto = turtle.Turtle("turtle")
Toto.speed(-1) #pārvietošanās animācijas momentālā

def moveForward():
    Toto.forward(10)
def moveBackward():
    Toto.backward(10)
def moveRight():
    Toto.right(30)
def moveLeft():
    Toto.left(30)

def paceltPildspalvu():
    Toto.penup()

def nolaistPildspalvu():
    Toto.pendown()

screen.onkey(paceltPildspalvu, "a")
screen.onkey(nolaistPildspalvu, "s")

# screen.onkey(moveForward, "Up") # nospiežot bultiņu uz augšu pārvietosies uz priekšu
# screen.onkey(moveLeft, "Left")
# screen.onkey(moveRight, "Right") 
# screen.onkey(moveBackward, "Down")

# onkey - mirklī, kad nospiež
# onkeypress - mirklī, kad tur
# on keyrelease - mirklī, kad atlaiž

# screen.onkeypress(moveForward, "Up") # turot nospiestu bultiņu uz augšu pārvietosies
# screen.onkeypress(moveLeft, "Left")
# screen.onkeypress(moveRight, "Right")
# screen.onkeypress(moveBackward, "Down")

def mouseDragging(x, y):
    #print(x, y) šīs koordinātas ondrag izveido pats
    Toto.ondrag(None) # pārstāj uz mirkli vilkt peli
    Toto.setheading(Toto.towards(x, y))
    # setheading - pagriež bruņurupucis
    # towards - nosaka leņķi no pašreizējās atrašanās vietas uz vēlamo
    Toto.goto(x, y) # pārvieto uz koordinātēm, kur atrodas velkošais kursors
    Toto.ondrag(mouseDragging) # atsākt vilkt peli
    # izveidojas rekursija - jeb kad funkcija izsauc pati sevi (nav 100% pareizi, jo iekš ondrag izsauc funkciju, bet pēc būtības notiek rekursija)
    # elpošana - ieelpas, izelpas, kad pabeidz elpošanu izsauc vēlreiz elpošanu

def clearScreen(x, y):
    Toto.clear()
Toto.ondrag(mouseDragging) # velk ar kreiso taustiņu
# Toto.ondrag(mouseDragging, 3) velk ar labo taustiņu
screen.onclick(clearScreen, 3) # notīram ekrānu nospiežot labo peles taustiņu
# 1 - kriesais peles taustiņš
# 2 - scroll
# 3 - labais peles taustiņš

screen.listen() # klausās vai notiek kāda darbība (vai lietotājs kaut ko dara)
screen.mainloop() # tur vaļā logu un ļauj atkārtoti izpildīt komandas