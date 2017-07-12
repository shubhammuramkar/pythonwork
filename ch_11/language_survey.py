from survey import AnonymousSurvey
question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)
my_survey.show_question()
print("Enter q to quit \n")
while True:
	re  = input("Enter language ")
	if re == 'q':
		break
	my_survey.reponse1(re)
print("\nThank you to everyone who participated in the survey!")
my_survey.show_result()