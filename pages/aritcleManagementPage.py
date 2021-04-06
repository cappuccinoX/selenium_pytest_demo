# import os, sys
# sys.path.append(os.getcwd())
from pages.basePage import BasePage
from selenium.webdriver.common.by import By

class AritcleManagementPage(BasePage):

    select_all_ckbox = (By.XPATH, "/html/body/div/div/section[3]/div/div/div/div[2]/table/tbody/tr[1]/th[1]/input")
    delete_all_btn = (By.ID, "batchDel")

    def __init__(self, driver):
        self.driver = driver
        super(AritcleManagementPage, self).__init__(driver)

    def select_all(self):
        self.click(*self.select_all_ckbox)

    def delete_all(self):
        self.click(*self.delete_all_btn)
        alert = self.driver.switch_to.alert
        alert.accept()