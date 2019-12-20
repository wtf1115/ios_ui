from common import *


class Meigou_hospital_do_search(unittest.TestCase):
    log = Log()

    def test_do_search(self):
        """
        美购聚合页医院热搜词
        """
        begin_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(begin_date)

        with GMdriver() as driver:
            driver.click_alert()
            driver.click_welfare_home()
            time.sleep(1)
            driver.click_czsl()
            time.sleep(1)
            driver.click_search()
            driver.click_hospital()
            driver.click_hot_search()
            time.sleep(1)
            driver.background_app(5)

        # 搜索框 埋点
        result_do_search = mysql_test.query(action='do_search',page_name='search_home',event_time=begin_date)
        assert len(result_do_search) == 1, f'埋点数量错误，预期为1个，实际为{len(result_do_search)}'
        print(result_do_search)
        do_search_create_time = result_do_search[0]['event_time']
        print("target埋点: %s" % do_search_create_time)
        raw_data = json.loads(result_do_search[0]['raw_data'])['params']
        assert raw_data['tab'] == '医院'


if __name__ == '__main__':
    unittest.main()
