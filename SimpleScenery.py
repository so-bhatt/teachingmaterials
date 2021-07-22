import turtle # helps draw
import random # helps create random numbers

paper=turtle.Screen()# creating paper
pen=turtle.Turtle()# creating pen
pen.speed(100)# speeding up entire process
pen.color("OliveDrab")
pen.fillcolor("Olive")# setting color to triangle
pen.setpos(-50,0) # setting position such that triangle fully inside screen

pen.begin_fill()# starting triangle filling
pen.pensize(2)# changing pen thickness
pen.forward(200)# creating first line

pen.left(120)# rotate pen into correct position
pen.forward(200)# create second line

pen.left(120)# rotate pen into correct position
pen.forward(200)#create third line
pen.end_fill()# ending triangle filling


pen.setpos(-30,0)# setting square start point
pen.right(-30) # correcting the angle
pen.color("Red")# starting side color
pen.fillcolor("Red")# set square filling
pen.begin_fill()# starting square filling
pen.forward(160) # square's 1st sidelength
pen.left(90)# correcting direction

pen.forward(160)# square's 2nd sidelength
pen.left(90)# correcting direction

pen.forward(160)# square's 3rd sidelength
pen.left(90)# correcting direction

pen.forward(160)# square's 4th sidelength
pen.left(90)# correcting direction
pen.end_fill()# ending square filling

pen.setpos(-10,0)# setting pos for the door
pen.color("White") # setting pen color
pen.fillcolor("White") # setting fill color
pen.begin_fill()# starting door filling
pen.forward(160)#1st side
pen.left(90)# correcting direction

pen.forward(120)#2nd sidelength
pen.left(90)# correcting direction

pen.forward(160)#3rd sidelength
pen.left(90)# correcting direction

pen.forward(120)#4th sidelength
pen.left(90)# correcting direction
pen.end_fill()# ending door filling

pen.setpos(50,0)
pen.color("Red") # setting pen color
pen.fillcolor("Red") # setting fill color
pen.forward(160)

##### starting tree
####### leaves
pen.penup()## stopping drawing
pen.setpos(-120,0) # setting position for tree head
pen.right(90)# make cursor in correct direction
pen.color("Green")# starting side color
pen.fillcolor("Green")# set fill of tree
pen.begin_fill()#starts fill
pen.pendown()##starts the drawing again
pen.forward(60)## Creates 1st side
pen.right(120)## changes into correct direction
pen.forward(60)#2nd side
pen.right(120)## changes into correct direction
pen.forward(60)#3rd side
pen.right(120)## changes into correct direction
pen.end_fill()# ends fill
####### wood
pen.color("Brown")# base side color
pen.fillcolor("Brown")# base fill color
pen.penup()## stops drawing before in position for square's start
pen.setpos(-130,0)## starting position for square
pen.pendown()## starts drawing when making square
pen.begin_fill()
pen.forward(40)## 1st side
pen.left(90)# change direction
pen.forward(40)## 2nd side
pen.left(90)# change direction
pen.forward(40)## 3rd side
pen.left(90)## change direction
pen.forward(40)## 4th side
pen.left(90)## change direction
pen.end_fill()



pen.color("blue")
def snowflake(size):
# move the pen into starting position
    pen.penup()
    pen.forward(10*size)
    pen.left(45)
    pen.pendown()
    pen.color("blue")
    # draw branch 8 times to make a snowflake
    for i in range(8):
        branch(size)   
        pen.left(45)
def branch(size):
    for i in range(3):
        for i in range(3):
            pen.forward(10.0*size/3)
            pen.backward(10.0*size/3)
            pen.right(45)
        pen.left(90)
        pen.backward(10.0*size/3)
        pen.left(45)
    pen.right(90) 
    pen.forward(10.0*size)
num=random.randrange(5,10)## number of snowflakes
for ind in range(num):## repeating random snowflakes num time
  x=random.randrange(-200,200)## random x pos
  y=random.randrange(0,200)## random y pos
  pen.penup()## preventive measure such that streak is not visible
  pen.setpos(x,y)# setting position of snow flake
  pen.pendown()# start draw
  size=random.randrange(1,3)# set snowflake size
  snowflake(size)# create snowflake
paper.exitonclick()# exit
