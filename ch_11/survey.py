class AnonymousSurvey():
	def __init__(self,q):
		self.q = q
		self.reponse = []
	def show_question(self):
		print(self.q)
	def reponse1(self,new_reponse):
		self.reponse.append(new_reponse)
	def show_result(self):
		print("------Result-------")
		for lan in self.reponse:
			print("-" + lan)

# question = "What language did you first learn to speak?"
# my_survey = AnonymousSurvey(question)
# my_survey.show_question()