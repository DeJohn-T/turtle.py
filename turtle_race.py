import turtle
import random

deejay = turtle.Turtle()
deejay.shape("turtle")
deejay.color("purple")

spongebob = turtle.Turtle()
spongebob.shape("turtle")
spongebob.color("yellow")



deejay.penup()
deejay.left(100)
deejay.goto(0,200)
deejay.pendown()
deejay.goto(-200,200)
deejay.goto(200,200)
deejay.left(170)

spongebob.penup()
spongebob.left(100)
spongebob.goto(0,200)
spongebob.pendown()
deejay.goto(200,200)
deejay.left(170)



turtle.mainloop()