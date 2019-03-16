from graphics import *
from random import *

def mk_circle(rad, cirXY, color, window):
    bullRing = Circle(Point(cirXY, cirXY), rad)
    bullRing.setFill(color)
    bullRing.draw(window)

rad = randint(10, 20)
cirXY = randint(200, 400)
counter = 5

window = GraphWin("Frankie Boi's Bullseye", 600, 600)
window.setCoords(0, 0, 600, 600)

for i in range(counter):
    mk_circle(rad * counter,
              cirXY,
              color_rgb(randint(0, 255),
                        randint(0, 255),
                        randint(0, 255)),
              window)
    counter -= 1

window.getMouse()
window.close()
