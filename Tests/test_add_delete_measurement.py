from selenium import webdriver
import unittest
from page_objects.measurement_page import Measurement
from time import sleep

class MyTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.elektrowiz.pl/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def test01_CreatePowerStation(self):
        Measurement.log_in(self)
        Measurement.pre_check_powerstation(self)
        sleep(2)
        Measurement.create_powerstation(self)
        Measurement.check_powerstation(self)
        sleep(4)

    def test02_CreateGenerator(self):
        Measurement.log_in(self)
        Measurement.create_generator(self)
        sleep(2)
        Measurement.check_generator(self)

    def test03_CreateMeasurement(self):
        Measurement.log_in(self)
        Measurement.create_measurement(self)
        sleep(2)
        Measurement.check_measurement(self)
        sleep(2)

    def test04_ClearTestCase(self):
        Measurement.log_in(self)
        Measurement.delete_measurement(self)
        sleep(2)
        Measurement.delete_generator(self)
        sleep(2)
        Measurement.delete_powerstation(self)
        sleep(2)
        Measurement.check_powerstation_after_cleaning(self)

    def tearDown(self):
        self.driver.quit()
