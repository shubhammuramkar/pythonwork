mess = """ Hello {name} your size  is  """
rep  = """ I am {repo} """

def make_shirt(size,message,name,rep):
	print(mess.format(name = name) + str(size))
	print("Your response is " + rep.format(repo = "boss".title()) )
make_shirt(34,mess,"shubham",rep)