from selenium import webdriver
import unittest


class MyTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.elektrowiz.pl/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)


    def testCreateNewUser(self):


    def tearDown(self):
        self.driver.quit()