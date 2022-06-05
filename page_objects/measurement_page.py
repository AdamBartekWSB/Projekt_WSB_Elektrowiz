#Selectors, variables and methods needed for testing Measurement page (from Left sidebar)-> test_add_delete_measurement.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

class Variables():
    #POWERSTATION FORM VARIABLES
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
    #GENERATOR FORM VARIABLES
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
    #Measurement Page Variables
    measurement_date = "2020-02-02"
