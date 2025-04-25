from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 2


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.move_increment = 0

    def make_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))

            random_y = random.randint(-245, 245)
            new_car.goto(310, random_y)

            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE + self.move_increment)

            if car.xcor() < -400:
                car.hideturtle()

    def increase_speed(self):
        self.move_increment += 1



