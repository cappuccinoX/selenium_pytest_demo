from selenium.webdriver.common.by import By
from pages.basePage import BasePage

class UserRegisterPage(BasePage):

    username = (By.NAME, 'username')
    email = (By.NAME, 'email')
    pwd = (By.NAME, 'pwd')
    confirm_pwd = (By.NAME, 'confirmPwd')
    captcha = (By.ID, "captcha")
    captcha_img = (By.ID, "captchaimg")
    submit_btn = (By.CLASS_NAME, "btn")

    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()

    def go_to_register_page(self):
        self.driver.get("http://localhost:8080/jpress/user/register")

    def input_email(self, email):
        self.input_text(email, *self.email)

    def input_username(self, username):
        self.input_text(username, *self.username)

    def input_captcha(self, captcha):
        self.input_text(captcha, *self.captcha)

    def input_pwd(self, pwd):
        self.input_text(pwd, *self.pwd)

    def input_confirm_pwd(self, confirm_pwd):
        self.input_text(confirm_pwd, *self.confirm_pwd)

    def click_register(self):
        self.click(*self.submit_btn)


if __name__ == "__main__":
    print(11)