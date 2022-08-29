import pytest
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.base_page import BasePage
from .pages.basket_page import BasketPage
import time
from selenium.common.exceptions import NoSuchElementException

@pytest.mark.guest_main
class TestLoginAndBasketFromMainPage():
    def test_guest_can_go_to_login_page(self,browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        page.open()                      # открываем страницу
        login_page = page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()
   
   
    def test_guest_cant_see_product_in_basket_opened_from_main_page(self,browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        page2 = BasketPage(browser, link)
        page.open()
        page.go_to_basket()
        time.sleep(10)
        page2.text_about_empty_basket()
    
