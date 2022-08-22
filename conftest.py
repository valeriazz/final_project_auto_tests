import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en', help='Choose language')
    # Обработчик опции командной строки: в командную строку передается параметр "language", например, '--language="en"'.

@pytest.fixture(scope="function")
def browser(request):
    # В переменную site_language передается параметр "language" из командной строки
    site_language = request.config.getoption('language')
    # Активизируется класс Options
    options = Options()
    # В опции вебдрайвера передаётся параметр из командной строки
    options.add_experimental_option('prefs', {'intl.accept_languages': site_language})
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(5)
    yield browser
    browser.quit()