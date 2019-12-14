import unittest
import datetime
import time
import json

from common.dbMysql import mysql_test
from common.gmdriver import GMdriver

from common.Log import Log

class Welfare_home_pv(unittest.TestCase):
    log = Log()

    def test_welfare_home_pv(self):
        """
        美购首页
        """

        begin_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(begin_date)

        with GMdriver() as driver:
            driver.click_alert()
            # 点击美购首页
            driver.click_welfare()
            time.sleep(1)
            driver.background_app(5)

        result = mysql_test.query(action='page_view', page_name='welfare_home', event_time=begin_date)
        assert len(result) == 1, f'买点数量错误，预期为1个，实际为{len(result)}'
        page_view_create_time = result[0]['event_time']
        print("target埋点: %s" % page_view_create_time)


if __name__ == '__main__':
    unittest.main()
