import unittest
import datetime
import time
import json

from common.dbMysql import mysql_test
from common.gmdriver import GMdriver

from common.Log import Log


class Homepage_is_open_push(unittest.TestCase):
    log = Log()

    def test_is_open_push(self):
        """
        首页品类聚合->点击玻尿酸
        """

        begin_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(begin_date)

        with GMdriver() as driver:
            driver.background_app(3)
        # 首页埋点
        result = mysql_test.query(action='is_open_push', event_time=begin_date)
        assert len(result) == 1, f'埋点数量错误，预期为1个，实际为{len(result)}'
        end_date_is_open_push = result[0]['event_time']
        end_raw_data = result[0]['raw_data']
        raw_data = json.loads(end_raw_data)
        params_type = raw_data['params']['type']
        print("target埋点: %s" % end_date_is_open_push)
        # 判断 params_type 存在
        if params_type:
            pass
        else:
            self.log.error("params_type不存在！")


if __name__ == '__main__':
    unittest.main()
