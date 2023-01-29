import turtle #settings of turtle grafics
t=turtle.Pen()
turtle.bgcolor("black")
#settings list of any color names of Python
colors = ["red","green","yellow","blue","purple","orange","white","gray"]
#ask user of count of side from 1 to 8
#default quolity is 4
sides = int(turtle.numinput("how many sides you want from 1 to 8", 1 - 8))
#painting colorfull spiral with numbers of sides
for x in range(360) :
    t.pencolor(colors[x % sides]) #used corect colors counting
    t.forward(x * 3 / sides + x) #increase the pen size
    t.left(360 / sides + 1) #change the size with sides counting
    t.width(x * sides / 200) #turn to 360 degree +1 side
