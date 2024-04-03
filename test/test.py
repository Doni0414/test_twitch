import time

import pytest
from selenium import webdriver

from page_objects.main_page import MainPage
from page_objects.BooksPage import BooksPage
from page_objects.CartPage import CartPage
from page_objects.PersonalInformationPage import PersonalInformation

from utils import get_options

site = "https://www.flip.kz/"
email = 'qwer254565@gmail.com'
password = 'Pokemon1'
name = "Анс"
bookId = ""


@pytest.fixture
def driver():
    chrome_options = get_options()

    driver = webdriver.Chrome(options=chrome_options)

    driver.get(site)

    yield driver
    driver.quit()


def test_change_name(signedin):
    page = MainPage(signedin)
    personalis_page = page.pass_to_PersonalInformation()
    personalis_page.delete_name()
    personalis_page.send_name(name)
    personalis_page.click_save_button()
    personalis_page.driver.refresh()
    assert personalis_page.get_name() == name


def test_check_cart(signedin):
    page = MainPage(signedin)
    books_page = page.pass_to_BooksPage()
    bookId = books_page.save_book_id()
    books_page.click_button_add_book()
    cart_page = books_page.pass_to_CartPage(bookId=bookId)
    bookId2 = cart_page.save_book_id()
    assert bookId == bookId2



@pytest.fixture
def signedin():
    chrome_options = get_options()

    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    driver.get(site)

    page = MainPage(driver)
    page.click_signin_button()
    page.button_toggle_email()
    page.send_email(email)
    page.send_password(password)
    page.click_login()
    yield driver
    driver.quit()
@pytest.mark.parametrize(
    'login, password, success', (
            (email, 'OnePieceIsReal', False),
            (email, password, True)
    )
)
def test_login(driver, login, password, success):
    page = MainPage(driver)
    page.click_signin_button()
    page.button_toggle_email()
    page.send_email(login)
    page.send_password(password)
    page.click_login()

    time.sleep(5)

    assert page.is_logged() == success

def test_favorite_button(signedin):
    page = MainPage(signedin)
    time.sleep(3)
    book_page = page.pass_to_BooksPage()
    time.sleep(3)
    product = book_page.click_first_favorite()
    time.sleep(10)
    favourite_page = book_page.click_favorites()
    assert favourite_page.contains_product(product)
