import turtle

def make_square():
	window = turtle.Screen()
	window.bgcolor("red")

	brad = turtle.Turtle()
	brad.color("yellow")
	brad.shape("turtle")
	brad.speed(2)

	for turn in range(0,4):
		brad.forward(100)
		brad.right(90)



	angie = turtle.Turtle()
	angie.color("blue")
	angie.shape("arrow")
	angie.circle(100)


	caty = turtle.Turtle()
	caty.shape("arrow")
	caty.color("green")
	for t in range(0,3):
		caty.forward(80)
		caty.right(120)



	star = turtle.Turtle()
	star.shape("arrow")
	star.color("black")
	for i in range(0,5):
		star.forward(150)
		star.right(144)




	window.exitonclick()


make_square()

