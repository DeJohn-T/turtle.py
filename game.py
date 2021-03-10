import turtle

rafa = turtle.Turtle()
rafa.shape('turtle')
rafa.color('pink')

rafa.begin_fill()

rafa.forward(200)
rafa.left(90)

rafa.forward(200)
rafa.left(90)

rafa.forward(200)
rafa.left(90)

rafa.foward(200)
rafa.left(90)

rafa.end_fill()

rafa.penup()
rafa.goto(-350, 150)
rafa.pendown

rafa.color('green')
rafa.begin_fill()
for i in range(4):
    rafa.forward(100)
    rafa.left(90)
rafa.end_fill()

rafa.penup()
rafa.goto(-200,-200)


rafa.write("MOM, font=('Arial', 48, 'italic'))
rafa.hideturtle()


turtle.mainloop()