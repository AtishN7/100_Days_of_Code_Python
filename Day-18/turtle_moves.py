from turtle_attributes import Kasav
import random



class MoveTurtle(Kasav):

    def __init__(self):
        super().__init__()
        self.colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

    def move_paces(self, paces):
        self.turtle.forward(paces)

    def square_move(self, paces, angle):
        for i in range(4):
            self.turtle.right(angle)
            self.turtle.forward(paces)

    def dotted_line(self, line_paces):
        for l in range(10):
            # self.turtle.forward(line_paces)
            # self.turtle.teleport(x=self.turtle.xcor()+line_paces)
            # self.turtle.forward(line_paces)

            self.turtle.forward(line_paces)
            self.turtle.pendown()
            self.turtle.forward(line_paces)
            self.turtle.penup()

    def draw_pattern(self, shape_sides, shape_length):
        i = 3
        while i < shape_sides:
            self.turtle.color(random.choice(self.colours))
            for _ in range(i):
                self.turtle.forward(shape_length)
                angle = 360/i
                self.turtle.right(angle)
            i += 1

    def move_right(self, paces):
        self.turtle.right(90)
        self.turtle.forward(paces)

    def move_left(self, paces):
        self.turtle.left(90)
        self.turtle.forward(paces)

    def random_walk(self, paces):
        self.turtle.width(10)
        movements = [self.turtle.right, self.turtle.left]
        # directions = [0, 90, 180, 270]
        for _ in range(50):
            self.turtle.color(random.choice(self.colours))
            self.turtle.forward(paces)
            random.choice(movements)(90)
            # self.turtle.setheading(random.choice(directions))

