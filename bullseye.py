from graphics import *

def mk_circle(rad, cirX, cirY, color, window):
    bullRing = Circle(Point(cirX, cirY), rad)
    bullRing.setFill(color)
    bullRing.draw(window)

window = GraphWin("Frankie Boi's Bullseye", 600, 600)
window.setCoords(0, 0, 600, 600)

mk_circle(50, 300, 300, "red", window)
