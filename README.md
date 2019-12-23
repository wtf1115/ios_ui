
如果想使用本地校验，请安装redis
brew install redis
brew services start redis
pip3 install redis
pip3 install mitmproxy
#并执行common下的getNewAPI.py
mitmdump -s common/getNewAPI.py --listen-port=8899
#设置客户端代理 端口号8899，记得链接mitm.it安装证书支持ssl


