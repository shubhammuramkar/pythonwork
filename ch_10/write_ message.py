# filename = 'ch_10/programming.txt'
# with open(filename, 'w') as file_object:
# 	file_object.write("I love programming.\n" + str(int(10)) + "\n")
# 	file_object.write("I love creating new games.\n")



filename = 'ch_10/text_file/programming.txt'
with open(filename, 'a') as file_object:
	file_object.write("I also love finding meaning in large datasets.\n")
	file_object.write("I love creating apps that can run in a browser.\n")




