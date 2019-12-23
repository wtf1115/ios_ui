import os
import time
import json
import redis

redis_gm = redis.Redis(host='localhost')


def mitm_query(**kwargs):
    if kwargs:
        action = kwargs.get('action')
        page_name = kwargs.get('page_name')
        from .dbMysql import dev_id
        kwargs['device_id'] = dev_id
        if not any((action, page_name)):
            raise Exception('action,page_name必须传至少一个！')
    result = redis_gm.lrange('maidian', 0, -1)

    def inner_filter(data):
        #设备必须过滤
        data = filter(lambda x: json.loads(x).get('device', {}).get('device_id') == dev_id, data)
        if page_name:
            data = filter(lambda x: json.loads(x).get('params', {}).get('page_name') == page_name, data)

        if action:
            data = filter(lambda x: json.loads(x).get('type') == action, data)
        return data

    filter_result = list(inner_filter(result))
    # 删掉 maidian
    redis_gm.delete('maidian')
    return filter_result
# BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# port = '8899'
# try:
#
#     os.popen('brew install redis')
#     os.popen('brew services start redis')
#     os.popen('pip3 install mitmproxy')
# except:
#     pass
#
#
# def openmitm():
#     os.popen(f'mitmdump -s {os.path.join(BASE_DIR, "common", "getNewAPI.py")} --listen-port={port}')
#
#
# def closemitm():
#     time.sleep(5)
#     os.system("for i in ` lsof -i:8899|awk '{print $2}'`; do kill -9  $i; done;")
#
#
# if __name__ == '__main__':
#     openmitm()
#
#     closemitm()
