from turtle import Turtle

class MiddleLine(Turtle):
    
    def __init__(self):
        super().__init__()
        self.middleLine()
    
    def middleLine(self):
        self.color("white")
        self.hideturtle()
        self.penup()
        self.width(5)
        self.goto(0, 275)
        self.setheading(270)
        for i in range(0, 4):
            self.pendown()
            self.forward(100)
            self.penup()
            self.forward(50)
