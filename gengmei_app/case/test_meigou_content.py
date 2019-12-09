import unittest
import datetime
import time
import json

from gengmei_app.page.basetestcase import Testtodolist
from gengmei_app.page import canshu
from gengmei_app.pageobject.page_todolist_build import TodolistBuild

from gengmei_app.common.Log import Log


class Testbuild(Testtodolist):

    log = Log()

    def test_01(self):
        """
        美购首页->品类聚合除皱廋脸
        """

        begin_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(begin_date)

        testbuild = TodolistBuild(self.driver)
        testbuild. click_alert()
        testbuild.click_meigou()
        testbuild.click_czsl()
        time.sleep(10)
        self.driver.background_app(5)
        time.sleep(10)

        # 美购品类聚合 埋点
        sql_welfare_home_click_section = "select * from maidian_history_data where device_id ='{}' and action = 'welfare_home_click_section' order by event_time desc".format(
            canshu.dev_id)
        result_welfare_home_click_section = canshu.mysql_test.query(sql_welfare_home_click_section)
        end_welfare_home_click_section_create_time = result_welfare_home_click_section[0]['event_time']
        print("page_view: %s" % end_welfare_home_click_section_create_time)
        if begin_date > end_welfare_home_click_section_create_time:
            self.log.error("welfare_home_click_section埋点异常")
        else:
            self.log.info("welfare_home_click_section埋点正常")


        sql_page_view_welfare_list = "select * from maidian_history_data where device_id ='{}' and action = 'page_view' and page_name = 'welfare_list' order by event_time desc".format(
            canshu.dev_id)
        result_page_view_welfare_list = canshu.mysql_test.query(sql_page_view_welfare_list)
        result_page_view_welfare_list_create_time = result_page_view_welfare_list[0]['event_time']
        result_page_view_welfare_list_all = result_page_view_welfare_list[0]['raw_data']
        page_view_welfare_list = json.loads(result_page_view_welfare_list_all)
        referrer_page_view_welfare_list = page_view_welfare_list['params']['referrer']
        page_name_page_view_welfare_list = page_view_welfare_list['params']['page_name']
        assert referrer_page_view_welfare_list == 'welfare_home', 'referrer获取错误！'
        assert page_name_page_view_welfare_list == 'welfare_list', 'page_name获取错误！'
        print("page_view: %s" % result_page_view_welfare_list_create_time)
        if begin_date > result_page_view_welfare_list_create_time:
            self.log.error("美购品类聚合page_view埋点异常")
        else:
            self.log.info("美购品类聚合page_view埋点正常")
        time.sleep(10)


if __name__ == '__main__':
    unittest.main()