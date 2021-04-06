# import os, sys
# sys.path.append(os.getcwd())
from pages.basePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class AddArticlePage(BasePage):

    title = (By.CLASS_NAME, "article-title")
    iframe = (By.CLASS_NAME, "cke_wysiwyg_frame cke_reset")
    textarea = (By.XPATH, "/html/body")
    submit_btn = (By.XPATH, "//*[@id='form']/div/div[2]/div[1]/div/button[1]")
    script_btn = (By.XPATH, "//*[@id='form']/div/div[2]/div[1]/div/button[2]")

    def __init__(self, driver):
        self.driver = driver
        super(AddArticlePage, self).__init__(driver)

    def input_title(self, text):
        self.input_text(text, *self.title)

    def input_content(self, content):
        iframe = self.find_element(*self.iframe)
        self.driver.switch_to.frame(iframe)
        textarea = self.find_element(*self.textarea)
        textarea.send_keys(content)
        # 全部选中
        textarea.send_keys(Keys.CONTROL + 'a')
        self.driver.switch_to.default_content()
        # 内容加粗
        bold_btn = self.find_element(*(By.ID, "cke_16"))
        bold_btn.click()

    def submit(self):
        self.click(*self.submit_btn)
