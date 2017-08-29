file = "ch_10//text_file/Learning_python.txt"
with open(file) as data:
	content = data.read()
	print(content.replace("Python","C"))    ## This will replace PYTHON with C

