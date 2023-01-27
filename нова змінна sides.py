import turtle
t = turtle.Pen()
turtle.bgcolor('purple')
sides = eval(input('Введіть кількість сторін від 2 до 6: '))
colors = ['red','green','black','yellow','green','pink','orange','darkblue']
for x in range(360):
    t.pencolor(colors[x%sides])
    t.forward(x * 2/sides + x)
    t.left(360/sides + 1)
    t.width(x*sides/200)
    t.left(90)
