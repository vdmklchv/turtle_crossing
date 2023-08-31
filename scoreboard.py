from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, level: int) -> None:
        """Takes in player level, draws it on screen"""
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.write(f"Level: {level}", font=("Verdana", 24, "normal"))

    def update_score(self, level: int) -> None:
        self.clear()
        self.write(f"Level: {level}", font=("Verdana", 24, "normal"))

    def game_over(self):
        self.goto(-100, 0)
        self.write(f"GAME OVER!", font=("Verdana", 24, "normal"))