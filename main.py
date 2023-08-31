import turtle
from player import Player
from scoreboard import Scoreboard
import time
import random
from car import Car


turtle.setup(600, 600)
turtle.title("Turtle Crossing")
turtle.bgcolor("gray")
turtle.tracer(0)

player = Player()
sb = Scoreboard(player.level)

GAME_ON = True

turtle.listen()
turtle.onkeypress(player.go_up, "w")

cars = []


def move_cars():
    for car in cars:
        car.move()
        if car.xcor() <= -280:
            cars.remove(car)
            car.hideturtle()


while GAME_ON:
    time.sleep(0.1)
    turtle.update()
    random_int = random.randint(0, 100)
    if random_int <= 20:
        cars.append(Car())
    move_cars()

    if player.has_reached_end():
        player.update_level()
        player.to_start_position()
        sb.update_score(player.level)

    print(len(cars))

turtle.mainloop()
