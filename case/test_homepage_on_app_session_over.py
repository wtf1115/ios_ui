import unittest
import datetime
import time
import json

from common.dbMysql import mysql_test
from common.gmdriver import GMdriver

from common.Log import Log


class Homepage_on_app_session_over(unittest.TestCase):
    log = Log()

    def test_on_app_session_over(self):
        """
        首页, 退出
        """

        begin_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(begin_date)

        with GMdriver() as driver:
            driver.background_app(3)

        result = mysql_test.query(action='on_app_session_over', event_time=begin_date)
        assert len(result) == 1, f'买点数量错误，预期为1个，实际为{len(result)}'
        end_page_view = result[0]['event_time']
        end_raw_data = result[0]['raw_data']
        raw_data = json.loads(end_raw_data)
        app_serial_id = raw_data['app']['serial_id']
        params_duration = raw_data['params']['duration']
        app_session_id = raw_data['app_session_id']
        print("on_app_session_over: %s" % end_page_view)
        if app_serial_id:
            pass
        else:
            self.log.error("app_serial_id不存在！")

        if params_duration:
            pass
        else:
            self.log.error("params_duration不存在！")

        if app_session_id:
            pass
        else:
            self.log.error("app_session_id不存在！")

        time.sleep(10)


if __name__ == '__main__':
    unittest.main()
