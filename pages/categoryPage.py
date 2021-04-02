import sys, os
sys.path.append(os.getcwd())
from pages.basePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class CategoryPage(BasePage):

    title = (By.NAME, "category.title")
    parent = (By.NAME, "category.pid")
    slug = (By.NAME, "category.slug")
    order = (By.NAME, "category.order_number")
    content = (By.NAME, "category.content")
    summary = (By.NAME, "category.summary")
    icon = (By.NAME, "category.icon")
    flag = (By.NAME, "category.flag")
    switch = (By.CLASS_NAME, "switchery-small")
    description = (By.NAME, "category.meta_description")
    keywords = (By.NAME, "category.meta_keywords")

    def __init__(self, driver):
        self.driver = driver

    def input_title(self, text):
        self.input_text(text, *self.title)

    def select_parent(self):
        parent = self.find_element(*self.parent)
        Select(parent).select_by_value("0")

    def input_slug(self, text):
        self.input_text(text, *self.slug)

    def do_order(self, num):
        self.input_text(num, *self.order)

    def input_content(self, text):
        self.input_text(text, *self.content)

    def input_summary(self, text):
        self.input_text(text, *self.summary)

    def input_flag(self, text):
        self.input_text(text, *self.flag)

    def ctrl_dispaly_in_menu(self, status):
        '''
        关闭样式: 
        box-shadow: rgb(223, 223, 223) 0px 0px 0px 0px inset; border-color: rgb(223, 223, 223); background-color: rgb(255, 255, 255); transition: border 0.4s ease 0s, box-shadow 0.4s ease 0s;
        left: 0px; transition: background-color 0.4s ease 0s, left 0.2s ease 0s;
        value="false"
        打开样式:
        box-shadow: rgb(100, 189, 99) 0px 0px 0px 11px inset; border-color: rgb(100, 189, 99); background-color: rgb(100, 189, 99); transition: border 0.4s ease 0s, box-shadow 0.4s ease 0s, background-color 1.2s ease 0s;
        left: 13px; transition: background-color 0.4s ease 0s, left 0.2s ease 0s; background-color: rgb(255, 255, 255);
        value="true"
        '''
        span = self.find_element(*(By.XPATH, "/html/body/div/div/section[2]/div/div[1]/div/form/div[1]/div[9]/div/span"))
        btn = self.find_element(*(By.XPATH, "/html/body/div/div/section[2]/div/div[1]/div/form/div[1]/div[9]/div/span/small"))
        input = self.find_element(*(By.ID, "displayInMenu"))
        close_script = "var span=document.querySelector('body > div > div > section.content > div > div.col-lg-5 > div > form > div.box-body > div:nth-child(9) > div > span');\
            span='box-shadow: rgb(100, 189, 99) 0px 0px 0px 11px inset; border-color: rgb(100, 189, 99); background-color: rgb(100, 189, 99); transition: border 0.4s ease 0s, box-shadow 0.4s ease 0s, background-color 1.2s ease 0s;';\"
        open_script = ""
        if status == "false":
            self.driver.execute_script(close_script)
        elif status == "true":
            self.driver.execute_scipt(open_script)
        else:
            raise Exception(f"status传值错误: {status}")

    def input_description(self, text):
        self.input_text(text, *self.description)

    def input_keyword(self, text):
        self.input_text(text, *self.keywords)


if __name__ == "__main__":
    print(os.getcwd())
    print(sys.path.append(os.getcwd()))