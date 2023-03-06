import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome", help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en', help="Choose language browser: ru,en,es... (default - en)")


@pytest.fixture(scope="function")   # Возможными значениями параметра scope являются function, class, module, package или session
def browser(request):
    time_0 = time.time()                                                        # для отладки
    print('\n***** Start conftest.py" ***** ', time.time() - time_0)            # для отладки
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    browser = None
    if browser_name == "chrome":
        print(f"\nuser language: {user_language}\nstart {browser_name} browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        options.add_experimental_option('excludeSwitches', ['enable-logging'])  # This should remove the DevTools message - https://stackoverflow.com/questions/47392423/python-selenium-devtools-listening-on-ws-127-0-0-1/56408800#56408800
        browser = webdriver.Chrome(options=options)
        browser.implicitly_wait(15)
        print('***** Start Web driver from "conftest.py" ***** ', time.time() - time_0)      # для отладки
    elif browser_name == "firefox":
        print(f"\nuser language: {user_language}\nstart {browser_name} browser for test..")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=fp)
        browser.implicitly_wait(15)
        print('***** Start Web driver from "conftest.py" ***** ', time.time() - time_0)      # для отладки
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser           # возвращает значение фикстуры
    print("\nquit browser..")
    browser.quit()
    print('***** Stop conftest.py" ***** ', time.time() - time_0)             # для отладки
