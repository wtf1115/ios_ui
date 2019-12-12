import unittest
import datetime
import time
import json

from gengmei_app.common.dbMysql import mysql_test
from gengmei_app.common.gmdriver import GMdriver

from gengmei_app.common.Log import Log


class Homepage_category(unittest.TestCase):
    log = Log()

    # 不必重构setup，Testtodolist中对driver已经获取！

    def test_category(self):
        """
        首页品类聚合->点击玻尿酸
        """
        # self._testMethodDoc
        begin_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(begin_date)
        with GMdriver() as driver:
            driver.click_alert()
            driver.click_bns()
            time.sleep(1)
            # 切换到后台
            driver.background_app(5)

        # sql_page_view2 = "select * from maidian_history_data where device_id ='{}' and action = 'page_view'" \
        #                  " and page_name = 'category'  and event_time > '{}' order by event_time desc".format(canshu.dev_id,begin_date)

        result = mysql_test.query(action='page_view', page_name='category', event_time=begin_date)
        print(result)
        assert len(result) == 1, f'买点数量错误，预期为1个，实际为{len(result)}'
        end_raw_data = result[0]['raw_data']
        raw_data = json.loads(end_raw_data)
        referrer = raw_data['params']['referrer']
        page_name = raw_data['params']['page_name']
        assert referrer == 'home', 'referrer获取错误！'
        assert page_name == 'category', 'page_name获取错误！'


if __name__ == '__main__':
    unittest.main()
