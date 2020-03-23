from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time
import unittest


MAX_WAIT = 10


class NewVisitorTest(LiveServerTestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()
    
    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)
    
    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith heard about new cool applications with todo-lists

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

        self.wait_for_row_in_list_table('1: Buy fruits')

        # The text fields is still on page ready to another input
        # Edith enters 'Buy vegitables'
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy vegetables')
        inputbox.send_keys(Keys.ENTER)
        
        # Page refreshes again and now there are two elements in the list
        self.wait_for_row_in_list_table('1: Buy fruits')
        self.wait_for_row_in_list_table('2: Buy vegetables')
        # Edith is interested if the site will remember her todo-list
        # Hey, now she sees that our site generated for her unique URL - there
        # is a little message on the page with this information
        ## self.fail('Finish the test!')
        # She goes to that URL and her list is there

        # Edith is satisfied now and she goes to bed

    def test_multiple_users_can_start_lists_at_different_urls(self):
        # Edith starts with a new list
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy fruits')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy fruits')

        # She notices that a list has unique URL
        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, '/lists/.+')

        # Now new user, Francis, visits the site
        
        self.browser.quit()
        self.browser = webdriver.Firefox()
        
        # Francis visits home page. There is no Edith's list
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('But fruits', page_text)
        self.assertNotIn('But vegetables', page_text)

        # Francis starts new list
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')

        # Francis gets unique URL
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)

        # And again, there is no Edith's list here
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy fruits', page_text)
        self.assertIn('Buy milk', page_text)
        
        # Now they both go to sleep


if __name__ == "__main__":
    unittest.main(warnings='ignore')
