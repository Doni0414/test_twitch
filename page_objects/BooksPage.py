from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from page_objects.CartPage import CartPage
from page_objects.favorites_page import FavoritesPage


class BooksPage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.button_add_book_slctr = (By.XPATH, '(//input[@title="Добавить в корзину"])[1]')
        self.button_move_to_cart_slctr = (By.XPATH, '(//a[@href="/cart"])[4]')
        self.save_book_id_slctr = (By.XPATH, '(//input[@name="cart_id_produce"])[1]')
        self.button_first_favorite_slctr = (By.XPATH, '(//label[contains(@for, "favorites-")])[1]')
        self.button_favorites = (By.XPATH, '//a[@href="/favorites"]')
        self.button_personalis_slctr = (By.XPATH, '(//a[@href="https://www.flip.kz/user?personalis=person"])[1]')
        self.wait = WebDriverWait(self.driver, 20)
        self.checkbox_field_slctr = (By.XPATH, '//ul[@class="underline text-unselectable"]/li/input')
        self.text_checkbox_value_slctr = (By.XPATH, '//*[@id="main-catalog-filter"]/ul[1]/li[1]/label/div[2]/span')
        self.field_checkbox_slctr = (By.XPATH, '//*[@id="main-catalog-filter"]/ul[1]')

    def click_button_add_book(self):
        action = webdriver.ActionChains(self.driver)
        button_add_book = self.find_element(self.button_add_book_slctr)
        action.move_to_element(button_add_book)
        action.perform()
        button_add_book.click()

    def click_first_favorite(self) -> str:
        button_first_favorite = self.find_element(self.button_first_favorite_slctr)
        button_first_favorite.click()
        return self.driver.find_element(By.XPATH, '(//a[@class="title" and contains(@href, "/catalog?prod")])[1]').text

    def pass_to_FavouritePage(self) -> FavoritesPage:
        action = webdriver.ActionChains(self.driver)
        button_personalis = self.find_element(self.button_personalis_slctr)
        action.move_to_element(button_personalis)
        action.perform()
        button_favorites = self.find_element(self.button_favorites)
        button_favorites.click()
        return FavoritesPage(self.driver)

    def pass_to_CartPage(self, bookId: str) -> CartPage:
        button_move_to_cart = self.find_element(self.button_move_to_cart_slctr)
        button_move_to_cart.click()
        return CartPage(self.driver, bookId=bookId)

    def save_book_id(self) -> str:
        save_book_id = self.find_element(self.save_book_id_slctr)
        return save_book_id.get_attribute("value")

    def find_element(self, slctr):
        return self.driver.find_element(slctr[0], slctr[1])

    def click_checkbox(self, index: int):
        checkbox_fields = self.driver.find_element(By.XPATH, '(//*[@id="main-catalog-filter"]/ul/li/label/div['
                                                             '@class="checkbox cell w-o"])[' + str(index) + ']')
        checkbox_fields.click()

    def save_checkbox_value(self) -> str:
        text_checkbox_value = self.find_element(self.text_checkbox_value_slctr)
        return text_checkbox_value.text
