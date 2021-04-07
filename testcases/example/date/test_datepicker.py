from selenium import webdriver
import pytest
import os
from time import sleep
import random

class TestDatePicker():

    def test_1(self):
        driver = webdriver.Chrome()
        driver.get("https://hotels.ctrip.com/")
        driver.maximize_window()
        sleep(4)
        calendar = driver.find_element_by_xpath("//*[@id='ibu_hotel_container']/div[1]/div[1]/div[3]/div/div/ul/li[2]/div/div[1]/input")
        print(f"\ncalendar: {calendar}")
        calendar.click()
        calendar_month = driver.find_elements_by_class_name("c-calendar-month")
        print(f"\nmonth length: {len(calendar_month)}")
        # 获取所有可选的check-in date
        available_checkin_days = calendar_month[0].find_elements_by_class_name("is-allow-hover")
        print(f"\navailable_checkin_days length: {len(available_checkin_days)}")
        # 任意选择可选的check-in date
        idx = random.randint(0, len(available_checkin_days))
        available_checkin_days[idx].click()
        # 获取所有可选的check-out date
        available_checkout_days = calendar_month[1].find_elements_by_class_name("is-allow-hover")
        # 任意选择可选的check-out date
        idx = random.randint(0, len(available_checkout_days))
        available_checkout_days[idx].click()

    # 移除readonly属性
    def test_2(self):
        driver = webdriver.Chrome()
        driver.get("https://hotels.ctrip.com/")
        driver.maximize_window()
        sleep(4)
        js = "document.querySelector('#ibu_hotel_container > div.m-homePage.m-hbuPage > div.top > div.inner-page > div > div > ul > li.list-item.li-item-calendar.list-calendar > div > div:nth-child(1) > input').removeAttribute('readonly')"
        driver.execute_script(js)
        return

if __name__ == "__main__":
    pytest.main(["-s", "-v", "%s/example/date/test_datepicker.py" % os.path.abspath("testcases")])
