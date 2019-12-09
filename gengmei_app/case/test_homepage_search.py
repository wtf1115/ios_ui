import unittest
import time
import datetime

from gengmei_app.page.basetestcase import Testtodolist
from gengmei_app.pageobject.page_todolist_build import TodolistBuild
from gengmei_app.page import canshu

from gengmei_app.common.Log import Log


class Testbuild(Testtodolist):

    log = Log()

    def test_01(self):
        """
        点击首页搜索
        """
        testbuild = TodolistBuild(self.driver)
        testbuild.click_alert()

        time.sleep(2)

        begin_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(begin_date)

        testbuild.home_search()

        time.sleep(2)
        self.driver.background_app(5)

        on_click_navbar_search = "select * from maidian_history_data where device_id ='{}' and action = 'on_click_navbar_search' order by event_time desc".format(
            canshu.dev_id)
        result = canshu.mysql_test.query(on_click_navbar_search)
        end_date_home_open = result[0]['event_time']
        print("on_click_navbar_search: %s" % end_date_home_open)
        if begin_date > end_date_home_open:
            self.log.error("on_click_navbar_search埋点异常")
        else:
            self.log.info("on_click_navbar_search埋点正常")
        time.sleep(3)


if __name__ == '__main__':
    unittest.main()