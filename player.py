from turtle import Turtle


class Player(Turtle):
    """Player class"""
    def __init__(self) -> None:
        super().__init__("turtle")
        self.level = 1
        self.penup()
        self.speed("fastest")
        self.setheading(90)
        self.setpos(0, -280)

    def go_up(self) -> None:
        """Moves turtle up"""
        new_y_cor = self.ycor() + 10
        self.setpos(0, new_y_cor)

