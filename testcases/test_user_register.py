from selenium import webdriver
import pytest
from util import util
from util.read_data import ReadData
from util.logger import Logger
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

    @allure.story("测试注册")
    @pytest.mark.parametrize("casedata", ReadData("register.json").read_json())
    def test_register(self, casedata):
        try:
            if (casedata["result"] != "registerSuccess"):
                username = util.get_random_str()
                email = '%s@qq.com' % username
                self.logger.info("生成随机账户%s和邮箱%s" % (username, email))
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
        except Exception as e:
            self.logger.error("用例'测试注册'执行报错: %s" % e)


if __name__ == "__main__":
    logger = Logger().get_logger()
    logger.info("a")
