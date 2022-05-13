import turtle

window = turtle.Screen()
window.title("Pong game Python")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

score_a = 0
score_b = 0

left_paddle = turtle.Turtle()
left_paddle.speed(6)
left_paddle.shape("square")
left_paddle.color("white")
left_paddle.shapesize(stretch_wid=5, stretch_len=1)
left_paddle.penup()
left_paddle.goto(-350, 0)

right_paddle = turtle.Turtle()
right_paddle.speed(2)
right_paddle.shape("square")
right_paddle.color("white")
right_paddle.shapesize(stretch_wid=5, stretch_len=1)
right_paddle.penup()
right_paddle.goto(350, 0)

object = turtle.Turtle()
object.speed(0)
object.shape("square")
object.color("red")
object.penup()
object.goto(0, 0)
object.dx = 0.5
object.dy = 0.5

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))


def left_paddle_up():
    y = left_paddle.ycor()
    y += 20
    left_paddle.sety(y)


def left_paddle_dowindow():
    y = left_paddle.ycor()
    y -= 20
    left_paddle.sety(y)


def right_paddle_up():
    y = right_paddle.ycor()
    y += 20
    right_paddle.sety(y)


def right_paddle_dowindow():
    y = right_paddle.ycor()
    y -= 20
    right_paddle.sety(y)


# Keyboard bindings
window.listen()
window.onkeypress(left_paddle_up, "w")
window.onkeypress(left_paddle_dowindow, "s")
window.onkeypress(right_paddle_up, "Up")
window.onkeypress(right_paddle_dowindow, "Down")

while True:
    window.update()

    object.setx(object.xcor() + object.dx)
    object.sety(object.ycor() + object.dy)

    if object.ycor() > 290:
        object.sety(290)
        object.dy *= -1

    elif object.ycor() < -290:
        object.sety(-290)
        object.dy *= -1

    if object.xcor() > 350:
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        object.goto(0, 0)
        object.dx *= -1

    elif object.xcor() < -350:
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        object.goto(0, 0)
        object.dx *= -1

    if object.xcor() < -340 and left_paddle.ycor() + 50 > object.ycor() > left_paddle.ycor() - 50:
        object.dx *= -1

    elif object.xcor() > 340 and right_paddle.ycor() + 50 > object.ycor() > right_paddle.ycor() - 50:
        object.dx *= -1

    if score_a == 11:
        quit()

    elif score_b == 11:
        quit()
