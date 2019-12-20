from common import *


class Home_pv(unittest.TestCase):
    log = Log()

    def test_home_pv(self):
        """
        首页品类聚合->点击玻尿酸
        """

        begin_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(begin_date)

        with GMdriver() as driver:
            driver.click_alert()
            time.sleep(1)
            driver.background_app(3)
        # 首页埋点R
        result = mysql_test.query(action='page_view', page_name='home', event_time=begin_date)
        assert len(result) == 1, f'埋点数量错误，预期为1个，实际为{len(result)}'


if __name__ == '__main__':
    unittest.main()
