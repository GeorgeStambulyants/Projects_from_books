from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()
    
    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edit heard about new cool applications with todo-lists

        # She decides check out the home page ot the application
        self.browser.get('http://localhost:8000')

        # She sees that the title and the header of the page reference the todo-list
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # She is suggested to enter new element of the list

        # She prints in the text fields 'Buy fruits'

        # When she hits enter button page refreshes and now it has:
        # '1: Buy fruits' in the list

        # The text fields is still on page ready to another input
        # Edit enters 'Buy vegitables'

        # Page refreshesassert 'Django' in browser.title again and now there are two elements in the list

        # Edit is interested if the site will remember her todo-list
        # Hey, now she sees that our site generated for her unique URL - there
        # is a little message on the page with rhis information

        # She goes to that URL and her list is there

        # Edit is satisfied now and she goes to bed


if __name__ == "__main__":
    unittest.main(warnings='ignore')
