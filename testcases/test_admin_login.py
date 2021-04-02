from time import sleep

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import os
import pytest
from common.constant import chrome_capabilities


class TestAdminLogin(object):

    def setup_class(self):
        # self.driver = webdriver.Chrome()
        # self.driver.get('http://localhost:8080/jpress/admin/login')
        self.driver = webdriver.Remote(
            command_executor = "http://localhost:4444/wd/hub",
            desired_capabilities = chrome_capabilities
        )
        self.driver.get('http://localhost:8080/jpress/admin/login')
        self.driver.add_cookie({
            "name" : "_jpuid",
            "value": 'ZjYyYzQxZThjN2NkM2JjOTUxNWFlNDlhMmE2MzMxY2EjMTYxNzA3NzIwMTQ0MSMxNzI4MDAjTVE9PQ=='
        })
        self.driver.maximize_window()

    # 测试管理员登录
    def test_admin_login(self):
        self.driver.get("http://localhost:8080/jpress/admin/index")
        # self.driver.find_element_by_name('user').clear()
        # self.driver.find_element_by_name('user').send_keys(username)

        # self.driver.find_element_by_name('pwd').clear()
        # self.driver.find_element_by_name('pwd').send_keys(pwd)

        # self.driver.find_element_by_name('captcha').clear()
        # if captcha != '666':
        #     captcha = util.get_code(self.driver, 'captchaImg')
        # self.driver.find_element_by_name('captcha').send_keys(captcha)
        # self.driver.find_element_by_class_name('btn').click()

        # if captcha != '666':
        #     WebDriverWait(self.driver, 5).until(EC.title_is(expected))
        #     assert expected == self.driver.title
        # else:
        #     WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        #     alert = self.driver.switch_to.alert

        #     assert alert.text == expected
        #     alert.accept()

        #     sleep(5)

        # self.driver.quit()

if __name__ == '__main__':
    pytest.main(["-s", "-v", f"{os.path.abspath('testcases')}/test_admin_login.py"])
