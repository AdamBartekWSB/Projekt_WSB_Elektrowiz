from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep

class Variables():
    usrlogin = "achybicki"
    usrpasswd = "qwertyuiop"
    newusrLogin = "jkowalski"
    newusrPsswd = "1234abcd"
    newusrName = "Jan"
    newuserLastname = "Kowalski"
    newusrEmail = "jkowalski@test.com"
    company = "Niedzica"
    usractive = "TAK"
    usrstatus = "zweryfikowane"

class UserMenagement():
    Login = "login"
    Password = "password"
    LoginBTN = "Login"
    Administration = "Panel administracyjny"
    Users = "//a[@href='users.php']"
    NewUserAddBtn = "//img[@data-target='#user_add']"
    NewUserLoginInput = "user_login"
    NewUserPasswdInput = "user_password"
    NewUserNameInput = "user_name"
    NewUserLastNameInput = "user_lastname"
    NewUserCompanySelect = "user_affiliation"
    NewUserEmail = "user_email"
    NewUserActivation = "user_active"
    NewUserStatus = "user_status"
    SaveBtn = "submit"
    NewUserMsg = "//div[@class='message_box' and text()='Konto zostało stworzone']"
    CloseBtn = "//td//button[text()='Zamknij']"
    NewUserLogin = "//table[@id='user_list']//td[text()='" + Variables.newusrLogin + "']"
    DeleteBtn = "//tr/td[text()='" + Variables.newusrLogin + "']/following-sibling::td/img[@src='images/delete.png']"

    def log_in(self):
        driver = self.driver
        driver.find_element(By.NAME, UserMenagement.Login).send_keys(Variables.usrlogin)
        driver.find_element(By.ID, UserMenagement.Password).send_keys(Variables.usrpasswd)
        driver.find_element(By.NAME, UserMenagement.LoginBTN).click()

    def administration_page(self):
        driver = self.driver
        driver.find_element(By.LINK_TEXT, UserMenagement.Administration).click()

    def users_page(self):
        driver = self.driver
        driver.find_element(By.XPATH, UserMenagement.Users).click()

    def create_new_user(self):
        driver = self.driver
        driver.find_element(By.XPATH, UserMenagement.NewUserAddBtn).click()
        driver.find_element(By.ID, UserMenagement.NewUserLoginInput).send_keys(Variables.newusrLogin)
        driver.find_element(By.ID, UserMenagement.NewUserPasswdInput).send_keys(Variables.newusrPsswd)
        driver.find_element(By.ID, UserMenagement.NewUserNameInput).send_keys(Variables.newusrName)
        driver.find_element(By.ID, UserMenagement.NewUserLastNameInput).send_keys(Variables.newuserLastname)
        company_select = Select(driver.find_element(By.ID, UserMenagement.NewUserCompanySelect))
        company_select.select_by_visible_text(Variables.company)
        driver.find_element(By.ID, UserMenagement.NewUserEmail).send_keys(Variables.newusrEmail)
        user_active_select = Select(driver.find_element(By.ID, UserMenagement.NewUserActivation))
        user_active_select.select_by_visible_text(Variables.usractive)
        user_status_select = Select(driver.find_element(By.ID, UserMenagement.NewUserStatus))
        user_status_select.select_by_visible_text(Variables.usrstatus)
        driver.find_element(By.ID, UserMenagement.SaveBtn).click()
        sleep(2)

    def check_new_user_msg(self):
        driver = self.driver
        new_user_msg = driver.find_element(By.XPATH, UserMenagement.NewUserMsg)
        self.assertEqual("Konto zostało stworzone", new_user_msg.text, "There is no message about adding a user")

        driver.find_element(By.XPATH, UserMenagement.CloseBtn).click()

    def check_new_user(self):
        driver = self.driver
        new_user_check = driver.find_element(By.XPATH, UserMenagement.NewUserLogin)
        self.assertEqual(Variables.newusrLogin, new_user_check.text, "There is no new user")

    def delete_user(self):
        driver = self.driver
        driver.find_element(By.XPATH, UserMenagement.DeleteBtn).click()







