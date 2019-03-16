#Imports modules needed for program
from graphics import *
from random import *

#Define custom function that will create the rings of the bullseye
def mk_circle(rad, cirX, cirY, color, window):
    #Create a circle using two pieces of data:
        #1. Center point of circle
        #2. Radius of circle
    bullRing = Circle(Point(cirX, cirY), rad)
    #Colors circle
    bullRing.setFill(color)
    #Draws circle on window
    bullRing.draw(window)

#Boolean variable acting as escape condition for while loop that ensures proper
#inputs
userInput = True

#Creates window called "Frankie Boi's Bullseye" that bullseye will be drawn on
window = GraphWin("Frankie Boi's Bullseye", 600, 600)
window.setCoords(0, 0, 600, 600)

#Determine if user would rather have random values for variables or manually
#input values for variables
while userInput:
    try:
        rand = input("""Do you want the program to randomly generate your
bullseye? Or do you want to enter values for each element of the bullseye?

Type in random to have to program randomly generate your bullseye,
or type in manual to enter values manually: """)
        #Sets user input to all lowercase
        rand = rand.lower()
        #If user input is valid, escape while loop
        if rand == "random" or rand == "manual":
            userInput = False
        #Otherwise offer feedback and stay in loop
        else:
            print("\nSorry, that input is not valid. Please check your spelling.")
    #If user enters wrong data type, offer feedback and loop back to try
    except ValueError:
        print("""\nSorry, that input is not valid. Please only enter
letters. Enter random if you want the program to randomly generate your
bullseye,or enter manual to enter values manually: """)

#Assigns random values to variables, if user chose to have computer generate
#random values for variables
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
    counter = randint(2,20)
#Otherwise, prompt the user to enter values for each variable
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

#For loop controls how many rings are drawn
for i in range(counter):
    #Uses the modulus operator to determine if i is even or odd to color the
    #rings appropriatly
    if i % 2 == 0:
        color = color1
    else:
        color = color2
    #Calls the mk_circle function
    mk_circle(rad * counter,
              cirX, cirY,
              color,
              window)
    #Increments the counter
    counter -= 1

#Waits until user clicks onto window, then closes it
window.getMouse()
window.close()
