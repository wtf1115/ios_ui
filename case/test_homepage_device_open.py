import unittest
import datetime
import time
import json

from common.dbMysql import mysql_test
from common.gmdriver import GMdriver

from common.Log import Log

class Homepage_device_open(unittest.TestCase):
    log = Log()

    def test_device_open(self):
        """
        首页品类聚合->点击玻尿酸
        """

        begin_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(begin_date)

        with GMdriver() as driver:
            driver.background_app(3)
        # 首页埋点
        result = mysql_test.query(action='device_opened', event_time=begin_date)
        assert len(result) > 1, f'买点数量错误，预期为1个，实际为{len(result)}'
        end_date_device_opened = result[0]['event_time']
        end_raw_data = result[0]['raw_data']
        raw_data = json.loads(end_raw_data)

        app_session_id = raw_data['app_session_id']  # 2019.11.27号增加
        app_serial_id = raw_data['app']['serial_id']  # 2019.11.27号增加
        # android_device_id = raw_data['device']['android_device_id']
        params = raw_data['params']
        print("target埋点: %s" % end_date_device_opened)
        if params:
            pass
        else:
            self.log.error("params不存在！")

        if app_session_id:  # 2019.11.27号增加
            pass
        else:
            self.log.error("app_session_id不存在！")
        print(app_serial_id)
        print(type(app_serial_id))
        if app_serial_id >= 0 and app_serial_id < 101:  # 2019.11.27号增加
            pass
        else:
            self.log.error("app_serial_id不存在！")

if __name__ == '__main__':
    unittest.main()
