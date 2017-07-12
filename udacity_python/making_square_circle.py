import turtle

def draw_square(some_turtle):
	for turn in range(0,4):
		some_turtle.forward(100)
		some_turtle.right(90)


def draw_art():
	window = turtle.Screen()
	window.bgcolor("red")
# create a turtle brad  - Draw a square
	brad = turtle.Turtle()
	brad.color("yellow")
	brad.shape("turtle")
	brad.speed(20)
	for i in range(0,37):
		draw_square(brad)
		brad.right(10)
	window.exitonclick()

# create a turtle Angie - Draw a circle
	# angie = turtle.Turtle()
	# angie.color("blue")
	# angie.shape("arrow")
	# angie.circle(100)

draw_art()