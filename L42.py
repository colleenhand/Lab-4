#the author's names are: Colleen and Anna
import turtle
jack = turtle.Turtle()
jack.color("yellow")

for side in range(4):
    if side == 3:
        jack.color("green")
    if side == 1:
        jack.color("magenta")
    jack.forward(100)
    jack.right(90)
