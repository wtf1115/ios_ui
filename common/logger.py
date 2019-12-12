import logging
import time
import os


class Logger(object):
    def __init__(self, logger):
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)
        file_name = time.strftime("%Y%m%d %H%M",time.localtime(time.time()))
        log_path = os.path.dirname(os.path.abspath('.')) + "\\logs\\"
        full_path = log_path + file_name+'.log'
        file_handler = logging.FileHandler(full_path)
        file_handler.setLevel(logging.INFO)

        # 再定义一个 （Handler定义成输出到控制台）
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

    def getlog(self):
        return self.logger