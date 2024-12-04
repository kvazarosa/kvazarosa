from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time


# Тестовая функция, которая принимает браузер как аргумент
def test_button_is_present(browser):
    url = f"http://selenium1py.pythonanywhere.com/{browser.language}/catalogue/coders-at-work_207/"
    browser.get(url)
    time.sleep(15)

    # Проверяем наличие кнопки добавления в корзину
    button = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert len(button) > 0, '!!!Кнопка не найдена!!!!'

