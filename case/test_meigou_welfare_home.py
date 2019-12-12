import unittest
import datetime
import time
import json

from gengmei_app.common.dbMysql import mysql_test
from gengmei_app.common.gmdriver import GMdriver

from gengmei_app.common.Log import Log


class Meigou_welfare_home(unittest.TestCase):
    log = Log()

    def test_welfare_home(self):
        """
        美购首页
        """

        begin_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(begin_date)

        with GMdriver() as driver:
            driver.click_alert()
            # 点击美购首页
            driver.click_meigou()
            time.sleep(1)
            driver.background_app(5)

        result = mysql_test.query(action='page_view', page_name='welfare_home', event_time=begin_date)
        assert len(result) == 1, f'买点数量错误，预期为1个，实际为{len(result)}'
        page_view_create_time = result[0]['event_time']
        print("page_view: %s" % page_view_create_time)
        page_view_raw_data_all = result[0]['raw_data']
        page_view_raw_data = json.loads(page_view_raw_data_all)
        print(page_view_raw_data)
        page_view_referrer = page_view_raw_data['params']['referrer']
        page_view_page_name = page_view_raw_data['params']['page_name']
        assert page_view_referrer == 'home', 'referrer获取错误！实际：{}'.format(page_view_referrer)
        assert page_view_page_name == 'welfare_home', 'page_name获取错误！实际：{}'.format(page_view_page_name)


if __name__ == '__main__':
    unittest.main()
