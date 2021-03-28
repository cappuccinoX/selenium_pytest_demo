from pages.basePage import BasePage
from selenium.webdriver.common.by import By

class ArticleListPage(BasePage):

    article_table = (By.CLASS_NAME, "table-striped")
    rows = (By.TAG_NAME, "tr")

    def __init__(self, driver):
        self.driver = driver

    def check(self, text):
        rows = self.find_elements(*self.rows)
        is_contain = False
        for item in rows:
            if text in (item):
                is_contain = True
                break
        return is_contain