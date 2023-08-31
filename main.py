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


turtle.listen()
turtle.onkeypress(player.go_up, "w")


cars = []


def move_cars() -> None:
    "Moves all existing cars and removes cars that go out of screen"
    for car in cars:
        car.move()
        if car.xcor() <= -280:
            cars.remove(car)
            car.hideturtle()


GAME_ON = True

while GAME_ON:
    time.sleep(0.3/player.level)  # increase speed through each level
    turtle.update()

    # choose how often to create a new car
    random_int = random.randint(0, 100)
    if random_int <= 20:
        cars.append(Car())

    move_cars()

    for car in cars:
        if player.distance(car) < 15:
            GAME_ON = False
            sb.game_over()

    if player.has_reached_end():
        player.update_level()
        player.to_start_position()
        sb.update_score(player.level)

turtle.mainloop()
