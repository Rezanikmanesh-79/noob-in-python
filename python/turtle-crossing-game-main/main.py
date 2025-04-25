import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Create player
player = Player()

# Control player
screen.listen()
screen.onkeypress(player.move, "Up")

# Instantiate CarManager
car_manager = CarManager()

# Create Scoreboard
score = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()

    # Create and move car
    car_manager.make_car()
    car_manager.move()

    # Detect collision with car
    for car in car_manager.all_cars:
        if player.distance(car) < 21:
            score.game_over()
            game_is_on = False

    # Detect successful crossing and speed up cars
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.increase_speed()
        score.update_scoreboard()


screen.exitonclick()


