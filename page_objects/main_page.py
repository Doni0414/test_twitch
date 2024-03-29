import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class MainPage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.sign_up_button_selector = (By.CSS_SELECTOR, 'button[data-a-target="signup-button"]')
        self.email_toggle_button_selector = (By.XPATH, '//div[text()="Use email instead"]')
        self.username_input_selector = (By.ID, 'signup-username')
        self.password_input_selector = (By.ID, 'password-input')
        self.password_input_confirmation_selector = (By.ID, 'password-input-confirmation')
        self.birth_month_selector = (By.CSS_SELECTOR, 'select[data-a-target="birthday-month-select"]')
        self.birth_day_input_selector = (By.CSS_SELECTOR, 'input[placeholder="Day"]')
        self.birth_year_input_selector = (By.CSS_SELECTOR, 'input[placeholder="Year"]')
        self.sign_up_pop_button_selector = (By.CSS_SELECTOR, 'button[data-a-target="passport-signup-button"]')
        self.email_input_selector = (By.ID, 'email-input')
        self.remind_me_later_selector = (By.XPATH, '//div[text()="Remind me later"]')

        self.login_button_selector = (By.CSS_SELECTOR, 'button[data-a-target="login-button"]')
        self.login_input_selector = (By.ID, 'login-username')
        self.login_pop_button_selector = (By.CSS_SELECTOR, 'button[data-a-target="passport-login-button"]')

    def open(self, url):
        self.driver.get(url)

    def click_sign_up_button(self):
        sign_up_button = self.driver.find_element(self.sign_up_button_selector[0], self.sign_up_button_selector[1])
        sign_up_button.click()

    def toggle_email(self):
        toggle_email_button = self.driver.find_element(self.email_toggle_button_selector[0], self.email_toggle_button_selector[1])
        toggle_email_button.click()

    def send_username(self, username: str):
        username_input = self.driver.find_element(self.username_input_selector[0], self.username_input_selector[1])
        username_input.send_keys(username)

    def send_password(self, password: str):
        password_input = self.driver.find_element(self.password_input_selector[0], self.password_input_selector[1])
        for letter in password:
            password_input.send_keys(letter)
            time.sleep(0.2)

    def send_birth_month(self, month: str):
        birth_month_select = Select(self.driver.find_element(self.birth_month_selector[0], self.birth_month_selector[1]))
        birth_month_select.select_by_visible_text(month)

    def send_birth_day(self, day: int):
        birth_day_input = self.driver.find_element(self.birth_day_input_selector[0], self.birth_day_input_selector[1])
        birth_day_input.send_keys(day)

    def send_birth_year(self, year: int):
        birth_year_input = self.driver.find_element(self.birth_year_input_selector[0], self.birth_year_input_selector[1])
        birth_year_input.send_keys(year)

    def send_email(self, email: str):
        email_input = self.driver.find_element(self.email_input_selector[0], self.email_input_selector[1])
        email_input.send_keys(email)

    def click_sign_up_pop_button(self):
        sign_up_pop_button = self.driver.find_element(self.sign_up_pop_button_selector[0], self.sign_up_pop_button_selector[1])
        sign_up_pop_button.click()

    def click_login_button(self):
        login_button = self.driver.find_element(self.login_button_selector[0], self.login_button_selector[1])
        login_button.click()

    def send_login(self, login):
        login_input = self.driver.find_element(self.login_input_selector[0], self.login_input_selector[1])
        for letter in login:
            login_input.send_keys(letter)
            time.sleep(0.2)

    def click_login_pop_button(self):
        login_pop_button = self.driver.find_element(self.login_pop_button_selector[0], self.login_pop_button_selector[1])
        login_pop_button.click()
