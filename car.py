import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        self.cars = []

    def create(self):
        car = Turtle(shape='square')
        car.penup()
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.speed(1)
        color = random.choice(COLORS)
        car.color(color)

        y = random.randint(-250, 250)
        car.goto(310, y)
        self.cars.append(car)

    def move(self):
        for car in self.cars:
            x = car.pos()[0] - 5
            car.goto(x, car.pos()[1])

