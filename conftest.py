import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption(
        "--language",
        action="store",
        default=None,
    )

@pytest.fixture(scope='session')
def browser(request):

    language = request.config.getoption("--language")

    if language is not None:
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})

        print(f"\nЗапуск браузера Chrome с языком {language}")
        driver = webdriver.Chrome(options=options)
    else:
        raise ValueError("Не указан параметр --language!")

    driver.language = language

    yield driver
    print("\nЗакрытие браузера...")
    driver.quit()

