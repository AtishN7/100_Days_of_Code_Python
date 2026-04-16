from turtle import Turtle

class Kasav :
    def __init__(self):
        self.turtle = Turtle()


    def kasav_properties(self, color):
        self.turtle.shape("turtle")
        self.turtle.color(color)
        self.turtle.speed(10)
        self.turtle.width(5)

    def start_position(self, x, y):
        self.turtle.penup()
        self.turtle.goto(x, y)

    def move_forwards(self, paces):
        self.turtle.forward(paces)

    def get_x_coordinate(self):
        return self.turtle.xcor()

    def get_turtle_color(self):
        return self.turtle.pencolor()

    # def move_backwards(self):
    #     self.turtle.backward(50)
    #
    # def turn_counter_clockwise(self):
    #     self.turtle.left(10)
    #
    # def turn_clockwise(self):
    #     self.turtle.right(10)
    #
    # def move_circular(self):
    #     self.turtle.circle(radius=100,extent=10)
    #
    # def clear_screen(self):
    #     self.turtle.clear()
    #     self.turtle.teleport(x=0,y=0)
    #     self.turtle.setheading(0)
    #     self.turtle.tiltangle(0)
    #
    # def screen_listen(self):
    #     self.screen.listen()
    #
    # def screen_on_key(self):
    #     self.screen.onkey(key="w",fun=self.move_forwards)
    #     self.screen.onkey(key="s",fun=self.move_backwards)
    #     self.screen.onkey(key="a", fun=self.turn_clockwise)
    #     self.screen.onkey(key="d",fun=self.turn_counter_clockwise)
    #     self.screen.onkey(key="e",fun=self.move_circular)
    #     self.screen.onkey(key="c",fun=self.clear_screen)

