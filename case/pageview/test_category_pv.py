from common import *


class Category_pv(unittest.TestCase):
    log = Log()

    # 不必重构setup，Testtodolist中对driver已经获取！

    def test_category_pv(self):
        """
        品类聚合页pv
        """
        # self._testMethodDoc
        begin_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(begin_date)
        with GMdriver() as driver:
            driver.click_alert()
            driver.click_bns()
            time.sleep(1)
            driver.background_app(3)

        result = mysql_test.query(action='page_view', page_name='category', event_time=begin_date)
        print(result)
        assert len(result) == 1, f'埋点数量错误，预期为1个，实际为{len(result)}'
        end_raw_data = result[0]['raw_data']
        raw_data = json.loads(end_raw_data)
        referrer = raw_data['params']['referrer']
        assert referrer == 'home', 'referrer获取错误！'


if __name__ == '__main__':
    unittest.main()
