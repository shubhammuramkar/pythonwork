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




class Admin(User):
	def __init__(self,first_name,last_name,middle='',**info):
		super().__init__(first_name,last_name,middle='',**info)
		self.pre = Privileges()





class Privileges():

	def __init__(self,*privileges ):
		self.privileges = privileges
	def show_privileges(self,*prvileges):
		return prvileges




obj = Admin("shubham","rock",locate = "bhopal",tracel = "U.S.A")
l = obj.pre. show_privileges("can add post", "can delete post", "can ban user")
print(l)



