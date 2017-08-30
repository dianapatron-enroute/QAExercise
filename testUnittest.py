import unittest
from selenium import webdriver
import time

class testUnittest(unittest.TestCase):


    def setUp(self):
           self.browser = webdriver.Firefox()
    def testWindow(self):
            driver = self.browser
            driver.get('https://misterneutron.com/videoTag/index.html')
            driver.set_window_position(1450,700,windowHandle='current' )
            time.sleep(15)
            driver.set_window_position(0, 0, windowHandle='current')
            time.sleep(15)
    def tearDown(self):
            self.browser.quit()

if __name__ == '__main__':
    unittest.main()