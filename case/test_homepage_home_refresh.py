from common import *


class Homepage_home_refresh(unittest.TestCase):
    log = Log()

    def test_home_open(self):
        """
        首页下拉刷新
        """

        begin_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(begin_date)

        with GMdriver() as driver:
            driver.click_alert()
            time.sleep(2)
            driver.swipe_ios()
            time.sleep(2)
            driver.background_app(3)
        # 首页埋点
        result = mysql_test.query(action='refresh_page', page_name='home', event_time=begin_date)
        assert len(result) == 1, f'埋点数量错误，预期为1个，实际为{len(result)}'


if __name__ == '__main__':
    unittest.main()
