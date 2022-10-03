import turtle

window = turtle.Screen()
window.bgcolor("coral1")
window.title("A and B")

a = turtle.Turtle()
a.color("green")
a.pensize(5)

b = turtle.Turtle()
b.color("blue")
b.pensize(5)

a.forward(10)
a.left(50)
a.forward(100)
a.left(50)

b.forward(10)
b.right(50)
b.forward(100)
b.right(50)

window.mainloop()