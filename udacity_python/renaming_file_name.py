import os

def rename_file():
	# get the file name from a folder
	file_list = os.listdir("/Users/cool/Documents/python_work/udacity_python/im")
	#print(file_list)
	remove_digit = str.maketrans('','','0123456789')
	saved_path  = os.getcwd()
	#print("Current working directory " + saved_path)
	os.chdir("/Users/cool/Documents/python_work/udacity_python/im")
	for name in file_list:
		print("Old name " + name)
		print("New name " + name.translate(remove_digit))
		os.rename(name,name.translate(remove_digit))
	os.chdir(saved_path)

rename_file()

# l = "23esdc"
# remove_digit = str.maketrans('','','0123456789')
# re = l.translate(remove_digit)
# print(re)