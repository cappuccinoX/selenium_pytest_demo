from pages.basePage import BasePage
from selenium.webdriver.common.by import By
import random

class IconPage(BasePage):

    icon_list = (By.ID, "fa-icons")

    def __init__(self, driver):
        super(IconPage, self).__init__(driver)

    def fetch_icon(self):
        all_sections = self.find_elements(*(By.XPATH, "//*[@id='fa-icons']/section"))
        self.logger.info(f"section lenth: {len(all_sections)}")
        url = self.driver.current_url
        self.logger.info(f"url: {url}")
        sec_idx = random.randint(0, len(all_sections))
        sec = all_sections[sec_idx]
        self.logger.info("选择图标类型: %s" % sec.get_attribute("id"))

        childs = sec.find_elements_by_class_name("col-sm-4")
        icon_idx = random.randint(0, len(childs))
        icon_text = childs[icon_idx].text
        self.logger.info(f"选择图标类型: {icon_text}")
        return icon_text
    