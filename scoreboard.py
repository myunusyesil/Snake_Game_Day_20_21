from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Arial', 12, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(0, 260)
        self.high_score = self.read_high_score()
        self.score = 0
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score:  {self.high_score} ", align=ALIGNMENT, move=False, font=FONT)

    def increase_score(self):
        self.score += 1
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_high_score()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, move=False, font=FONT)

    def reset_score(self):
        self.score = 0
        self.update_scoreboard()

    def write_high_score(self):
        with open("data.txt", mode='w') as file:
            file.write(str(self.high_score))

    def read_high_score(self):
        with open("data.txt") as file:
           return int(file.read())
