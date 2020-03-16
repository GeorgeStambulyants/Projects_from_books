from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
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
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # She is suggested to enter new element of the list
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # She prints in the text fields 'Buy fruits'
        inputbox.send_keys('Buy fruits')

        # When she hits enter button page refreshes and now it has:
        # '1: Buy fruits' in the list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy fruits' for row in rows)
        )

        # The text fields is still on page ready to another input
        # Edit enters 'Buy vegitables'
        self.fail('Finish the test!')

        # Page refreshesassert 'Django' in browser.title again and now there are two elements in the list

        # Edit is interested if the site will remember her todo-list
        # Hey, now she sees that our site generated for her unique URL - there
        # is a little message on the page with rhis information

        # She goes to that URL and her list is there

        # Edit is satisfied now and she goes to bed


if __name__ == "__main__":
    unittest.main(warnings='ignore')
