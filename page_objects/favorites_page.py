from selenium import webdriver
from selenium.webdriver.common.by import By


class FavoritesPage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.url = 'https://www.flip.kz/favorites'

    def open(self):
        self.driver.get(self.url)

    def find_element(self, slctr):
        return self.driver.find_element(slctr[0], slctr[1])

    def contains_product(self, product: str) -> bool:
        prods = [prod.text for prod in self.driver.find_elements(By.XPATH, '(//a[@class="title" and contains(@href, "/catalog?prod")])')]
        print(prods)
        print(product)
        return prods.__contains__(product)
