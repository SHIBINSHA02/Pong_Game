import turtle
from paddle import Paddle
import time
from ball import Ball
from bountaryd import Boundary
screen = turtle.Screen()
screen.title("Pong Game")
screen.bgcolor("black")
screen.setup(width= 800, height= 600)
def bound():
    b1=Boundary(390,0)
    b2=Boundary(-390,0)
    b3=Boundary(0,290)
    b3.setheading(90)
    b4=Boundary(0,-290)
    b4.setheading(90)





screen.tracer(0)
rp=Paddle(1)
lp=Paddle(-1)
b=Ball()
game_is_on =True
screen.listen()

              
screen.onkeypress(rp.go_up,"Up")
screen.onkeypress(rp.go_down,"Down")
screen.onkeypress(lp.go_up,"w")
screen.onkeypress(lp.go_down,"s")
bound()
while game_is_on:
    screen.update()
    time.sleep(0.05)
    b.move()
    b.collision()
    b.paddlec(rp)
    b.paddlec(lp)
       







screen.exitonclick()