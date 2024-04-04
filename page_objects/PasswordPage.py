from selenium import webdriver
from selenium.webdriver.common.by import By

class PasswordPage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.input_old_password_slctr = (By.XPATH, "//input[@name='old_password']")
        self.input_new_password_slctr = (By.XPATH, "//input[@name='new_password']")
        self.input_retry_password_slctr = (By.XPATH, "//input[@name='retry_password']")
        self.button_save_slctr = (By.XPATH, "//input[@value='Сохранить']")
        self.password_confirmation_slctr = (By.XPATH, "//div[contains(@class, 'mess')]")

    def send_old_password(self, password: str):
        self.find_element(self.input_old_password_slctr).send_keys(password)

    def send_new_password(self, password: str):
        self.find_element(self.input_new_password_slctr).send_keys(password)

    def send_retry_password(self, password: str):
        self.find_element(self.input_retry_password_slctr).send_keys(password)

    def find_element(self, slctr):
        return self.driver.find_element(slctr[0], slctr[1])

    def click_save(self):
        self.find_element(self.button_save_slctr).click()

    def is_password_successfully_changed(self):
        try:
            message = self.find_element(self.password_confirmation_slctr).text
            return message == 'Пароль успешно изменен'
        except:
            return False