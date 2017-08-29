message = "I love python"
base_mess = "I love swift"
def make_shirt(mess,base,size = "large"):
	if size == "large" or size == "medium":
		print(mess)
	else :
		print(base)

make_shirt(message,base_mess,"small")
make_shirt(message,base_mess)
