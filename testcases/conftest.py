from logging import log
import pytest
from selenium import webdriver
from pages.userLoginPage import UserLoginPage
from common.constant import chrome_capabilities
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.constant import ADMIN_TOKEN

@pytest.fixture(name = "token")
def get_token():
    return "NTljZjRiNDliMGE1ZDIzYWI2ODE2ZDc0ZmQ4NDczNmYjMTYxNjkyNTk4ODA2OSMxNzI4MDAjTVE9PQ"

@pytest.fixture(name = "admin_token", scope = "module")
def get_admin_token():
    print("\nfixture")
    ADMIN_TOKEN["value"] = "ZjYyYzQxZThjN2NkM2JjOTUxNWFlNDlhMmE2MzMxY2EjMTYxNzA3NzIwMTQ0MSMxNzI4MDAjTVE9PQ=="

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

