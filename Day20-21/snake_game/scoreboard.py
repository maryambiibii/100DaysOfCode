from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle,):
    def __init__(self):
        super().__init__()
        self.num_hits = 0
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.update_score(self.num_hits)

    def update_score(self, num_hits):
        self.write(f"Score: {self.num_hits}", False, align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.num_hits += 1
        self.write(f"Score: {self.num_hits}", False, align=ALIGNMENT, font=FONT)
        self.hideturtle()


