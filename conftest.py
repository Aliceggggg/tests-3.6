import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption(
        '--language',
        action='store',
        default='en',
        help='Choose language for browser'
    )


@pytest.fixture(scope='function')
def browser(request):
    # Получаем значение параметра language из командной строки
    user_language = request.config.getoption('language')
    
    # Настраиваем опции браузера Chrome
    options = Options()
    options.add_experimental_option(
        'prefs',
        {'intl.accept_languages': user_language}
    )
    
    # Инициализируем браузер с указанными опциями
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()