import unittest
import datetime
import time
import json

from common.dbMysql import mysql_test
from common.gmdriver import GMdriver

from common.Log import Log

class Welfare_list_pv(unittest.TestCase):
    log = Log()

    def test_welfare_list_pv(self):
        """
        美购首页->品类聚合除皱廋脸
        """

        begin_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(begin_date)

        with GMdriver() as driver:
            driver.click_alert()
            driver.click_welfare_home()
            time.sleep(1)
            driver.click_czsl()
            time.sleep(1)
            driver.background_app(5)

        #美购首页点击 聚合标签
        result_page_view_welfare_list = mysql_test.query(action='page_view', page_name='welfare_list',
                                                         event_time=begin_date)
        assert len(result_page_view_welfare_list) == 1, f'买点数量错误，预期为1个，实际为{len(result_page_view_welfare_list)}'
        result_page_view_welfare_list_create_time = result_page_view_welfare_list[0]['event_time']
        result_page_view_welfare_list_all = result_page_view_welfare_list[0]['raw_data']
        page_view_welfare_list = json.loads(result_page_view_welfare_list_all)
        referrer_page_view_welfare_list = page_view_welfare_list['params']['referrer']
        assert referrer_page_view_welfare_list == 'welfare_home', 'referrer获取错误！'
        print("target埋点: %s" % result_page_view_welfare_list_create_time)


if __name__ == '__main__':
    unittest.main()
