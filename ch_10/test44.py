# with open('ch_10/text_file/pi_digits.txt') as file_object:   ##with open('file_location/filename.txt') as file_object:
# 	content = file_object.read()
# 	print(content.rstrip())

# with open('pi_digits.txt') as file_object:   ## it work if file in  same directory
#     contents = file_object.read()
#     print(contents.rstrip())


filename = 'ch_10/text_file/pi_digits.txt'
with open(filename) as file_object:
	for line in file_object:
		print(line.rstrip())




# filename = 'ch_10/text_file/pi_digits.txt'
# with open(filename) as file_object:
# 	lines = file_object.readlines()  ##the readlines() method takes each line from the file and stores it in a list. This list is then stored in lines, which we can continue to work with after the with block ends
# #print(lines)                            ## lines become a list
# for line in lines:
# 	print(line.rstrip())















