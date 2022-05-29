import time
from scoreboard import Score
from turtle import Screen
from player import Player
from car import CarManager

screen = Screen()
screen.setup(600,600)

def screen_update():
    screen.tracer(0)
    screen.listen()
    screen.onkeypress(player.move_up, 'Up')

player = Player()
screen_update()
score = Score()
game_on = True
loop = 0
car = CarManager()
while game_on:
    time.sleep(0.1)
    screen.update()
    car.move()

    if loop % 6 == 0:
        car.create()

    if player.ycor() == 290:
        screen.clear()
        player.goto(0, -280)
        screen_update()
        score.update()
        car = CarManager()

    loop += 1


screen.exitonclick()