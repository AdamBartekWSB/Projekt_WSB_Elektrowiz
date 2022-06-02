from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep

class Variables():
    usrlogin = "achybicki"
    usrpasswd = "qwertyuiop"

class UserMenagement():
    Login = "login"
    Password = "password"
    LoginBTN = "Login"
    Administration = "Panel administracyjny"

    def log_in(self):
        driver = self.driver
        driver.find_element(By.NAME, UserMenagement.Login).send_keys(Variables.usrlogin)
        driver.find_element(By.ID, UserMenagement.Password).send_keys(Variables.usrpasswd)
        driver.find_element(By.NAME, UserMenagement.LoginBTN).click()

    def administration_page(self):
        driver = self.driver
        driver.find_element(By.LINK_TEXT, UserMenagement.Administration).click()







