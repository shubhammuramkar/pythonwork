import unittest
from survey import AnonymousSurvey

class Test(unittest.TestCase):
	def test_store(self):
		question = "What language did you first learn to speak?"
		my_survey = AnonymousSurvey(question)
		responses = ['English', 'Spanish', 'Mandarin']
        for response in responses:
        	my_survey.reponse1(response)
        for response in responses:
        	self.assertIn(response,my_survey.reponse)

unittest.main()