import sys
# sys.path.append(r'/Users/xuyaogang/myProjects/python/selenium_pytest_demo/')
import random
import string
import time
import os
from PIL import Image
import pytesseract
from lib.ShowapiRequest import ShowapiRequest
import logging
import datetime
import logging.handlers

def get_random_str():
    rand_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    return rand_str

def save_screenshot(driver):
    st = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
    filename = st + '.png'
    dirname = os.path.abspath("screenshots")
    driver.save_screenshot("%s/%s" % (dirname, filename))

'''
使用pytesseract获取验证码
1. 截屏这个页面
2. 获取验证码坐标数据
3. 根据坐标数据抠图
4. 使用pytesseract模块验证
'''
def get_code_with_pytesseract(driver, locator, type):
    code_ele = None
    if type == "id":
        code_ele = driver.find_element_by_id(locator)
    elif type == "class":
        code_ele = driver.find_element_by_class_name(locator)
    elif type == "name":
        code_ele = driver.find_element_by_name(locator)
    elif type == "xpath":
        code_ele = driver.find_element_by_xpath(locator)
    else:
        raise RuntimeError("不可用的定位类型: %s" % type)

    st = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
    dirname = os.path.abspath("code_screenshots")
    file_name = 'fullscreen_' + st + '.png'
    driver.get_screenshot_as_file("%s/%s" % (dirname, file_name))

    # 获取验证码图片左顶点和右底点坐标
    left = code_ele.location["x"]
    top = code_ele.location["y"]
    right = code_ele.size["width"] + left
    height = code_ele.size["height"] + top

    im = Image.open("%s/%s" % (dirname, file_name))
    # 解决因分辨率问题导致抠图结果为空白图
    dpr = driver.execute_script('return window.devicePixelRatio')
    # 抠图
    code_image = im.crop((left*dpr, top*dpr, right*dpr, height*dpr))
    code_image_name = dirname + '/code_' + st + '.png'
    code_image.save(code_image_name)
    # 获取图片文字
    code_image_1 = Image.open(code_image_name)
    # 目前会报错, tesseract 没有配置好
    code = pytesseract.image_to_string(code_image_1)
    return code

# 使用第三方插件获取验证码
def get_code():
    dir_path = os.path.abspath("code_screenshots")
    file_path = dir_path + '/code_2021-03-14-14-11-09.png'
    r = ShowapiRequest(
        "http://route.showapi.com/184-4",
        "564736",
        "f2283f5fda2743b19447c29c6dbe421c"
    )
    print(file_path)
    r.addFilePara("image", file_path)
    r.addBodyPara("typeId", "34")
    r.addBodyPara("convert_to_jpg", "0")
    r.addBodyPara("needMorePrecise", "0")
    res = r.post()
    text = res.json()['showapi_res_body']
    code = text['Result']
    return code

    

if __name__ == "__main__":
    logger = get_logger()
    logger.error('error.log')
    logger.warning("warn log")
    logger.info("info log")
    logger.debug("debug log")
    logger.critical("critical log")