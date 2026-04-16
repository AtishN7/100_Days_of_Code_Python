from turtle import Turtle, Screen

class Kasav :
    def __init__(self):
        self.turtle = Turtle()
        self.screen =Screen()

    def kasav_properties(self, sp, wd):
        self.turtle.shape("arrow")
        self.turtle.color("DarkOliveGreen4")
        self.turtle.speed(sp)
        self.turtle.width(wd)

    def kasav_screen_setup(self):
        self.screen.setup(width=1400, height=1000)
        self.screen.bgcolor("snow")

    def kasav_screen_exit(self):
        self.screen.exitonclick()

    def move_forwards(self):
        self.turtle.forward(50)

    def move_backwards(self):
        self.turtle.backward(50)

    def turn_counter_clockwise(self):
        self.turtle.left(10)

    def turn_clockwise(self):
        self.turtle.right(10)

    def move_circular(self):
        self.turtle.circle(radius=100,extent=10)

    def clear_screen(self):
        self.turtle.clear()
        self.turtle.teleport(x=0,y=0)
        self.turtle.setheading(0)
        self.turtle.tiltangle(0)

    def screen_listen(self):
        self.screen.listen()

    def screen_on_key(self):
        self.screen.onkey(key="w",fun=self.move_forwards)
        self.screen.onkey(key="s",fun=self.move_backwards)
        self.screen.onkey(key="a", fun=self.turn_clockwise)
        self.screen.onkey(key="d",fun=self.turn_counter_clockwise)
        self.screen.onkey(key="e",fun=self.move_circular)
        self.screen.onkey(key="c",fun=self.clear_screen)


