from .pages.login_page import LoginPage


def test_guest_can_see_login_form(browser):
    link = "http://selenium1py.pythonanywhere.com/accounts/login/"
    page = LoginPage(browser, link)    
    page.open()                      
    page.should_be_login_url()
    page.should_be_login_form()
    page.should_be_register_form()
   