## this check valid input should be give by user
while True:
	try:
		first_no = input("Enter two number ")
		l = int(first_no)
		second_no = input("Enter another number ")
		m = int(second_no)
		sum_1 = l + m
	except ValueError:
		print("Invalid Input! Try again")
		l = input("press q to quit and Enter to continue ")
		if l == "q":
			break
	else:
		print("Sum of " + str(first_no) + " and " + str(second_no) + " = " + str(sum_1))
