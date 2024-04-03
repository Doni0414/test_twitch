# This is a sample Python script.
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium_stealth import stealth


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from seleniumwire.undetected_chromedriver.v2 import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
import time
import pickle


if __name__ == "__main__":
    options = {}

    browser = Chrome()
    browser.get('https://gmail.com')

    time.sleep(50)
    browser.get('https://www.youtube.com')
    pickle.dump(browser.get_cookies(), open('test_cookies.pkl', 'wb'))
    print('Dumped Successfully')

    time.sleep(10)
    browser.close()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
