from selenium import webdriver
from selenium.webdriver.common import utils
from selenium.webdriver.remote.webelement import WebElement
from util.logger import Logger
from time import sleep
import pytest
import os
from pages.menu import Menu
from pages.contributeArticles import ContributeArticlesPage
import allure
from pages.userLoginPage import UserLoginPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from common.constant import chrome_capabilities

'''
用例难点
1. 登录步骤设置为固件
2. 上传文件
3. SEO 相关信息的输入框在页面底部，需要滚动才能定位
4. 切换iframe
'''

# @pytest.mark.usefixtures("login")
@allure.feature("用户投稿功能用例集")
class TestConArticles():

    def setup_class(self):
        # self.driver = webdriver.Remote(
        #     command_executor = "http://localhost:4444/wd/hub",
        #     desired_capabilities = chrome_capabilities
        # )
        self.driver = webdriver.Chrome()
        self.logger = Logger().get_logger()
        self.menu = Menu(self.driver)
        self.con_articles = ContributeArticlesPage(self.driver)
        self.user_login_page = UserLoginPage(self.driver)
        self.driver.get("http://localhost:8080/jpress/ucenter")
        self.driver.add_cookie({
            "name" : "_jpuid",
            "value": 'NTljZjRiNDliMGE1ZDIzYWI2ODE2ZDc0ZmQ4NDczNmYjMTYxNjkyNTk4ODA2OSMxNzI4MDAjTVE9PQ=='
        })
        print(self.driver.get_cookies())

    
    # TODO 改为固件
    def login(self):
        self.user_login_page.goto_login_page()
        WebDriverWait(self.driver, 3).until(EC.title_is("登录到用户中心"))
        self.user_login_page.input_user("admin")
        self.user_login_page.input_pwd("123456")
        self.user_login_page.click_login_btn()


    # @pytest.mark.skip()
    @allure.story("保存并投稿")
    def test_add_articles(self):
        # self.login()
        self.driver.get("http://localhost:8080/jpress/ucenter")
        self.menu.wait_ele_visiable(self.menu.my_articles, "我的文章")
        self.menu.click_menu("my_articles")
        self.menu.wait_ele_visiable(self.menu.contribute_aritcles, "投稿")
        self.menu.click_menu("contribute_aritcles")
        self.menu.wait_ele_visiable(self.con_articles.iframe, "内容输入框")
        self.con_articles.input_content("This is 1st line content")
        self.con_articles.input_seo_keywords("Key")
        self.con_articles.input_seo_des("SEO Description")
        self.con_articles.upload("girl.jpeg")
        self.con_articles.remove_picture()
        self.con_articles.upload("nokia.jpeg")
        self.con_articles.input_title("Title")
        self.con_articles.submit()
        ele = (By.CLASS_NAME, "toast-message")
        # self.con_articles.wait_ele_visiable(ele, "成功提示框")
        WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(ele)
        )
        message = self.con_articles.find_element(*ele)
        assert message.text == "文章保存成功。"


if __name__ == "__main__":
    pytest.main([
        '-s',
        '-v',
        "%s/test_contribute_articles.py" % os.path.abspath("testcases")
    ])