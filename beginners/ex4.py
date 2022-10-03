import turtle

window = turtle.Screen()

background_color = input("Insert the desired color for the background: ")
window.bgcolor(background_color)
window.title("Turtle program")
turtle_name = turtle.Turtle()

turtle_color = input("Insert the desired color for the turtle")
turtle_name.color(turtle_color)
turtle_pensize = int(input("Insert the size of the pen for the turtle"))
turtle_name.pensize(turtle_pensize)
turtle_name.forward(50)
turtle_name.left(90)
turtle_name.forward(50)

window.mainloop()
