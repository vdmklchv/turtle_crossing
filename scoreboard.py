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
        """Writes player level"""
        self.clear()
        self.write(f"Level: {level}", font=("Verdana", 24, "normal"))

    def game_over(self) -> None:
        """Writes Game Over line in center of the screen"""
        self.goto(-100, 0)
        self.write(f"GAME OVER!", font=("Verdana", 24, "normal"))