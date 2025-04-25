from turtle import Turtle
FONT = ("Courier", 20, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.current_level = 1
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-220, 260)
        self.write(arg=f"Level: {self.current_level}", align="center", font=FONT)
        self.current_level += 1

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"GAME OVER!", align="center", font=FONT)