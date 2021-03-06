from common import *


class Homepage_home_open(unittest.TestCase):
    log = Log()

    def test_home_open(self):
        """
        打开app首页
        """

        begin_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(begin_date)

        with GMdriver() as driver:
            driver.background_app(3)
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        # 首页埋点
        result = mysql_test.query(action='home_open', event_time=begin_date)
        assert len(result) == 1, f'埋点数量错误，预期为1个，实际为{len(result)}'


if __name__ == '__main__':
    unittest.main()
