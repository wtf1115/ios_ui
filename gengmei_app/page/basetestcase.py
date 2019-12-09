from appium import webdriver
import os
import unittest

apk_path = os.path.dirname(os.path.abspath("."))


class Testtodolist(unittest.TestCase):
    def setUp(self):
        # desired_caps = {}
        # desired_caps['platformName'] = 'Android'
        # desired_caps['platformVersion'] = '9'
        # desired_caps['deviceName'] = '6f2efb81'
        # desired_caps['androidDeviceReadyTimeout'] = '20'
        # desired_caps['sessionOverride'] = True
        # desired_caps['noReset'] = True
        # desired_caps['appPackage'] = 'com.wanmeizhensuo.zhensuo'  # 程序包名
        # desired_caps['appActivity'] = '.module.MainActivity'  # 启动类名
        # desired_caps['unicodeKeyboard'] = True  # 安装一个中文输入法
        # desired_caps['waitappActivity'] = '.module.MainActivity'
        # desired_caps['noReset'] = True

        desired_caps = {
            "deviceName": "iPhone",
            "platformName": "iOS",
            "plarformVersion": "13.0",
            "bundleId": "com.wanmeizhensuo.ZhengXing",
            "automationName": "XCUITest",
            "udid": "00008030-00021D880A08802E"
        }

        # 调试覆盖
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
