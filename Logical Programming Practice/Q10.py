import turtle
gimmicks = turtle.Screen()
gimmicks.bgcolor("black")
gimmicks.title("Bouncing ball")

ball = turtle.Turtle()
ball.shape("circle")
ball.color("yellow")
ball.penup()
ball.speed(0)
ball.goto(0,200)
ball.dy = 0

g = 0.1

while True:
    ball.dy -= g
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() < -300:
        ball.dy *= -1
        