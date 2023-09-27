from turtle import Turtle

class Paddle(Turtle):
    
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1, None)
        self.penup()
        self.goto(position)

        
    def moveUp(self):
        newY = self.ycor() + 20
        self.sety(newY)

        
    def moveDown(self):
        newY = self.ycor() - 20
        self.sety(newY)