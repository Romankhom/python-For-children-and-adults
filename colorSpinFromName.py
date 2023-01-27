#color spiral from user name
import turtle # встановлення графіки Turtle
t = turtle.Pen()
turtle.bgcolor("black")
colors = ("red","yellow","green","blue")
#Запит імя коритсувача за допомогою вспливаючого вікна
# textinput
yourName = turtle.textinput("Введіть ваше ім'я", "Як вас звати?")
# Намалювати на екрані спірал повторену 100 разів
for x in range (1000):
    t.pencolor(colors[x%4]) #вибирати по черзі всі 4 кольори
    t.penup() #на малювати звичайні лінії спіралі
    t.forward(x*4) #просто перемістити черепашку по екрану
    t.pendown() #написати ім'я користувача збільшуючи шрифт кожного разу
    t.write(yourName, font = ("Arial", int((x+4)/4),"bold"))
    t.right(120) #повернути наліво як в інших спіралях