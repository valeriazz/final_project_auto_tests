from .base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def text_about_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY), "No message about empty basket"