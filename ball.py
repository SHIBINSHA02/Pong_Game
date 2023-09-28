from turtle import Turtle
from random import Random 
# from score import Score
r=Random()
# s=Score()
class Ball(Turtle):
    def __init__(self):
        super().__init__(shape="circle")
        self.color("white")
        self.penup()
        self.goto(r.randint(-380,380),r.randint(-280,280))
        self.ycord=10
        self.xcord=10

    def move(self):
        x= self.xcor()+ self.xcord
        y=self.ycor() + self.ycord
        self.goto(x,y)
    def ybounce(self):
        self.ycord*=-1
    def xbounce(self):
        self.xcord*=-1
    def collision(self):
        if abs(self.ycor())> 280 :
            self.ybounce()
        if abs(self.xcor()) > 380:
            self.xbounce()
    def paddlec(self,Paddle):
        if self.distance(Paddle) < 50 and abs(self.xcor()) > 320:
            self.xbounce()
        
