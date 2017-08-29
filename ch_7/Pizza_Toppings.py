mes = "Enter a series of pizza toppings"
mes += "\nEnter a 'quit' value : "
message = ""
while message != "quit":
	message = input(mes)
	if message == "quit":
		break
	else:
		print("you’ll add "+ message +" topping to your pizza.")