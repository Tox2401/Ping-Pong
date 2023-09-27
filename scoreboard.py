from turtle import Turtle

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.p1Score = 0
        self.p2Score = 0
        self.update()

    
    def pointForP1(self):
        self.p1Score += 1
        
    def pointForP2(self):
        self.p2Score += 1       
        
    def update(self):
        self.clear()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(300, 275)
        self.write(f"Player 1: {self.p1Score}", False, "center", ("Arial", 12, "bold"))
        self.goto(-300, 275)
        self.write(f"Player 2: {self.p2Score}", False, "center", ("Arial", 12, "bold"))
        
    def p1Victory(self):
        self.goto(0, 0)
        self.write(f"Player 1 has won!", False, "center", ("Arial", 24, "bold"))
    
    def p2Victory(self):
        self.goto(0, 0)
        self.write(f"Player 2 has won!", False, "center", ("Arial", 24, "bold"))