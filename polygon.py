import turtle
turtle.Screen().bgcolor("yellow")
turtle.Screen().setup(300,500)

polygon=turtle.Turtle()
sides=6
lenght=70
angle=360.0/sides

for i in range(sides):
    polygon.forward(lenght)
    polygon.left(angle)
    
turtle.done()





