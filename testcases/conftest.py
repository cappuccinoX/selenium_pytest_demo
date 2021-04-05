from logging import log
import pytest
from selenium import webdriver
from pages.userLoginPage import UserLoginPage
from common.constant import chrome_capabilities
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.constant import ADMIN_TOKEN
import os

@pytest.fixture(name = "token")
def get_token():
    return "NTljZjRiNDliMGE1ZDIzYWI2ODE2ZDc0ZmQ4NDczNmYjMTYxNjkyNTk4ODA2OSMxNzI4MDAjTVE9PQ"

@pytest.fixture(name = "admin_token", scope = "module")
def get_admin_token():
    ADMIN_TOKEN["value"] = "YjMwZGY0MjYzMTM5YmIxZTNkMjEzMWYyN2E0N2MyZjMjMTYxNzU4Nzc3MDczOSMxNzI4MDAjTVE9PQ=="

# 创建文章分类时, 将分类标题写入临时文件, 便于删除分类用例通过临时文件找到标题并删除
@pytest.fixture(scope="class")
def tmp_title_file(tmpdir_factory):
    print("\n======start to create temp file======")
    tmp_dir = tmpdir_factory.mktemp("tmp")
    tmp_file = tmp_dir.join("tmp_title.txt")
    print("\n======success to create temp file======")
    yield tmp_file
    print("\n======delete tmp_title.txt======")

@pytest.fixture(scope="class")
def test_fixture():
    print("\nlalallalalala.......")

@pytest.fixture(scope="class", name="login")
def login():
    driver = webdriver.Remote(
        command_executor = "http://localhost:4444/wd/hub",
        desired_capabilities = chrome_capabilities
    )
    user_login_page = UserLoginPage(driver)
    user_login_page.goto_login_page()
    WebDriverWait(driver, 3).until(EC.title_is("登录到用户中心"))
    user_login_page.input_user("admin")
    user_login_page.input_pwd("123456")
    user_login_page.click_login_btn()
    driver.add_cookie({"age": 19})
    return driver

# if __name__ == "__main__":
