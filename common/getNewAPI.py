from mitmproxy import http
import json

import gzip
import urllib3
import redis

redis_gm = redis.Redis(host='localhost')
urllib3.disable_warnings(Exception)


class Gmaddon:
    def __init__(self):
        '''需要再添加'''
        self.host_list = ['log.igengmei.com', 'log.test.igengmei.com']

    def request(self, flow: http.HTTPFlow):
        '''do nothing here'''
        if flow.request.host in self.host_list:
            # 放在redis里面
            d = json.loads(gzip.decompress(flow.request.data.content).decode())
            if isinstance(d, list):
                [redis_gm.lpush('maidian', json.dumps(item)) for item in d]
            elif isinstance(d, dict):
                redis_gm.lpush('maidian', json.dumps(d))


addons = [
    Gmaddon(),
    # Mladdon(),
]
