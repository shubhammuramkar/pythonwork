import unittest

from name_function import get_formatted_name

class NameTestCase(unittest.TestCase):
	def test_first_last_name(self):
		fomratted_name = get_formatted_name('janis','joplin')
		self.assertEqual(fomratted_name,'Janis Joplin')

	def test_first_last_middle_name(self):
		fomratted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
		self.assertEqual(fomratted_name,'Wolfgang Amadeus Mozart')



unittest.main()