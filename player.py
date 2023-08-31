from turtle import Turtle
START_POSITION = (0, -280)


class Player(Turtle):
    """Player class"""
    def __init__(self) -> None:
        super().__init__("turtle")
        self.level = 1
        self.penup()
        self.speed("fastest")
        self.setheading(90)
        self.setpos(START_POSITION)

    def go_up(self) -> None:
        """Moves turtle up"""
        new_y_cor = self.ycor() + 10
        self.goto(0, new_y_cor)

    def update_level(self) -> None:
        """Updates player level by 1"""
        self.level += 1

    def has_reached_end(self) -> bool:
        """Returns true if player has reached the other side of the road, false otherwise"""
        return self.ycor() > 280

    def to_start_position(self) -> None:
        """Reset player to initial position on screen"""
        self.setpos(START_POSITION)


