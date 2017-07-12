
# print(5/0)


# try:
# 	print(5/0)
# except ZeroDivisionError:
# 	print("You can't divide by zero!")



print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
	first_no = input("First No. : ")
	if first_no == "q":
		break
	second_no = input("Second No : ")
	if second_no == "q":
		break
	try:
		answer = int(first_no)/int(second_no)
	except ZeroDivisionError:
		print("You can;t divide by 0!")
	else:
		print(answer)
