import unittest
from city_functions import world

class city_Test(unittest.TestCase):
	def test(self):
		tested = world("Santiago","Chile")
		self.assertEqual(tested,"Santiago, Chile")

	def test_city_country(self):
		tested = world("Santiago","Chile")
		print(tested)

	def test_city_country_population(self):
		tested = world("Santiago","Chile",5000000)
		self.assertEqual(tested,"Santiago, Chile-5000000")


unittest.main()
