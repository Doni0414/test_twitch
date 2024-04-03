import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class PersonalInformation:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.input_name_selector = (By.CSS_SELECTOR, 'input[name="client_name"]')
        self.button_save_selector = (By.CSS_SELECTOR, 'input[value="Сохранить"]')
        self.button_personalis_slctr = (By.XPATH,'(//a[@href="https://www.flip.kz/user?personalis"])[1]/span')

    def send_name(self, name: str):
        input_name = self.find_element(self.input_name_selector)
        input_name.send_keys(name)

    def delete_name(self):
        input_name = self.find_element(self.input_name_selector)
        input_name.clear()

    def click_save_button(self):
        button_save = self.find_element(self.button_save_selector)
        button_save.click()

    def get_name(self) -> str:
        button_personalis = self.find_element(self.button_personalis_slctr)
        return button_personalis.text


    def find_element(self, slctr):
        return self.driver.find_element(slctr[0], slctr[1])
