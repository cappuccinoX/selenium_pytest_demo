from selenium import webdriver
import pytest
from util import util
from util.read_data import ReadData
from util.logger import Logger
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import allure
from time import sleep
from pages.userRegisterPage import UserRegisterPage

@allure.feature("用户注册")
class TestUserRegister():
    def setup_class(self):
        self.logger = Logger().get_logger()
        self.driver = webdriver.Chrome()
        self.user_register_page = UserRegisterPage(self.driver)
    
    def teardown_class(self):
        self.driver.quit()

    # 验证码正确提示语"注册成功，点击确定进行登录。"
    # 验证码不正确提示语"验证码不正确"
    @pytest.mark.skip()
    @allure.story("输入错误的验证码")
    def test_register_error_code(self):
        username = util.get_random_str()
        email = '%s@qq.com' % username
        pwd = 123
        confirm_pwd = 123
        captcha = '666'
        expected = '验证码不正确'

        self.driver.find_element_by_name("username").send_keys(username)
        self.driver.find_element_by_name("email").send_keys(email)
        self.driver.find_element_by_name("pwd").send_keys(pwd)
        self.driver.find_element_by_name("confirmPwd").send_keys(confirm_pwd)
        self.driver.find_element_by_id("captcha").send_keys(captcha)
        self.driver.find_element_by_class_name("btn").click()
        WebDriverWait(self.driver, 3).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        assert alert.text == expected

    @pytest.mark.skip()
    @allure.story("注册成功")
    def test_register_ok(self):
        username = util.gen_random_str()
        email = '%s@qq.com' % username
        pwd = 123
        confirm_pwd = 123
        captcha = '666'
        # expected = '验证码不正确'
        # 输入用户名
        username_elem = self.driver.find_element_by_name('username')
        username_elem.clear()
        username_elem.send_keys(username)

        # email
        email_elem = self.driver.find_element_by_name('email')
        email_elem.clear()
        email_elem.send_keys(email)
        # 密码
        self.driver.find_element_by_name('pwd').clear()
        self.driver.find_element_by_name('pwd').send_keys(pwd)
        # 确认密码
        self.driver.find_element_by_name('confirmPwd').clear()
        self.driver.find_element_by_name('confirmPwd').send_keys(confirm_pwd)


    @pytest.mark.parametrize("casedata", ReadData("register.json").read_json())
    def test_register(self, casedata):
        if (casedata["result"] != "registerSuccess"):
            username = util.get_random_str()
            email = '%s@qq.com' % username
            self.user_register_page.go_to_register_page()
            self.user_register_page.input_username(username)
            self.user_register_page.input_email(email)
            self.user_register_page.input_pwd(casedata["pwd"])
            self.user_register_page.input_confirm_pwd(casedata["confirmPwd"])
            self.user_register_page.input_captcha(casedata["captcha"])
            self.user_register_page.click_register()
            WebDriverWait(self.driver, 3).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert_msg = self.driver.switch_to.alert.text
            alert.accept()
            assert alert_msg == casedata["expected"]
        else:
            print("not finish...............")

    @pytest.mark.parametrize('user, pwd',
        [
            ('jack', 12345),
            ('Andy', 2223)
        ])
    @pytest.mark.skip()
    def test_3(self, user, pwd):
        print('User is {user}, password is {pwd}'.format(user = user, pwd = pwd))

if __name__ == "__main__":
    pytest.main(['test_user_register.py'])