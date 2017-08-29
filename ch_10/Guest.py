prompt = input("Enter your name : ")
file = 'ch_10/text_file/guest.txt'
with open(file,'w') as data:
	data.write(prompt)