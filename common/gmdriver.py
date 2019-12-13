from appium import webdriver
from common.basepage import BasePage
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait  # added by longshu on 2019-12-06


class GMdriver(BasePage):
    gengmei_alert = (By.ID, "com.wanmeizhensuo.zhensuo:id/dialog_home_img_cancel")
    gengmei_ai = "com.wanmeizhensuo.zhensuo:id/item_home_area_single_iv"
    ai_scanface = (By.ID, "com.wanmeizhensuo.zhensuo:id/face_ai_analysis_tv")
    ai_photo = (By.ID, "com.wanmeizhensuo.zhensuo:id/take_photo_album_img")
    ai_phoneselect = "android.widget.RelativeLayout"
    gengmei_anly = (By.ID, "com.wanmeizhensuo.zhensuo:id/jump_over_tv")
    report_back = (By.ID, "com.wanmeizhensuo.zhensuo:id/header_back_iv")
    gengmei_scanagain = (By.ID, "com.wanmeizhensuo.zhensuo:id/face_result_tv_once_again")
    report_share = (By.ID, "com.wanmeizhensuo.zhensuo:id/face_result_iv_share")
    gengmei_skin = (By.ID, "com.wanmeizhensuo.zhensuo:id/face_result_tv_skin")
    popup_x_xpath_ios = (By.XPATH, '//XCUIElementTypeApplication[@name="更美TEST"]/XCUIElementTypeWindow[1]/XCUIElemen'
                                   'tTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIEleme'
                                   'ntTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeImage')

    def __init__(self):

        self.desired_caps = {
            "deviceName": "iPhone",
            "platformName": "iOS",
            "plarformVersion": "13.0",
            "bundleId": "com.wanmeizhensuo.ZhengXing",
            "automationName": "XCUITest",
            "udid": "00008030-00021D880A08802E"
        }
        i = 0
        while i < 5:
            try:
                self.driver = webdriver.Remote("http://localhost:4723/wd/hub", self.desired_caps)
                break
            except:
                time.sleep(3)
                i += 1
        else:
            raise Exception('Error: Fail to get driver!')
        self.waiter = WebDriverWait(self.driver, 20)
        self.click_alert()
        super().__init__(self.driver)

    def click_alert(self):
        """
        关闭首页广告业
        :return:
        """
        try:
            self.waiter.until(lambda x: self.driver.find_element_by_xpath(self.popup_x_xpath_ios[1])).click()
        except:
            'do nothing'

    def click_ai(self):
        """
        点击首页更美ai豆腐块
        :return:
        """
        self.find_elements(By.ID, self.gengmei_ai, num=2).click()

    def click_gengmei_photo(self):
        """
        选择照片侧颜值
        :return:
        """
        self.click(*self.ai_photo)

    def select_photo(self):
        """
        从相册选择一张照片
        :return:
        """
        self.find_elements(By.CLASS_NAME, self.ai_phoneselect, num=2).click()

    def dump_analyse(self):
        """
        跳过面部分析板块
        :return:
        """
        time.sleep(5)
        self.click(*self.gengmei_anly)

    def ai_report_back(self):
        """
        进入混合型报告页
        点击退出，退出到测服，扫脸页
        :return:
        """
        time.sleep(30)
        self.click(*self.report_back)

    def ai_again(self):
        """
        进入测服结果页
        点击再测一次
        :return:
        """
        self.click(*self.gengmei_scanagain)

    def ai_share(self):
        """
        进入报告页
        点击炫耀肌龄，也就是分享
        :return:
        """
        self.click(*self.report_share)

    def ai_switch_skin(self):
        """
        进入报告页
        点击颜值分析，也就是扫脸
        :return:
        """
        self.click(*self.gengmei_skin)

    def home_search(self):
        """
        点击首页搜索
        :return:
        """

        self.waiter.until(lambda x: self.driver.find_element_by_xpath("(//XCUIElementTypeStaticText)[2]")).click()

    def click_bns(self):
        """
        首页点击玻尿酸
        :return:
        """
        self.waiter.until(lambda x: self.driver.find_element_by_xpath(
            '(//XCUIElementTypeStaticText[@name="玻尿酸"])[1]/..')).click()

    def click_meigou(self):
        """
        点击美购首页
        :return:
        """
        self.waiter.until(
            lambda x: self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="美购"]')).click()

    def click_czsl(self):
        """
        点击美购里的除皱廋脸
        :return:
        """
        self.waiter.until(
            lambda x: self.driver.find_element_by_xpath('(//XCUIElementTypeStaticText[@name="除皱瘦脸"])[1]/..')).click()

    def click_search(self):
        """
        点击美购品类聚合里面的搜索
        :return:
        """
        #  点击搜索
        self.waiter.until(
            lambda x: self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="搜索项目、美购、医生"]')).click()

    def click_hot_search(self):
        """
        点击第一个热搜内容
        :return:
        """

        self.waiter.until(lambda x: self.driver.find_element_by_xpath(
            '//XCUIElementTypeStaticText[@name="搜索发现"]/../../XCUIElementTypeButton[1]')).click()

    def click_diary(self):
        """
        美购搜索中点击日记
        :return:
        """
        self.waiter.until(
            lambda x: self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="日记"]')).click()

    def click_content(self):
        """
        美购搜索中点击综合
        :return:
        """
        self.waiter.until(
            lambda x: self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="综合"]')).click()

    def click_wiki(self):
        """
        点击百科
        :return:
        """
        self.waiter.until(
            lambda x: self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="百科"]')).click()

    def click_tractate(self):
        """
        点击帖子
        :return:
        """
        self.waiter.until(
            lambda x: self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="帖子"]')).click()

    def click_hospital(self):
        """
        点击医院
        :return:
        """

        self.waiter.until(
            lambda x: self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="医院"]')).click()

    def click_doctor(self):
        """
        点击医生
        :return:
        """
        self.waiter.until(
            lambda x: self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="医生"]')).click()

    def click_shopping_cart(self):
        """
        点击美购首页、购物车
        :return:
        """
        try:
            time.sleep(3)
            shopping = "com.wanmeizhensuo.zhensuo:id/common_red_iv"
            self.driver.find_element_by_id(shopping).click()
        except Exception as e:
            print("找不到元素 %s,%d" % (e, 1))
        finally:
            try:
                time.sleep(3)
                shopping = 'com.wanmeizhensuo.zhensuo:id/titleBarWelfareHome_rl_shopping_cart'
                self.driver.find_element_by_id(shopping).click()
                time.sleep(3)
            except Exception as e:
                print("找不到元素 %s,%d" % (e, 2))
            finally:
                try:
                    time.sleep(3)
                    shopping = '//android.widget.RelativeLayout[@resource-id="com.wanmeizhensuo.zhensuo:id/common_red_iv"]'
                    self.driver.find_element_by_android_uiautomator(shopping).click()
                    time.sleep(3)
                except Exception as e:
                    print("找不到元素 %s,%d" % (e, 3))
                finally:
                    print("继续下一步")
                    time.sleep(5)

    def click_welfare_home_search(self):
        """
        点击美购首页搜索
        :return:
        """
        #  点击搜索
        self.waiter.until(lambda x: self.driver.find_element_by_xpath("(//XCUIElementTypeStaticText)[2]/..")).click()

    def __enter__(self):
        # 调试覆盖，有可能失败

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.driver.quit()
        if exc_type:
            raise Exception(exc_val)

        time.sleep(10)


