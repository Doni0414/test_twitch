import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class CartPage:
    def __init__(self, driver: webdriver.Chrome, bookId: str):
        self.driver = driver
        self.bookId = bookId
        self.save_book_id_slctr = (By.XPATH, '(//a[@href="/catalog?prod=' + bookId + '"])/input')

    def save_book_id(self) -> str:
        save_book_id = self.find_element(self.save_book_id_slctr)
        return save_book_id.get_attribute("value")

    def find_element(self, slctr):
        return self.driver.find_element(slctr[0], slctr[1])
