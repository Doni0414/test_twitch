import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class PersonalInformation:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.input_name_selector = (By.CSS_SELECTOR, 'input[value="client_name"]')
        self.button_save_selector = (By.CSS_SELECTOR, 'input[value="Сохранить"]')

    def send_name(self, name: str):
        input_name = self.driver.find_element(self.input_name_selector[0], self.input_name_selector[1])
        input_name.send_keys(name)

    def delete_name(self):
        input_name = self.driver.find_element(self.input_name_selector[0], self.input_name_selector[1])
        input_name.clear()

    def click_save_button(self):
        button_save = self.driver.find_element(self.button_save_selector[0], self.button_save_selector[1])
        button_save.click()
