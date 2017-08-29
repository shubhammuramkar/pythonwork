detail = {}
class User():
	def describe_user(self,first_name,last_name,middle = '',**info):
		if middle:
			full = first_name + " " + middle + " " + last_name
		else:
			full = first_name + " " + last_name
		print("Full Name is " + full.title())
		for key,value in info.items():
			detail[key.title()] = value.title()
		return detail
de = User()
l = de.describe_user("shubham","rock",locate = "India",tracel = "U.S.A")
print(l)


v = de.describe_user("shubham","rock","cool",locate = "India",tracel = "U.S.A")
print(v)
