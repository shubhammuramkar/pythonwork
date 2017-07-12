while True:
	prompt = input("Enter your name : ")
	response = input("why you like programming :")
	file = 'ch_10/text_file/response.txt'
	with open(file,'a') as data:
		data.write(prompt.title() + "'s response is "  + response + "\n")
	re = input("Press Enter to continue and 'q' to exit")
	if re == "q":
		break