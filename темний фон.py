import turtle
t = turtle.Pen()
turtle.bgcolor('darkblue')
colors = ['red','yellow','green','purple']
for x in range(100):
    t.pencolor(colors[x%4])
    t.circle(x)
    t.left(90)
