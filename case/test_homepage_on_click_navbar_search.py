from common import *


class Homepage_on_click_navbar_search(unittest.TestCase):
    log = Log()

    def test_on_click_navbar_search(self):
        """
        点击首页搜索框
        """
        begin_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(begin_date)
        with GMdriver() as driver:
            driver.click_alert()
            driver.home_search()
            time.sleep(1)
            driver.background_app(3)

        result = mysql_test.query(action='on_click_navbar_search', page_name='search_home', event_time=begin_date)
        assert len(result) == 1, f'埋点数量错误，预期为1个，实际为{len(result)}'
        end_date_home_open = result[0]['event_time']
        print("target埋点: %s" % end_date_home_open)


if __name__ == '__main__':
    unittest.main()
