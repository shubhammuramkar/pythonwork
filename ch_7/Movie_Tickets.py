mes = "What is your age :"
message = ""
while message != "quit":
	age_1 = input(mes)
	age_1 = int(age_1)
	if age_1 < 3:
		print("Your entry fee is Free")
	elif age_1 > 3 and age_1 < 12:
		print("Your entry fee is $" + str(10))
	else :
		print("Your entry fee is $" + str(15))