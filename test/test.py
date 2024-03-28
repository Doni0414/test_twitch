import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

from page_objects.main_page import MainPage

site = "https://www.twitch.tv/"

@pytest.fixture
def driver():
    language_preference = "en"
    chrome_options = Options()
    chrome_options.add_experimental_option('prefs', {'intl.accept_languages': language_preference})

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(site)

    yield driver
    driver.quit()

@pytest.mark.parametrize(
    'login, password, date_of_birth, email', [
        ('dummy_test1', 'OnePieceIsReal1997', ['May', 14, 2004], 'dummy_test@mail.ru'),
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
