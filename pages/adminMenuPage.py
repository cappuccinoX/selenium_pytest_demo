import sys, os
sys.path.append(os.getcwd())
from pages.basePage import BasePage
from selenium.webdriver.common.by import By

class AdminMenuPage(BasePage):

    article = (By.XPATH, "//*[@id='sidebar-menu']/li[4]/a")
    category = (By.XPATH, "//*[@id='sidebar-menu']/li[4]/ul/li[3]/a")

    def __init__(self, driver):
        self.driver = driver

    def click_aritcle(self):
        self.click(*self.article)

    def click_category(self):
        self.wait_ele_visiable(*self.category, "分类", 3)
        self.click(*self.category)