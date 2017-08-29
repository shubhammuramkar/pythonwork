detail = {}
class User():
	def __init__(self,first_name,last_name,middle = '',**info):
		self.first_name = first_name
		self.last_name = last_name
		self.login_attempts = 0
		if middle:
			full = self.first_name + " " + middle + " " + self.last_name
		else:
			full = self.first_name + " " + self.last_name
		print("Full Name is " + full.title())
		for key,value in info.items():
			detail[key.title()] = value.title()
		print(detail)


	def increment_login_attempts(self):
		self.login_attempts += 1
		return self.login_attempts

	def reset_login_attempts(self):
		self.login_attempts = 0
		return self.login_attempts


l = User("shubham","boss",locate = "bhopal",tracel = "U.S.A")
# q = l.increment_login_attempts()
# print(q)
# t = l.increment_login_attempts()
# print(t)
# re = l.reset_login_attempts()
# print(re)

t = l.increment_login_attempts()
print(t)



