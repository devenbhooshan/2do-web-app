from selenium import webdriver
import unittest
class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser=webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):	
		self.browser.quit()
	def test_can_start_a_list_and_retrieve_it_later(self):
		# Guru opens the homepage of To Do app
		self.browser.get("http://localhost:8000")
		# He checks the page title
		self.assertIn('To-Do', self.browser.title)  #5
		self.fail('Finish the test!')

		
if __name__ == '__main__':
	unittest.main(warnings='ignore')