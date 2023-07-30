from turtle import Turtle,Screen
screen= Screen()
screen.setup(width=500,height=400)
user_bet=screen.textinput(title="make bet",prompt="select color of turtle: ")
colors=["red","yellow","blue","green","purple","orange"]
y_position=[-70,-40,-10,26,53,90]

for i in range(0,6):
    tim = Turtle()
    tim.shape("turtle")
    tim.penup()
    tim.color(colors[i])
    tim.goto(x=-230,y=y_position[i])
screen.exitonclick()

