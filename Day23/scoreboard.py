from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-280, 250)
        self.level = 0
        self.level_update()
        self.hideturtle()

    def level_update(self):
        self.clear()
        self.write(f"Level: {self.level}", font=FONT)

    def level_increase(self):
        self.level += 1
        self.level_update()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER",align="center", font=FONT)



