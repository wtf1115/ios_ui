import unittest
import datetime
import time
import json

from gengmei_app.page.basetestcase import Testtodolist
from gengmei_app.page import canshu
from gengmei_app.pageobject.page_todolist_build import TodolistBuild

from gengmei_app.common.Log import Log


class Testbuild4(Testtodolist):

    log = Log()

    def testbuild(self):
        """
        步骤：
        1、美购首页
        2、搜索框
        4、点击热词
        5、切换医生tab
        :return:
        """
        begin_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(begin_date)

        testbuild = TodolistBuild(self.driver)
        testbuild.click_alert()
        testbuild.click_meigou()
        time.sleep(2)
        testbuild.click_welfare_home_search()  # 偶现失败
        testbuild.click_doctor()
        testbuild.click_hot_search()   # 偶现失败
        time.sleep(5)
        self.driver.background_app(5)
        time.sleep(5)

        # 美购搜索 埋点
        sql_search_result_open = "select * from maidian_history_data where device_id ='{}' and action = 'search_result_open' order by event_time desc".format(
            canshu.dev_id)
        result_search_result_open = canshu.mysql_test.query(sql_search_result_open)
        search_result_open_create_time = result_search_result_open[0]['event_time']
        print("search_result_open: %s" % search_result_open_create_time)
        if begin_date > search_result_open_create_time:
            self.log.error("搜索search_result_open埋点异常")
        else:
            self.log.info("搜索search_result_open埋点正常")

        sql_do_search = "select * from maidian_history_data where device_id ='{}' and action = 'do_search' order by event_time desc".format(
            canshu.dev_id)
        result_do_search = canshu.mysql_test.query(sql_do_search)
        do_search_create_time = result_do_search[0]['event_time']
        print("do_search: %s" % do_search_create_time)
        if begin_date > do_search_create_time:
            self.log.error("搜索do_search埋点异常")
        else:
            self.log.info("搜索do_search埋点正常")

        time.sleep(5)


if __name__ == '__main__':
    unittest.main()