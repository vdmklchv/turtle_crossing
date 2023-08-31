import turtle
from player import Player
from scoreboard import Scoreboard

turtle.setup(600, 600)
turtle.bgcolor("gray")

player = Player()
sb = Scoreboard(player.level)

turtle.listen()
turtle.onkey(player.go_up, "w")
turtle.mainloop()
