import py
import pytest
from selenium import webdriver
import os, sys
# sys.path.append(os.getcwd())
from common.constant import chrome_capabilities, ADMIN_TOKEN
import pytest
from util.read_data import ReadData
from util.util import get_random_str
from util.logger import Logger
from pages.categoryPage import CategoryPage
from pages.adminMenuPage import AdminMenuPage
from pages.iconPage import IconPage
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
import json

@pytest.mark.usefixtures("tmp_title_file")
@pytest.mark.usefixtures("admin_token")
class TestCategory(object):

    def setup_class(self):
        # self.driver = webdriver.Remote(
        #     command_executor = "http://localhost:4444/wd/hub",
        #     desired_capabilities = chrome_capabilities
        # )
        self.logger = Logger().get_logger()
        self.driver = webdriver.Chrome()
        self.category_page = CategoryPage(self.driver)
        self.admin_menu = AdminMenuPage(self.driver)
        self.icon_page = IconPage(self.driver)
        self.driver.get('http://localhost:8080/jpress/admin/login')
        self.driver.add_cookie(ADMIN_TOKEN)
        self.driver.get('http://localhost:8080/jpress/admin/index')
        self.driver.maximize_window()
        assert self.driver.title == "JPress后台"

    @pytest.mark.dependency(name="add_category")
    @pytest.mark.parametrize(
        "title, parent, slug, order, content, summary, show_in_menu, des, keyword",
        ReadData("category.xlsx").read_excel()
    )
    def test_add_category(self, tmp_title_file, title, parent, slug, order, content, summary, show_in_menu, des, keyword):
        self.admin_menu.click_aritcle()
        self.admin_menu.click_category()
        title = get_random_str()
        self.logger.info(f"随机生成title: {title}")
        self.category_page.input_title(title)
        self.category_page.select_parent(parent)
        self.category_page.input_slug(slug)
        self.category_page.do_order(order)
        self.category_page.input_content(content)
        self.category_page.input_summary(summary)
        self.category_page.ctrl_dispaly_in_menu(show_in_menu)
        self.category_page.input_description(des)
        self.category_page.input_keyword(keyword)
        self.category_page.input_icon()
        self.category_page.submit()
        sleep(2)
        result = self.check_add_category_result(title)
        assert result["result"]
        tmp_title_file.write(json.dumps({
            "title": title,
            "row_index": result["row_index"]
        }))

    @pytest.mark.dependency(depends=["add_category"])
    def test_delete_category(self, tmp_title_file):
        data = json.loads((tmp_title_file.read()))
        before_del_rows = self.total_rows()
        row = data["row_index"] + 1
        self.category_page.delete_one_title(row, data["title"])
        after_del_rows = self.total_rows()
        assert before_del_rows == after_del_rows + 1

    def check_add_category_result(self, expected_title):
        result = False
        row_index = None
        table = self.driver.find_element(*self.category_page.table)
        rows = table.find_elements_by_tag_name("tr")
        for idx in range(1, len(rows)):
            title = rows[idx].find_element_by_tag_name("a").text
            if title == expected_title:
                row_index = idx
                result = True
                break
        return {"result": result, "row_index": row_index}

    def total_rows(self):
        rows = self.driver.find_elements(*self.category_page.table_rows)
        return len(rows)


if __name__ == "__main__":
    pytest.main(["-s", "-v", f"{os.path.abspath('testcases')}/test_category.py"])