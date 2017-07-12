## this check valid input should be give by user

try:
	first_no = input("Enter two number ")
	l = int(first_no)
	second_no = input("Enter another number ")
	m = int(second_no)
	sum_1 = l + m
# c = int(sum_1)
except ValueError:
	print("Invalid Input! Try again")
else:
	print("Sum of " + str(first_no) + " and " + str(second_no) + " = " + str(sum_1))
