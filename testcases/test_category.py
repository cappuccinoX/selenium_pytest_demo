import pytest
from selenium import webdriver
import os, sys
sys.path.append(os.getcwd())
from common.constant import chrome_capabilities, ADMIN_TOKEN
import pytest

@pytest.mark.usefixtures("admin_token")
class TestCategory(object):

    def setup_class(self):
        self.driver = webdriver.Remote(
            command_executor = "http://localhost:4444/wd/hub",
            desired_capabilities = chrome_capabilities
        )
        self.driver.get('http://localhost:8080/jpress/admin/login')
        self.driver.add_cookie(ADMIN_TOKEN)
        self.driver.get('http://localhost:8080/jpress/admin/index')
        self.driver.maximize_window()
        assert self.driver.title == "JPress后台"

    
    def test_category(self):
        assert True


if __name__ == "__main__":
    pytest.main(["-s", "-v", f"{os.path.abspath('testcases')}/test_category.py"])