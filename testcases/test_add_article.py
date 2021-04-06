# import os, sys
# sys.path.append(os.getcwd())
from typing import no_type_check_decorator
from selenium import webdriver
from pages.addAritclePage import AddArticlePage
from pages.adminMenuPage import AdminMenuPage
from pages.aritcleManagementPage import AritcleManagementPage
import pytest
from common.constant import ADMIN_TOKEN, chrome_capabilities
from util import logger
from util.util import get_random_str
from util.logger import Logger
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep

@pytest.mark.usefixtures("admin_token")
class TestAddArticle(object):

    def setup_class(self):
        # self.driver = webdriver.Remote(
        #     command_executor = "http://localhost:4444/wd/hub",
        #     desired_capabilities = chrome_capabilities
        # )
        self.logger = Logger().get_logger()
        self.driver = webdriver.Chrome()
        self.admin_menu = AdminMenuPage(self.driver)
        self.add_article_page = AddArticlePage(self.driver)
        self.article_management_page = AritcleManagementPage(self.driver)
        self.driver.get('http://localhost:8080/jpress/admin/login')
        self.driver.add_cookie(ADMIN_TOKEN)
        self.driver.get('http://localhost:8080/jpress/admin/index')
        self.driver.maximize_window()
        assert self.driver.title == "JPress后台"

    @pytest.mark.dependency(name = "add_article")
    def test_add_article(self):
        self.admin_menu.click_aritcle()
        self.admin_menu.click_add_article()
        title = get_random_str()
        self.logger.info(f"生成随机的title: {title}")
        self.add_article_page.input_title(title)
        self.add_article_page.input_content("pytest introduction")
        self.add_article_page.submit()
        ele = (By.CLASS_NAME, "toast-message")
        # self.con_articles.wait_ele_visiable(ele, "成功提示框")
        WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(ele)
        )
        message = self.driver.find_element(*ele)
        assert message.text == "文章保存成功。"

    @pytest.mark.dependency(depends = ["add_article"])
    def test_delete_all_articles(self):
        self.admin_menu.click_article_manage()
        self.article_management_page.select_all()
        self.article_management_page.delete_all()
        sleep(1)
        assert self.check_delete_all_result()

    def check_delete_all_result(self):
        table = self.driver.find_element(By.CLASS_NAME, "table-striped")
        rows = table.find_elements_by_tag_name("tr")
        # rows = 1 表示文章列表只有标题行
        return len(rows) == 1

if __name__ == "__main__":
    pytest.main(["-s", '-v', "test_add_article.py"])