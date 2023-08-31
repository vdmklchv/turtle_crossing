import turtle
from player import Player
from scoreboard import Scoreboard
import time

turtle.setup(600, 600)
turtle.title("Turtle Crossing")
turtle.bgcolor("gray")
turtle.tracer(0)

player = Player()
sb = Scoreboard(player.level)

GAME_ON = True

turtle.listen()
turtle.onkey(player.go_up, "w")

while GAME_ON:
    time.sleep(0.05)
    turtle.update()

    if player.has_reached_end():
        player.update_level()
        player.to_start_position()
        sb.update_score(player.level)

turtle.mainloop()
