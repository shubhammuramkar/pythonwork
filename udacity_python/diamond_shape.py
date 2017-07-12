import turtle

def draw_kite(some_turtle):
	for i in range(0,2):
		some_turtle.forward(100)
		some_turtle.right(155)
		some_turtle.forward(100)
		some_turtle.right(25)


def draw_art():
	window = turtle.Screen()
	window.bgcolor("red")
	brad = turtle.Turtle()
	brad.shape("arrow")
	brad.speed(100)
	brad.color("green")
	for j in range(0,80):
		draw_kite(brad)
		brad.right(5)
	brad.right(50)
	brad.forward(150)



	window.exitonclick()

draw_art()