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
        # self._testMethodDoc
        begin_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(begin_date)

        testbuild = TodolistBuild(self.driver)
        testbuild.click_alert()
        testbuild.click_bns()
        time.sleep(2)
        self.driver.background_app(5)

        sql_page_view2 = "select * from maidian_history_data where device_id ='{}' and action = 'page_view'" \
                         " and page_name = 'category'  order by create_time desc".format(canshu.dev_id)

        result2 = canshu.mysql_test.query(sql_page_view2)
        end_page_view2 = result2[0]['create_time']
        end_raw_data2 = result2[0]['raw_data']
        raw_data2 = json.loads(end_raw_data2)
        referrer2 = raw_data2['params']['referrer']
        page_name2 = raw_data2['params']['page_name']
        assert referrer2 == 'home', 'referrer获取错误！'
        assert page_name2 == 'category', 'page_name获取错误！'
        print("page_view: %s" % end_page_view2)
        if begin_date > end_page_view2:
            self.log.error("page_view埋点异常")
        else:
            self.log.info("page_view埋点正常")

        time.sleep(10)


if __name__ == '__main__':
    unittest.main()
