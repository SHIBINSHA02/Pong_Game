from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,n) :
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=1 , stretch_wid=5)
        self.goto(n*350,0)

    def go_up(self):
        if self.ycor()<250:
            new_y = self.ycor() +20
            self.sety(new_y)
    def go_down(self):
        if self.ycor()>-250:
            new_y=self.ycor() - 20
            self.sety(new_y)