from graphics import *
from random import *

def mk_circle(rad, cirX, cirY, color, window):
    bullRing = Circle(Point(cirX, cirY), rad)
    bullRing.setFill(color)
    bullRing.draw(window)

userInput = True

window = GraphWin("Frankie Boi's Bullseye", 600, 600)
window.setCoords(0, 0, 600, 600)
while userInput:
    try:
        rand = input("""Do you want the program to randomly generate your
bullseye? Or do you want to enter values for each element of the bullseye?

Type in random to have to program randomly generate your bullseye,
or type in manual to enter values manually: """)
        rand = rand.lower()
        if rand == "random" or rand == "manual":
            userInput = False
        else:
            print("\nSorry, that input is not valid. Please check your spelling.")
    except ValueError:
        print("""\nSorry, that input is not valid. Please only enter
letters. Enter random if you want the program to randomly generate your
bullseye,or enter manual to enter values manually: """)

if rand == "random":
    rad = randint(10, 20)
    cirX = randint(200, 400)
    cirY = randint(200, 400)
    color1 = color_rgb(randint(0, 255),
                        randint(0, 255),
                        randint(0, 255))
    color2 = color_rgb(randint(0, 255),
                        randint(0, 255),
                        randint(0, 255))
    counter = 5
else:
    rad = int(input("\nEnter a integer value for the radius of the bullseye: "))
    cirX = int(
        input("\nEnter a integer value for the X position of the bullseye: "))
    cirY = int(
        input("\nEnter a integer value for the Y position of the bullseye: "))
    color1 = input(""":\nEnter a color for your bullseye. Examples are:
red,
yellow,
etc.: """)
    color2 = input(""":\nEnter a color for your bullseye. Examples are:
red,
yellow,
etc.: """)
    counter = int(
        input("\nEnter how many rings you want the bullseye to have: "))
    
for i in range(counter):
    if i % 2 == 0:
        color = color1
    else:
        color = color2
    mk_circle(rad * counter,
              cirX, cirY,
              color,
              window)
    counter -= 1

window.getMouse()
window.close()
