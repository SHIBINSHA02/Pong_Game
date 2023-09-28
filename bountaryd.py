from turtle import Turtle
class Boundary(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=60)
        self.goto(x,y)