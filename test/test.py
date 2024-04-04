import time

import pytest
from selenium import webdriver

from page_objects.main_page import MainPage

from utils import get_options

site = "https://www.flip.kz/"
email = 'nurdauletagabek2@gmail.com'
password = 'onepiece'
new_password = 'naruto'
name = "Нурда"
bookId = ""


@pytest.fixture
def driver():
    chrome_options = get_options()

    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
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
    favourite_page = book_page.pass_to_FavouritePage()
    assert favourite_page.contains_product(product)

@pytest.mark.parametrize(
    'query', [
            'ручка'
    ]
)
def test_search(driver, query):
    page = MainPage(driver)
    page.search(query)
    assert page.get_search_text().lower() == query.lower()

@pytest.mark.parametrize(
    'old_password, new_password, retry_password, success', [
        (password, new_password, new_password, True),
        ('qwertybek', new_password, new_password, False),
        (password, new_password, 'qwertybek', False)
    ]
)
def test_change_password(signedin, old_password, new_password, retry_password, success):
    page = MainPage(signedin)
    personalis_page = page.pass_to_PersonalInformation()
    password_page = personalis_page.pass_to_PasswordPage()
    password_page.send_old_password(old_password)
    password_page.send_new_password(new_password)
    password_page.send_retry_password(retry_password)
    password_page.click_save()
    assert password_page.is_password_successfully_changed() == success
    if success:
        password_page.send_old_password(new_password)
        password_page.send_new_password(old_password)
        password_page.send_retry_password(old_password)
        password_page.click_save()

def test_price_is_added_to_cart(signedin):
    page = MainPage(signedin)
    books_page = page.pass_to_BooksPage()
    bookId = books_page.save_book_id()
    books_page.click_button_add_book()
    cart_page = books_page.pass_to_CartPage(bookId=bookId)
    total_price = cart_page.get_total_price()
    actual_total_price = cart_page.compute_total_price()
    print(total_price)
    print(actual_total_price)
    assert total_price == actual_total_price