import time

from selenium import webdriver
from selenium.webdriver.common.by import By

class PersonalInformation:
    def __init__(self, driver):
        self.driver = driver

class MainPage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.button_signin_slctr = (By.XPATH, '//span[text()="Войти"]')
        self.button_toggle_email_slctr = (By.XPATH, '(//a[@class="enter-with-password"])[1]')
        self.input_email_slctr = (By.ID, 'username-pass')
        self.input_password_slctr = (By.ID, 'password')
        self.button_login_slctr = (By.XPATH, '(//input[@value="Войти"])[2]')
        self.button_personalis_slctr = (By.XPATH, '(//a[@href="https://www.flip.kz/user?personalis"])[1]')
    def click_signin_button(self):
        button_signin = self.find_element(self.button_signin_slctr)
        button_signin.click()

    def toggle_email(self):
        button_toggle_email = self.find_element(self.button_toggle_email_slctr)
        button_toggle_email.click()

    def send_email(self, email: str):
        input_email = self.find_element(self.input_email_slctr)
        input_email.send_keys(email)

    def send_password(self, password: str):
        input_password = self.find_element(self.input_password_slctr)
        input_password.send_keys(password)

    def click_login(self):
        button_login = self.find_element(self.button_login_slctr)
        button_login.click()

    def find_element(self, slctr):
        return self.driver.find_element(slctr[0], slctr[1])

    def click_personalis(self) -> PersonalInformation:
        button_personalis = self.find_element(self.button_personalis_slctr)
        button_personalis.click()
        return PersonalInformation(self.driver)

