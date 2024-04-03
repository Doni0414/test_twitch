import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

from page_objects.main_page import MainPage
from utils import get_options

site = "https://www.flip.kz/"
email = 'nurdauletagabek2@gmail.com'
password = 'onepiece'

@pytest.fixture
def driver():
    chrome_options = get_options()

    driver = webdriver.Chrome(options=chrome_options)

    driver.get(site)

    yield driver
    driver.quit()


@pytest.fixture
def signedin():
    chrome_options = get_options()

    driver = webdriver.Chrome(options=chrome_options)

    driver.get(site)

    page = MainPage(driver)
    time.sleep(2)
    page.click_signin_button()
    time.sleep(2)
    page.toggle_email()
    time.sleep(2)
    page.send_email(email)
    page.send_password(password)
    page.click_login()
    time.sleep(2)
    yield driver
    driver.quit()

# @pytest.mark.parametrize(
#     ''
# )
def test_following(signedin):
    page = MainPage(signedin)
    time.sleep(10)