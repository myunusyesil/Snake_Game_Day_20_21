from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0

class Snake:
    def __init__(self):
        # Starting positions of each segment, and they will create the whole snake together
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            # We are moving the 3rd place to the 2nd place, and 2nd place to the 1st and
            # move the old first square to forward
            # Last segment become the position of second to the last segment
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def turn_east(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def turn_north(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def turn_west(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def turn_south(self):
        if self.head.heading != UP:
            self.head.setheading(DOWN)
