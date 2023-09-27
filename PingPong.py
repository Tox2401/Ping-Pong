import time
from turtle import Screen
from scoreboard import Scoreboard
from middleLine import MiddleLine
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.title("Ping Pong")
screen.setup(1200, 600)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

p1 = Paddle((580, 0))
p2 = Paddle((-580, 0))

middleLine = MiddleLine()
scoreboard = Scoreboard()

ball = Ball()

screen.onkeypress(p1.moveUp, "Up")
screen.onkeypress(p1.moveDown, "Down")
screen.onkeypress(p2.moveUp, "w")
screen.onkeypress(p2.moveDown, "s")

gameOn = True

while gameOn:
    screen.update()
    time.sleep(0.06)
    ball.move()

    # Paddle bounce
    if p1.distance(ball) < 50 or p2.distance(ball) < 50:
        if ball.xcor() > 550 or ball.xcor() < -550:
            ball.reverse()

    # Edge bounce
    if ball.ycor() > 275:
        ball.moveDown()
    if ball.ycor() < -275:
        ball.moveUp()
        
    if ball.xcor() < -600:
        scoreboard.pointForP1()
        scoreboard.update()
        ball.resetball()
        
    if ball.xcor() > 600:
        scoreboard.pointForP2()
        scoreboard.update()
        ball.resetball()
        
    if scoreboard.p1Score == 5:
        scoreboard.p1Victory()
        gameOn = False
    if scoreboard.p2Score == 5:
        scoreboard.p2Victory()
        gameOn = False

screen.exitonclick()