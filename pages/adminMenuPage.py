import sys, os
sys.path.append(os.getcwd())
from pages.basePage import BasePage
from selenium.webdriver.common.by import By

class AdminMenuPage(BasePage):

    article = (By.XPATH, "//*[@id='sidebar-menu']/li[4]/a")
    category = (By.XPATH, "//*[@id='sidebar-menu']/li[4]/ul/li[3]/a")
    add_article = (By.XPATH, "//*[@id='sidebar-menu']/li[4]/ul/li[2]/a")
    article_management = (By.XPATH, "//*[@id='sidebar-menu']/li[4]/ul/li[1]/a")

    def __init__(self, driver):
        super(AdminMenuPage, self).__init__(driver)

    def click_aritcle(self):
        self.click(*self.article)

    def click_category(self):
        self.wait_ele_visiable(self.category, "分类", 3)
        self.click(*self.category)
    
    def click_add_article(self):
        self.wait_ele_visiable(self.add_article, "写文章", 3)
        self.click(*self.add_article)

    def click_article_manage(self):
        self.wait_ele_visiable(self.article_management)
        self.click(*self.article_management)
