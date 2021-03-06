from common import *


class Meigou_welfare_home_click_section(unittest.TestCase):
    log = Log()

    def test_welfare_home_click_section(self):
        """
        点击美购首页聚合icon
        """

        begin_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(begin_date)

        with GMdriver() as driver:
            driver.click_alert()
            driver.click_welfare_home()
            time.sleep(1)
            driver.click_czsl()
            time.sleep(1)
            driver.background_app(5)

        # 美购品类聚合 埋点
        result_welfare_home_click_section = mysql_test.query(action='welfare_home_click_section', event_time=begin_date)
        assert len(result_welfare_home_click_section) == 1, f'埋点数量错误，预期为1个，实际为{len(result_welfare_home_click_section)}'
        end_welfare_home_click_section_create_time = result_welfare_home_click_section[0]['event_time']
        print("target埋点: %s" % end_welfare_home_click_section_create_time)



if __name__ == '__main__':
    unittest.main()
