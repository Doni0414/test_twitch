from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

def get_options():
    # language_preference = "en"
    chrome_options = Options()

    chrome_options.add_argument("start-maximized")
    chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
    chrome_options.add_experimental_option('useAutomationExtension', False)

    chrome_options.add_argument('--disable-blink-features=AutomationControlled')

    # chrome_options.add_experimental_option('prefs', {'intl.accept_languages': language_preference})

    return chrome_options