from common import *


class On_click_create_topic(unittest.TestCase):
    log = Log()

    def test_on_click_create_topic(self):
        """
        点击首页创建按钮
        """

        begin_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(begin_date)

        with GMdriver() as driver:
            driver.click_alert()
            driver.click_create_topic()
            time.sleep(2)
            driver.background_app(3)
        result = mitm_query(action='on_click_create_topic', page_name='home', event_time=begin_date)

        assert len(result) == 1, f'埋点数量错误，预期为1个，实际为{len(result)}'


if __name__ == '__main__':
    unittest.main()
