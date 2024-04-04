import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_objects.PersonalInformationPage import PersonalInformation

from page_objects.BooksPage import BooksPage


class MainPage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.button_signin_slctr = (By.XPATH, '//span[text()="Войти"]')
        self.button_toggle_email_slctr = (By.XPATH, '(//a[@class="enter-with-password"])[1]')
        self.input_email_slctr = (By.ID, 'username-pass')
        self.input_password_slctr = (By.ID, 'password')
        self.button_login_slctr = (By.XPATH, '(//input[@value="Войти"])[2]')
        self.button_personalis_slctr = (By.XPATH, '(//a[@href="https://www.flip.kz/user?personalis=person"])[1]')
        self.button_books_slctr = (By.XPATH, '(//a[@class="condent p-0-8 "])[5]')
        self.username_container = (By.XPATH, '(//a[@href="https://www.flip.kz/user?personalis"])[1]/span')
        self.wait = WebDriverWait(self.driver, 10)
        self.input_search_slctr = (By.ID, 'search_input')
        self.search_text_slctr = (By.XPATH, '//h1[@class="cell"]')

    def click_signin_button(self):
        button_signin = self.find_element(self.button_signin_slctr)
        button_signin.click()

    def button_toggle_email(self):
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

    def pass_to_BooksPage(self) -> BooksPage:
        button_books = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.button_books_slctr[1])))
        button_books.click()
        return BooksPage(self.driver)

    def pass_to_PersonalInformation(self) -> PersonalInformation:
        button_personalis = self.find_element(self.button_personalis_slctr)
        button_personalis.click()
        return PersonalInformation(self.driver)

    def find_element(self, slctr):
        return self.driver.find_element(slctr[0], slctr[1])

    def is_logged(self):
        if self.driver.current_url == 'https://www.flip.kz/user?password':
            return False
        return self.find_element(self.username_container).text != 'Войти'

    def search(self, query: str):
        el = self.find_element(self.input_search_slctr)
        el.send_keys(query)
        el.send_keys(Keys.ENTER)

    def get_search_text(self) -> str:
        return self.find_element(self.search_text_slctr).text