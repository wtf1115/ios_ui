from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
import time

import os.path
from common.logger import Logger

logger = Logger(logger="BasePage").getlog()


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    def back(self):
        self.driver.back()
        logger.info("退出")

    def close(self):
        self.driver.close()

    def move(self, *loc):

        elem = self.find_element(*loc)
        elem1 = self.find_element(*loc)
        try:
            ActionChains(self.driver).move_to_element(elem).click(elem1).perform()
            logger.info("The element  was moved and clicked.")
        except Exception as e:
            logger.error("Faild to move and click the element ")

    def forward(self):
        self.driver.forward()

    def frame(self, loc):
        self.driver.switch_to.frame(loc)

    def open_url(self, url):

        self.driver.get(url)

    def quit_browser(self):

        self.driver.quit()

    def find_element(self, *loc):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
            logger.info("找到页面元素%s", *loc)
        except:
            logger.error("%s 页面中未能找到%s元素" % (self, loc))

    # 保存图片
    def get_windows_img(self):
        file_path = os.path.dirname(os.path.abspath('.')) + '/screenshots/'
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info('获取路径及文件名成功，如果报错将保存到：/screenshots/')
        except Exception as e:
            logger.error('出现报错现象，已保存截图！%s', e)

    # 输入
    def sendkeys(self, text, *loc):
        elem = self.find_element(*loc)
        elem.clear()
        try:
            elem.send_keys(text)
        except Exception as e:
            self.get_windows_img()

    # 清除文本框
    def clear(self, *loc):
        elem = self.find_element(*loc)
        try:
            elem.clear()
        except Exception as e:
            self.get_windows_img()

    # 点击元素
    def click(self, *loc):
        elem = self.find_element(*loc)
        try:
            elem.click()
            logger.info("The element was clicked.")
        except Exception as e:
            logger.error("Faild to click the element ")

    def js(self, script):
        # 执行js脚本
        self.driver.execute_script(script)
        logger.info("正在执行JS脚本")

    def wait(self, secs):
        # 隐式等待
        self.driver.implicitly_wait(secs)
        logger.info("隐式等待")

    def wait_click_element(self, locator):
        # 显示等待
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.element_to_be_clickable(locator))

    def switch_to_frame(self, n=0):
        """选择iframe"""
        n = int(n)
        self.driver.switch_to.frame(self.driver.find_elements_by_tag_name("iframe")[n])
        logger.info("切换iframe框架")

    def longpress(self, *loc):
        elem = self.find_element(*loc)
        try:
            action1 = TouchAction(self.driver)
            action1.long_press(elem).wait(10000).perform()
            logger.info("The element  was  longpress.")
        except Exception as e:
            logger.error("Faild to longpress the element ")

    def find_elements(self, by, locator, num):
        if by in [By.CLASS_NAME, By.ID, By.XPATH]:
            WebDriverWait(self.driver, 10, 0.3).until(EC.visibility_of_element_located((by, locator)))
            logger.info("successs to find the element")
            return self.driver.find_elements(by, locator)[num]
        else:
            print('定位方式不推荐')
            raise NameError("Faild to find the elements")

    def background_app(self, t):
        self.driver.background_app(t)

    def swipe_ios(self):
        # 这地方仅做简单滑动，不再支持动态传参
        size = self.driver.get_window_size()
        x, y = size['width'], size['height']
        self.driver.execute_script("mobile:dragFromToForDuration",
                                   {"duration": 0.5, "element": None, "fromX": int(x / 4), "fromY": int(y / 4),
                                    "toX": int(3 * x / 4), "toY": int(3 * y / 4)})
