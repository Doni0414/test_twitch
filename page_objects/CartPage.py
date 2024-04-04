import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class CartPage:
    def __init__(self, driver: webdriver.Chrome, bookId: str):
        self.driver = driver
        self.bookId = bookId
        self.save_book_id_slctr = (By.XPATH, '(//a[@href="/catalog?prod=' + bookId + '"])/input')
        self.span_total_price_slctr = (By.XPATH, "//span[@class='mclpriceDisc text_att']")
        self.books_price_slctr = (By.XPATH, "//b[@data-summa-total]")

    def save_book_id(self) -> str:
        save_book_id = self.find_element(self.save_book_id_slctr)
        return save_book_id.get_attribute("value")

    def find_element(self, slctr):
        return self.driver.find_element(slctr[0], slctr[1])

    def cart_is_empty(self) -> bool:
        try:
            el = self.find_element(self.span_total_price_slctr)
            return False
        except:
            return True
    def get_total_price(self) -> float:
        if self.cart_is_empty():
            return 0
        el = self.find_element(self.span_total_price_slctr)
        return self.clean_price(el.text)

    def compute_total_price(self):
        els = self.driver.find_elements(self.books_price_slctr[0], self.books_price_slctr[1])
        prices = [self.clean_price(el.text) for el in els]
        return sum(prices)

    def clean_price(self, price: str) -> float:
        return float(price.replace(" ", "").replace("₸", ""))