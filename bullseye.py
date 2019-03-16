from graphics import *
from random import *

def mk_circle(rad, cirX, cirY, color, window):
    bullRing = Circle(Point(cirX, cirY), rad)
    bullRing.setFill(color)
    bullRing.draw(window)

rad = randint(10, 100)
cirXY = randint(200, 400)
color = color_rgb(randint(0, 255), randint(0, 255), randint(0, 255))

window = GraphWin("Frankie Boi's Bullseye", 600, 600)
window.setCoords(0, 0, 600, 600)

mk_circle(rad, cirXY, cirXY, color, window)
