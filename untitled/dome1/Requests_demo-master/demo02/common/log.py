#coding:utf-8
import logging
from datetime import datetime
import threading
from demo02 import readConfig
import os

class Log:
    def __init__(self):
        global logPath,resultPath,proDir
        proDir = readConfig.proDir
        resultPath = os.path.join(proDir,"result")
        #结果文件处理
        if not os.path.exists(resultPath):
            os.mkdir(resultPath)
        #定义结果返回文件名称和地址
        logPath = os.path.join(resultPath,str(datetime.now().strftime("%Y-%m-%d-%H-%M-%S")))
        if not os.path.exists(logPath):
            os.mkdir(logPath)

        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        #日志头部
        handler = logging.FileHandler(os.path.join(logPath,"output.log"))
        #日志日期参数
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        handler.setFormatter(formatter)

        self.logger.addHandler(handler)


class Mylog:
    log = None
    mutex = threading.Lock()

    def __init__(self):
        pass

    @staticmethod
    def get_log():
        if Mylog.log is None:
            Mylog.mutex.acquire()
            Mylog.log = Log()
            Mylog.mutex.release()
        return Mylog.log


if __name__ == "__main__":
    Mylog()