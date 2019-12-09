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
        首页品类聚合->点击玻尿酸
        """

        begin_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(begin_date)

        testbuild = TodolistBuild(self.driver)
        testbuild.click_alert()
        testbuild.click_bns()
        time.sleep(10)
        self.driver.background_app(5)   # 退出后台5秒 ，再次进入app
        time.sleep(10)

        # 首页埋点
        sql_home_open = "select * from maidian_history_data where device_id ='{}' and action = 'home_open' order by event_time desc".format(canshu.dev_id)
        result = canshu.mysql_test.query(sql_home_open)
        end_date_home_open = result[0]['event_time']
        print("home_open: %s" % end_date_home_open)
        if begin_date > end_date_home_open:
            self.log.error("home_open埋点异常")
        else:
            self.log.info("home_open埋点正常")

        sql_device_opened = "select * from maidian_history_data where device_id ='{}' and action = 'device_opened' order by event_time desc".format(
            canshu.dev_id)
        result = canshu.mysql_test.query(sql_device_opened)
        end_date_device_opened = result[0]['event_time']
        end_raw_data = result[0]['raw_data']
        raw_data = json.loads(end_raw_data)
        device_id = raw_data['device']['device_id']
        device_type = raw_data['device']['device_type']
        app_session_id = raw_data['app_session_id']     # 2019.11.27号增加
        app_serial_id = raw_data['app']['serial_id']    # 2019.11.27号增加
        # android_device_id = raw_data['device']['android_device_id']
        params = raw_data['params']
        print("device_opened: %s" % end_date_device_opened)
        if begin_date > end_date_device_opened:
            self.log.error("device_opened埋点异常")
        else:
            self.log.info("device_opened埋点正常")
        assert device_type == canshu.dev_type, 'device_type获取错误！'
        assert device_id == canshu.dev_id, 'device_id获取错误！'
        if params:
            pass
        else:
            self.log.error("params不存在！")

        if app_session_id:    # 2019.11.27号增加
            pass
        else:
            self.log.error("app_session_id不存在！")
        print(app_serial_id)
        print(type(app_serial_id))
        if app_serial_id >= 0 and app_serial_id < 101:       # 2019.11.27号增加
            pass
        else:
            self.log.error("app_serial_id不存在！")

        sql_is_open_push = "select * from maidian_history_data where device_id ='{}' and action = 'is_open_push' order by event_time desc".format(
            canshu.dev_id)
        result = canshu.mysql_test.query(sql_is_open_push)
        end_date_is_open_push = result[0]['event_time']
        end_raw_data = result[0]['raw_data']
        raw_data = json.loads(end_raw_data)
        params_type = raw_data['params']['type']
        print("is_open_push: %s" % end_date_is_open_push)
        if begin_date > end_date_is_open_push:
            self.log.error("is_open_push埋点异常")
        else:
            self.log.info("is_open_push埋点正常")
        # 判断 params_type 存在
        if params_type:
            pass
        else:
            self.log.error("params_type不存在！")

        sql_urban_geographical_location = "select * from maidian_history_data where device_id ='{}' and action = 'urban_geographical_location' order by event_time desc".format(
            canshu.dev_id)
        result = canshu.mysql_test.query(sql_urban_geographical_location)
        end_date_urban_geographical_location = result[0]['event_time']
        print("urban_geographical_location: %s" % end_date_urban_geographical_location)
        if begin_date > end_date_urban_geographical_location:
            self.log.error("urban_geographical_location埋点异常")
        else:
            self.log.info("urban_geographical_location埋点正常")

        time.sleep(10)

if __name__ == '__main__':
    unittest.main()