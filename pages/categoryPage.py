import sys, os
# sys.path.append(os.getcwd())
from pages.basePage import BasePage
from pages.iconPage import IconPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

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
    icon_help_link = (By.XPATH, "/html/body/div/div/section[2]/div/div[1]/div/form/div[1]/div[7]/div/p/a")
    submit_btn = (By.CLASS_NAME, "btn-primary")
    table = (By.CLASS_NAME, "table-striped")
    table_rows = (By.CLASS_NAME, "jp-actiontr")

    def __init__(self, driver):
         super(CategoryPage, self).__init__(driver)
         self.icon_page = IconPage(driver)

    def input_title(self, text):
        self.input_text(text, *self.title)

    def select_parent(self, value):
        parent = self.find_element(*self.parent)
        Select(parent).select_by_value(value)

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
        ele = self.find_element(*(By.ID, "displayInMenu"))
        value = ele.get_attribute("value")
        if status.lower() != value:
            self.click(*self.switch)

    def input_description(self, text):
        self.input_text(text, *self.description)

    def input_keyword(self, text):
        self.input_text(text, *self.keywords)

    def input_icon(self):
        self.click(*self.icon_help_link)
        all_handles = self.driver.window_handles
        self.driver.switch_to_window(all_handles[1])
        icon = self.icon_page.fetch_icon()
        self.driver.switch_to_window(all_handles[0])
        self.input_text(icon, *self.icon)

    def submit(self):
        self.click(*self.submit_btn)
        
    def delete_one_title(self, row, title):
        target = self.driver.find_element_by_link_text(title)
        ActionChains(self.driver).move_to_element(target).perform()
        self.driver.find_element_by_xpath(f"/html/body/div/div/section[2]/div/div[2]/div/div[2]/table/tbody/tr[{row}]/td[1]/div/div/a[2]").click()
        alert = self.driver.switch_to.alert
        alert.accept()




if __name__ == "__main__":
    print(os.getcwd())
    print(sys.path.append(os.getcwd()))