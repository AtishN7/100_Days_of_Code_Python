from turtle_attrs import Kasav
from turtle import Screen
from random import randint


screen = Screen()
screen.setup(width=1400, height=1000)
screen.bgcolor("snow")

turtles = []
turtle_colors = ["Firebrick", "DodgerBlue", "DarkOliveGreen", "DarkOrchid", "Orange", "Magenta", "GoldenRod"]
y_cor = 300

for t in range(7):
    kas = Kasav()
    kas.kasav_properties(color=turtle_colors[t])
    kas.start_position(x=-650, y=y_cor)
    y_cor -= 100
    turtles.append(kas)

user_bet = screen.textinput(title="Place your bet",prompt="Which turtle will win the race?(Pick a coloured Turtle!!)")
print(user_bet)

is_game_on = True

winner_turtle = ""
result_msg = ""

while is_game_on:

    for turtle in turtles:
        if turtle.get_x_coordinate() >= 650:
            is_game_on = False
            winner_turtle = turtle.get_turtle_color()
        rand_distnace = randint(0,20)
        turtle.move_forwards(rand_distnace)


if winner_turtle.lower() == user_bet.lower():
    result_msg = "You win!"
else:
    result_msg = "You lose!"

print(f"{result_msg} {winner_turtle} turtle wins!")

screen.exitonclick()