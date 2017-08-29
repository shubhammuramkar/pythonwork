active = True
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while active:
	message = input(prompt)
	if message == "quit":
		# print(message)
		# active = False
		break
	else:
		print(message)
		# active = False
