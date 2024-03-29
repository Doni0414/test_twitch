import pytest
from selenium import webdriver
import time

from page_objects.main_page import MainPage
from utils import get_options

site = "https://www.twitch.tv/"
username = 'dummy_test1'
password = 'OnePieceIsReal1997'
email = 'dummy_test@mail.ru'

@pytest.fixture
def driver():
    chrome_options = get_options()

    driver = webdriver.Chrome(options=chrome_options)

    driver.get(site)

    yield driver
    driver.quit()

@pytest.mark.skip
@pytest.mark.parametrize(
    'login, password, date_of_birth, email', [
        (username, password, ['May', 14, 2004], email),
    ]
)
def test_registration(driver, login, password, date_of_birth, email):
    page = MainPage(driver)

    page.click_sign_up_button()

    time.sleep(5)

    page.toggle_email()

    time.sleep(2)

    page.send_username(login)

    time.sleep(2)

    page.send_password(password)

    time.sleep(2)

    page.send_birth_month(date_of_birth[0])

    time.sleep(2)

    page.send_birth_day(date_of_birth[1])

    time.sleep(2)

    page.send_birth_year(date_of_birth[2])

    time.sleep(2)

    page.send_email(email)

    time.sleep(2)

    page.click_sign_up_pop_button()

    time.sleep(2)

@pytest.fixture
def signedin():
    chrome_options = get_options()

    driver = webdriver.Chrome(options=chrome_options)

    driver.get(site)

    page = MainPage(driver)
    time.sleep(2)
    page.click_login_button()
    time.sleep(2)
    page.send_login(username)
    time.sleep(2)
    page.send_password(password)
    time.sleep(2)
    page.click_login_pop_button()
    time.sleep(20)

    yield driver
    driver.quit()

# @pytest.mark.parametrize(
#     ''
# )
def test_following(signedin):
    page = MainPage(signedin)