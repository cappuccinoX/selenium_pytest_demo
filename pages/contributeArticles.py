from pages.basePage import BasePage
import os
from selenium.webdriver.common.by import By

class ContributeArticlesPage(BasePage):

    article_title = (By.ID, "article-title")
    iframe = (By.CLASS_NAME, "cke_wysiwyg_frame")
    seo_keywords = (By.XPATH, "//*[@id='form']/div/div[1]/div/div[3]/div/div/div[2]/div/div[1]/div/textarea")
    seo_des = (By.XPATH, "//*[@id='form']/div/div[1]/div/div[3]/div/div/div[2]/div/div[2]/div/textarea")
    # 文本编辑框的字体加粗按钮
    bold_btn = (By.ID, "cke_16")
    upload_btn = (By.CLASS_NAME, "fileinput-button")
    upload_box = (By.ID, "cfile")
    rm_picture = (By.ID, "removeThumbnail")
    submit_btn = (By.ID, "submit")

    def __init__(self, driver):
        self.driver = driver
    
    def input_content(self, text):
        iframe_content = self.driver.find_element(*self.iframe)
        self.driver.switch_to.frame(iframe_content)
        self.driver.execute_script(
            "document.getElementsByClassName('cke_editable')[0].innerText='%s'" % text
        )
        self.driver.switch_to.default_content()
    
    def input_title(self, text):
        self.input_text(text, *self.article_title)

    def input_seo_keywords(self, text):
        self.input_text(text, *self.seo_keywords)

    def input_seo_des(self, text):
        self.input_text(text, *self.seo_des)

    def bold_font(self):
        self.click(*self.bold_btn)

    def upload(self, file_name):
        file = "%s/upload_pictures/%s" % (os.path.abspath("data"), file_name)
        upload_input = self.find_element(*self.upload_box)
        upload_input.send_keys(file)

    def remove_picture(self):
        self.click(*self.rm_picture)

    def submit(self):
        self.click(*self.submit_btn)

if __name__ == "__main__":
    print("%s/upload_pictures/%s" % (os.path.abspath("data"), "girl.jpeg"))
