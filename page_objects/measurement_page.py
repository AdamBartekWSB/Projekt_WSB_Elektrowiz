#Selectors, variables and methods needed for testing Measurement page (from Left sidebar)-> test_add_delete_measurement.py
from selenium.webdriver.common.by import By
from page_objects.Credentials import Login




class Variables():
    # POWERSTATION FORM VARIABLES
    powerstation_name = "Test Powerstation"
    powerstation_street = "Test street"
    powerstation_street_number = "1"
    powerstation_building_number = "2"
    powerstation_zip_code = "000-01"
    powerstation_country = "Poland"
    powerstation_city = "Poznan"
    powerstation_phone = "000000001"
    powerstation_fax = "123456789"
    powerstation_email = "testmail@gmail.com"
    # GENERATOR FORM VARIABLES
    generator_name = "Testgen1"
    generator_manufacturer = "Testing Company"
    generator_type = "GTH360"
    generator_serialno = "000001"
    generator_year = "2000"
    generator_rated_voltage = "20"
    generator_rated_current = "9000"
    generator_rated_excitation_voltage = "380"
    generator_rated_excitation_current = "1500"
    generator_insulation = "Resin Rich F"
    generator_power_apparent = "380"
    generator_power_real = "360"
    generator_power_reactive = "40"
    generator_cos = "0.85"
    generator_speed = "3000"
    generator_cooling = "hydrogen"
    # Measurement Page Variables
    measurement_date = "2020-02-02"

class Measurement():
    # All selectors used in these methods
    # Find by LINK or Partial LINK
    measurement_page_main = "Pomiary"
    measurement_page_left_sidebar = "Pomiary"
    powerstation_page = "Elektrownie"
    generator_page = "Generatory"
    # Find by  ID
    Login = "login"
    Password = "password"
    LoginBTN = "Login"
    measurement_add_btn = "submit"
    measurement_select_generator_form = "msaddform_generator"
    measurement_select_datepicker = "measurement_date"
    measurement_table = "measurement_table"
    powerstation_name = "powerstation_name"
    powerstation_street = "powerstation_street"
    powerstation_street_number = "powerstation_streetnum"
    powerstation_building_number = "powerstation_localnum"
    powerstation_zip_code = "powerstation_zipcode"
    powerstation_city = "powerstation_city"
    powerstation_select = "genform_powerstation_name"
    generator_name = "genform_generator_name"
    generator_manufacturer = "producer"
    generator_type = "device_type"
    generator_serialno = "manufacture_no"
    generator_year = "manufacture_year"
    generator_rated_voltage = "rated_voltage"
    generator_rated_current = "rated_current"
    generator_rated_excitation_voltage = "excitation_voltage"
    generator_rated_excitation_current = "excitation_current"
    generator_insulation = "insulation_type"
    generator_power_apparent = "generator_power_mva"
    generator_power_real = "generator_power_mw"
    generator_power_reactive = "generator_power_mvar"
    generator_cos = "cos_fi"
    generator_speed = "rotor_speed"
    generator_cooling = "cooling"
    generator_table = "measurement_table"
    # Select country
    powerstation_country = "powerstation_city"
    powerstation_phone = "powerstation_telephone"
    powerstation_fax = "powerstation_fax"
    powerstation_email = "powerstation_email"
    powerstation_add_form_btn = "submit"
    generator_add_form_btn = "submit"
    generator_add_form_submit = "//form[@id='generator_add_form']//input[@id='submit']"
    # Find by XPATH
    powerstation_add_btn = "//img[@data-target='#powerstation_add']"
    powerstation_table = '//div[@id="measurement_right"]'
    generator_add_btn = "//img[@data-target='#generator_add']"
    measurement_select_powerstation_form = "//select[@id='msaddform_powerstation']"
    powerstation_list_check = "//table[@id = 'powerstation_list']//td[text()='" + Variables.powerstation_name + "']"
    powerstation_list_number_testgen = "//table[@id='powerstation_list']//td[text()='" + Variables.powerstation_name + "']/following-sibling::td[3]/img"
    generator_list_number_testgen = "//table[@id='table_generator_list']//td[text()='" + Variables.generator_name + "']/following-sibling::td[3]/img"
    measurement_list_number_testgen = "//table[@id='measurement_table']//td[text()='" + Variables.measurement_date + "']/following-sibling::td[3]/img"

    def log_in(self):
        driver = self.driver
        driver.find_element(By.NAME, Measurement.Login).send_keys(Login.usrlogin)
        driver.find_element(By.ID, Measurement.Password).send_keys(Login.usrpasswd)
        driver.find_element(By.NAME, Measurement.LoginBTN).click()

    def create_powerstation(self):
        driver = self.driver
        driver.implicitly_wait(2)
        driver.get("http://www.elektrowiz.pl/measurements.php?s=powerstation_add")
        driver.find_element(By.XPATH, Measurement.powerstation_add_btn).click()
        driver.find_element(By.ID, Measurement.powerstation_name).send_keys(Variables.powerstation_name)
        driver.find_element(By.ID, Measurement.powerstation_street).send_keys(Variables.powerstation_street)
        driver.find_element(By.ID, Measurement.powerstation_street_number).send_keys(Variables.powerstation_street_number)
        driver.find_element(By.ID, Measurement.powerstation_building_number).send_keys(Variables.powerstation_building_number)
        driver.find_element(By.ID, Measurement.powerstation_zip_code).send_keys(Variables.powerstation_zip_code)
        driver.find_element(By.ID, Measurement.powerstation_city).send_keys(Variables.powerstation_city)
        driver.find_element(By.ID, Measurement.powerstation_phone).send_keys(Variables.powerstation_phone)
        driver.find_element(By.ID, Measurement.powerstation_add_form_btn).click()

    def pre_check_powerstation(self):
        driver = self.driver
        driver.get("http://www.elektrowiz.pl/measurements.php?s=powerstation_add")
        powerstation_table = driver.find_element(By.XPATH, Measurement.powerstation_table)
        powerstation_existing = Variables.powerstation_name in powerstation_table.text
        if powerstation_existing is True:
            print(
                "Na liście znajduje się już elektrownia o nazwie: " + Variables.powerstation_name + "\nPrzystępuję do jej usunięcia...")
            Measurement.delete_powerstation(self)
            print("Elektrownia " + Variables.powerstation_name + " została usunięta. Przechodzę do testu")
        else:
            print(
                "Nie znaleziono elektrowni: " + Variables.powerstation_name + " w bazie danych. \nMożna bezpiecznie kontynuować dodawanie nowej elektrowni testowej...")

