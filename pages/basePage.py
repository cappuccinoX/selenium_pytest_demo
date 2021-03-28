from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from util.logger import Logger
import time
import os

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.logger = Logger().get_logger()

    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    def find_elements(self, *loc):
        return self.driver.find_elements(*loc)

    def input_text(self, text, *loc):
        self.clear(*loc)
        self.find_element(*loc).send_keys(text)

    def click(self, *loc):
        self.find_element(*loc).click()

    def clear(self, *loc):
        self.find_element(*loc).clear()

    def get_title(self):
        return self.driver.title

    def wait_ele_visiable(self, loc, des, timeout = 3):
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(loc))
            self.logger.info("等待:{} - 元素{}可见成功。".format(des, loc))
        except Exception:
            self.logger.error("等待:{} - 元素{}可见失败！".format(des, loc))
            raise
    
    def save_img(self):
        now = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
        img_dir = os.path.abspath("screenshots") + "/failure"
        img_path = os.path.join(img_dir, now + '.png')
        try:
            self.driver.save_screenshot(img_path)
        except Exception:
            self.logger.error("截图异常")
        else:
            self.logger.info("异常截图成功，截图存放在{}".format(img_path))

if __name__ == "__main__":
    BasePage(webdriver).save_img()