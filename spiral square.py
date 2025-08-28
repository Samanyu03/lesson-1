import turtle

turtle.Screen().bgcolor("purple")
a=turtle.Turtle()
size=0

while True:
    for i in range(4):
        a.forward(size+1)
        a.left(90)
        size=size-5
        
    size=size+1
    

        