from selenium import webdriver
import unittest
from page_objects.administration_page import UserMenagement

class MyTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.elektrowiz.pl/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def testCreateNewUser(self):

        UserMenagement.log_in(self)
        UserMenagement.administration_page(self)
        UserMenagement.users_page(self)
        UserMenagement.create_new_user(self)

        UserMenagement.check_new_user_msg(self)
        UserMenagement.check_new_user(self)

        UserMenagement.delete_user(self)

        UserMenagement.check_del_user_msg(self)
        UserMenagement.check_del_user(self)

    def tearDown(self):
        self.driver.quit()