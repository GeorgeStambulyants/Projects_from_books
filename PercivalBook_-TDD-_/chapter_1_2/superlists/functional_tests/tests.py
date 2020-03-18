from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewVisitorTest(LiveServerTestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()
    
    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])
    
    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edit heard about new cool applications with todo-lists

        # She decides check out the home page ot the application
        self.browser.get(self.live_server_url)

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

        self.check_for_row_in_list_table('1: Buy fruits')

        # The text fields is still on page ready to another input
        # Edit enters 'Buy vegitables'
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy vegetables')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        
        # Page refreshes again and now there are two elements in the list
        self.check_for_row_in_list_table('1: Buy fruits')
        self.check_for_row_in_list_table('2: Buy vegetables')
        # Edit is interested if the site will remember her todo-list
        # Hey, now she sees that our site generated for her unique URL - there
        # is a little message on the page with this information
        self.fail('Finish the test!')
        # She goes to that URL and her list is there

        # Edit is satisfied now and she goes to bed


if __name__ == "__main__":
    unittest.main(warnings='ignore')
