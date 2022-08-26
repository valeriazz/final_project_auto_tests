from .base_page import BasePage
from .basket_page import BasketPage
from selenium import webdriver
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
import math
from selenium.common.exceptions import NoAlertPresentException

class ProductPage(BasePage):
    def add_to_basket(self):
        self.click_the_button_add_to_basket()
        self.solve_quiz_and_get_code()
              
    def click_the_button_add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        button.click()
        
    def solve_quiz_and_get_code(self):
        try:
            alert = self.browser.switch_to.alert
            x = alert.text.split(" ")[2]
            answer = str(math.log(abs((12 * math.sin(float(x))))))
            alert.send_keys(answer)
            alert.accept()
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
          
    def add_to_basket_alert_success(self):
        assert self.is_element_present(*ProductPageLocators.ALERT_ADDED_TO_BASKET), "No message about successful adding to basket"
        
    def product_name_is_the_same(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        alert_added_to_basket = self.browser.find_element(*ProductPageLocators.ALERT_ADDED_TO_BASKET).text
        assert product_name == alert_added_to_basket, "No product name in the message"
        
    def price_is_the_same(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        alert_basket_total = self.browser.find_element(*ProductPageLocators.ALERT_BASKET_TOTAL).text
        assert product_price == alert_basket_total, "No product price in the alert"
        
    def guest_cant_see_success_message_after_adding_product_to_basket(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
       "Success message is presented, but should not be"
    
    def guest_cant_see_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
       "Success message is presented, but should not be"
    
    def message_disappeared_after_adding_product_to_basket(self):
         assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
       "Success message doesn't disappear, but should be"
       
  