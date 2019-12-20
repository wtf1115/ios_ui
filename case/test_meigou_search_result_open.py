from common import *


class Meigou_search_result_open(unittest.TestCase):
    log = Log()

    def test_search_result_open(self):
        """
        点击美购聚合页搜索
        """
        begin_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(begin_date)

        with GMdriver() as driver:
            driver.click_alert()
            driver.click_welfare_home()
            time.sleep(1)
            driver.click_czsl()
            driver.click_search()
            time.sleep(1)
            driver.click_diary()
            driver.click_hot_search()
            driver.background_app(5)

        # 搜索框 埋点
        result_search_result_open = mysql_test.query(action='search_result_open', event_time=begin_date)
        assert len(result_search_result_open) == 1, f'埋点数量错误，预期为1个，实际为{len(result_search_result_open)}'
        search_result_open_create_time = result_search_result_open[0]['event_time']
        print("target埋点: %s" % search_result_open_create_time)


if __name__ == '__main__':
    unittest.main()
