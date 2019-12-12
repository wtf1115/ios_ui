import unittest
import datetime
import time
import json

from gengmei_app.page.basetestcase import Testtodolist
from gengmei_app.page import canshu
from gengmei_app.common.gmdriver import TodolistBuild

from gengmei_app.common.Log import Log


class Testbuild(Testtodolist):

    log = Log()

    def test_01(self):
        """
        美购首页->品类聚合除皱廋脸
        :return:
        """

        begin_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(begin_date)

        testbuild = TodolistBuild(self.driver)
        testbuild. click_alert()

        # 点击美购首页
        testbuild.click_meigou()

        time.sleep(10)
        self.driver.background_app(5)
        time.sleep(10)

        # 美购首页 埋点
        sql_page_view = "select * from maidian_history_data where device_id ='{}' and action = 'page_view' and page_name = 'welfare_home' order by create_time desc".format(
            canshu.dev_id)
        result = canshu.mysql_test.query(sql_page_view)
        page_view_create_time = result[0]['create_time']
        page_view_raw_data_all = result[0]['raw_data']
        page_view_raw_data = json.loads(page_view_raw_data_all)
        page_view_referrer = page_view_raw_data['params']['referrer']
        page_view_page_name = page_view_raw_data['params']['page_name']
        assert page_view_referrer == 'home', 'referrer获取错误！'
        assert page_view_page_name == 'welfare_home', 'page_name获取错误！'
        print("page_view: %s" % page_view_create_time)
        if begin_date > page_view_create_time:
            self.log.error("美购首页page_view埋点异常")
        else:
            self.log.info("美购首页page_view埋点正常")
        time.sleep(10)


        time.sleep(3)
        # 进入品类聚合
        testbuild.click_czsl()

        time.sleep(10)
        self.driver.background_app(5)
        time.sleep(10)


        # 美购品类聚合 埋点
        sql_welfare_home_click_section = "select * from maidian_history_data where device_id ='{}' and action = 'welfare_home_click_section' order by create_time desc".format(
            canshu.dev_id)
        result_welfare_home_click_section = canshu.mysql_test.query(sql_welfare_home_click_section)
        end_welfare_home_click_section_create_time = result_welfare_home_click_section[0]['create_time']
        print("page_view: %s" % end_welfare_home_click_section_create_time)
        if begin_date > end_welfare_home_click_section_create_time:
            self.log.error("welfare_home_click_section埋点异常")
        else:
            self.log.info("welfare_home_click_section埋点正常")


        sql_page_view_welfare_list = "select * from maidian_history_data where device_id ='{}' and action = 'page_view' and page_name = 'welfare_list' order by create_time desc".format(
            canshu.dev_id)
        result_page_view_welfare_list = canshu.mysql_test.query(sql_page_view_welfare_list)
        result_page_view_welfare_list_create_time = result_page_view_welfare_list[0]['create_time']
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