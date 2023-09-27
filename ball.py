from turtle import Turtle
import random

class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.setheading(random.randint(0, 360))
        
    def move(self):
        self.forward(20)
    
    def moveUp(self):
        if self.heading() < 90 or self.heading() > 270:
            self.setheading(45)
        else:
            self.setheading(135)
            
    def moveDown(self):
        if self.heading() > 90 and self.heading() < 270:
            self.setheading(225)
        else:
            self.setheading(315)
    
    def reverse(self):
        newHeading = self.heading() + random.randint(125, 225)
        if newHeading >= 360:
            newHeading = newHeading - 360
        self.setheading(newHeading)
        
    def resetball(self):
        self.goto(0, 0)