#2019-20 Fall Computer Science Principles Final Exam

#Ms. Haubold


#Name
#Braxton Garza
#Date 12/18/19
#


#### INSTRUCTIONS ####
#Create an etch a sketch turtle game
#The turtle should move with the arrow keys (up, down, left and right), and draw
#Space should clear the screen
#o and p should make the pen size bigger and smaller
#u should pick the pen up or put the pen down
#All code must be commented
#BONUS
#Add a feature to change colors
#

#import required libraries
import turtle as trtl 




#create turtle
sketchyboi=trtl.Turtle()
sketchyboi.shape= "classic"
sketchyboi.turtlesize=(3)
sketchyboi.goto(0,0)
sketchyboi.pendown()
sketchyboi.pensize(3)
#movement functions
#makes turtle go up when this function is called
def goup ():
    sketchyboi.setheading(90)
    sketchyboi.forward(10)
#makes turtle go right when called
def goright ():
    sketchyboi.setheading(0)
    sketchyboi.forward(10)
#makes turtle go down when called
def godown ():
    sketchyboi.setheading(270)
    sketchyboi.forward(10)
#makes turtle go left when called
def goleft ():
    sketchyboi.setheading(180)
    sketchyboi.forward(10)
#clears screen when called
def clear ():
    sketchyboi.clear()
#picks pen up when called
def penup ():
    sketchyboi.penup()
#puts pen down when called
def pendown():
    sketchyboi.pendown()
#makes pensize bigger
def uppensize():
    sketchyboi.pensize(8)
#makes pensize smaller
def downpensize():
    sketchyboi.pensize(3)



















#color/drawing functions



#create screen
wn=trtl.Screen()

#bind to keypresses

wn.onkeypress(goup , "Up")
wn.onkeypress(goright , "Right")
wn.onkeypress(godown , "Down")
wn.onkeypress(goleft , "Left")
wn.onkeypress(clear , "space")
wn.onkeypress(penup , "u")
wn.onkeypress(pendown , "d")
wn.onkeypress(uppensize , "o")
wn.onkeypress(downpensize , "p")
#(up) moves turtle up(left)moves turtle left(right)moves it to the right(down)moves it down(space)clears the screen(u)pickes up pen(d)puts down pen(o)makes pen bigger(p)brings pen back to normal





#listen
wn.listen()


#mainloop
wn.mainloop()
