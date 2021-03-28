import pytest
from selenium import webdriver
from util.logger import Logger
from pages.userLoginPage import UserLoginPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from util.read_data import ReadData
from time import sleep
import allure
from common.constant import chrome_capabilities

@allure.feature("用户登录用例集")
class TestUserLogin():
    
    def setup_class(self):
        self.driver = webdriver.Remote(
            command_executor = "http://localhost:4444/wd/hub",
            desired_capabilities = chrome_capabilities
        )
        self.logger = Logger().get_logger()
        self.user_login_page = UserLoginPage(self.driver)

    def teardown_class(self):
        self.driver.quit()


    @pytest.mark.skip()
    @allure.story("用户登录")
    @pytest.mark.parametrize("result, user, pwd, expected", ReadData("login.csv").read_csv())
    def test_login(self, result, user, pwd, expected):
        try:
            self.user_login_page.goto_login_page()
            WebDriverWait(self.driver, 3).until(EC.title_is("登录到用户中心"))
            self.user_login_page.input_user(user)
            self.user_login_page.input_pwd(pwd)
            self.user_login_page.click_login_btn()
            if result == "loginFail":
                WebDriverWait(self.driver, 3).until(EC.alert_is_present())
                alert = self.driver.switch_to.alert
                assert alert.text == expected
                alert.accept()
            else:
                WebDriverWait(self.driver, 3).until(EC.url_contains("ucenter"))
                assert self.driver.title == "用户中心"
        except Exception as e:
            self.logger.error("用例'用户登录'执行报错: %s" % e)

    # @pytest.mark.dependency(name = "admin_login")
    def test_admin_login(self):
        self.user_login_page.goto_login_page()
        WebDriverWait(self.driver, 3).until(EC.title_is("登录到用户中心"))
        self.user_login_page.input_user("admin")
        self.user_login_page.input_pwd("123456")
        self.user_login_page.click_login_btn()
        WebDriverWait(self.driver, 3).until(EC.url_contains("ucenter"))
        assert self.driver.title == "用户中心"

if __name__ == "__main__":
    pytest.main(['-s', '-v', '%s/test_login.py' % os.path.abspath("testcases")])