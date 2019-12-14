import unittest
import datetime
import time
import json

from common.dbMysql import mysql_test
from common.gmdriver import GMdriver

from common.Log import Log


class Search_result_wiki_pv(unittest.TestCase):
    log = Log()

    def test_search_result_wiki_pv(self):
        """
        搜索结果页-百科
        """
        begin_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(begin_date)
        with GMdriver() as driver:
            driver.click_alert()
            ele = driver.home_search()
            time.sleep(1)
            ele.send_keys('美莱')
            driver.click_search_button_sys()
            time.sleep(5)
            driver.click_wiki_statictext()
            time.sleep(1)
            driver.background_app(3)

        result = mysql_test.query(action='page_view', page_name='search_result_wiki', event_time=begin_date)
        assert len(result) == 1, f'买点数量错误，预期为1个，实际为{len(result)}'
        end_date_home_open = result[0]['event_time']
        print("target埋点: %s" % end_date_home_open)
        assert len(result) == 1, f'买点数量错误，预期为1个，实际为{len(result)}'


if __name__ == '__main__':
    unittest.main()
