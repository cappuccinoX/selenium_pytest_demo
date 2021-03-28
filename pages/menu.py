from pages.basePage import BasePage
from selenium.webdriver.common.by import By

class Menu(BasePage):

    my_articles = (By.XPATH, "//*[@id='sidebar-menu']/li[4]")
    article_list = (By.XPATH, "//*[@id='sidebar-menu']/li[4]/ul/li[1]/a")
    contribute_aritcles = (By.XPATH, "//*[@id='sidebar-menu']/li[4]/ul/li[2]")

    def click_menu(self, name):
        if name == "my_articles":
            self.click(*self.my_articles)
        elif name == "article_list":
            self.click(*self.article_list)
        elif name == "contribute_aritcles":
            self.click(*self.contribute_aritcles)
        else:
            raise Exception("指定菜单名称'%s'不存在" % name)
