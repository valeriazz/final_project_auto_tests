from selenium.webdriver.common.by import By
from selenium import webdriver
from .base_page import BasePage
from .locators import MainPageLocators
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url,"login is absent in current url"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL),"Login Email is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD),"Login Password is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REG_EMAIL),"Registration Email is not presented"
        assert self.is_element_present(*LoginPageLocators.REG_PASSWORD1),"Registration Password 1 is not presented" 
        assert self.is_element_present(*LoginPageLocators.REG_PASSWORD2),"Registration Password 2 is not presented"
        
        