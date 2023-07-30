from turtle import Turtle,Screen
import random
screen= Screen()
screen.setup(width=500,height=400)
is_race_on=False
user_bet=screen.textinput(title="make bet",prompt="select color of turtle: ")
colors=["red","yellow","blue","green","purple","orange"]
y_position=[-70,-40,-10,26,53,90]
all_turtles=[]
for i in range(0,6):
    tim= Turtle()
    tim.shape("turtle")
    tim.penup()
    tim.color(colors[i])
    tim.goto(x=-230,y=y_position[i])
    all_turtles.append(tim)
if user_bet:
    is_race_on=True
while is_race_on:
                for turtle in all_turtles:
                    if turtle.xcor()>230:
                        is_race_on=False
                        win_color=turtle.pencolor()
                        if win_color == user_bet:
                            print(f"you won,the {win_color} turtle won")
                        else:
                            print(f"you lose,the {win_color} turtle won")
                    rand_distance=random.randint(0,10)
                    turtle.forward(rand_distance)
screen.exitonclick()

