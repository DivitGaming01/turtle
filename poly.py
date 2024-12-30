import turtle
turtle.Screen().bgcolor("Lime")
turtle.Screen().setup(300,400)
p=turtle.Turtle()
side=6
s_lenth=70
angle=360.0/side
for i in range(side):
    p.forward(s_lenth)
    p.right(angle)
turtle.done()