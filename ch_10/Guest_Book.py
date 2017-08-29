while True:
	prompt = input("Enter your name : ")
	location = input("Enter where you live :")
	file = 'ch_10/text_file/guest.txt'
	with open(file,'a') as data:
		data.write(prompt.title() + "'s live in "  + location.title() + "\n")
	re = input("Press Enter to continue and 'q' to exit")
	if re == "q":
		break



