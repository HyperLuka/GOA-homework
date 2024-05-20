from turtle import *


#we want to paint a house

#step 1:  draw a square


width(7)
color("brown")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing of a door
begin_fill()
forward(70)
color("black")
left(90)
forward(120)
right(90) 
forward(60)
right(90)
forward(120)
end_fill()


penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#drawing of windows

penup()
goto(195, 180)
pendown()
color("blue")
begin_fill()
left(30)
forward(50)
right(90)
forward(60)
right(90)
forward(50)
right(90)
forward(60)
end_fill()


penup()
goto(5, 180)
pendown()
begin_fill()
forward(60)
right(90)
forward(50)
right(90)
forward(60)
right(90)
forward(50)
end_fill()





exitonclick()