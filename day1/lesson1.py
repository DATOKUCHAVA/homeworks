from turtle import *


#we want to paint a house

#step1 draw a square
speed(8)
width(9)
color("red")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door
forward(70)
color("blue")
begin_fill()
left(90)
forward(120) #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown

color("yellow")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()


penup()
goto(140,140)
pendown()

color("purple")
begin_fill()
right(150)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
end_fill()



penup()
goto(70,140)
pendown()
color("purple")
begin_fill()
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
end_fill()

exitonclick()
        