import turtle
turtle.Screen().bgcolor("orange")
turtle.setup(300,400)
polygon=turtle.Turtle()
num_sides=6
length=70
angle=360/6
for i in range(num_sides):
    polygon.forward(length)
    polygon.left(angle)
    polygon.color("white")
turtle.done()