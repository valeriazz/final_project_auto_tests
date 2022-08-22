from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators():

    LOGIN_EMAIL = (By.NAME, "login-username")
    LOGIN_PASSWORD = (By.NAME, "login-password")
    REG_EMAIL = (By.NAME, "registration-email")
    REG_PASSWORD1 = (By.NAME, "registration-password1")
    REG_PASSWORD2 = (By.NAME, "registration-password2") 
   
   
