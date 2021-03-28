from pages.basePage import BasePage
from selenium.webdriver.common.by import By

class AdminLoginPage(BasePage):

    url = "http://localhost:8080/jpress/admin/login"
    user = (By.NAME, "user")
    pwd = (By.NAME, "pwd")
    login_btn = (By.CLASS_NAME, "btn")
    help_link = (By.CLASS_NAME, "help-block")

    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()
    
    def input_user(self, text):
        self.input_text(text, *self.user)
    
    def input_pwd(self, text):
        self.input_text(text, *self.pwd)

    def click_login_btn(self):
        self.click(*self.login_btn)

    def click_help_link(self):
        self.click(*self.help_link)

    def goto_login_page(self):
        self.driver.get(self.url)