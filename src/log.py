# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:admin
# datetime:2022/8/9 15:39
# software: PyCharm
import time
import logging
import os
import sys


class Log:
    def __init__(self,):
        # logging.basicConfig()
        # 文件的命名
        log_path = os.path.join((os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'log/')
        filename = '%s.log' % time.strftime('%Y-%m-%d-%H-%M-%S')
        # filename = '%s.log' % time.strftime('%Y_%m_%d')
        self.logname = os.path.join(log_path, filename)
        self.loger = logging.getLogger('Ybei')
        self.loger.propagate = 0
        # 此处配置日志级别
        # gd = gcd.GetData()
        # self.loglevel = gd.get_level()
        self.loglevel = 'INFO'
        if self.loglevel == 'INFO':
            self.loger.setLevel(logging.INFO)
        elif self.loglevel == 'WARNING':
            self.loger.setLevel(logging.WARNING)
        elif self.loglevel == 'DEBUG':
            self.loger.setLevel(logging.DEBUG)
        elif self.loglevel == 'ERROR':
            self.loger.setLevel(logging.ERROR)

        # 日志输出格式
        self.formatter = logging.Formatter('[%(asctime)s]%(filename)s +++ [line:%(lineno)d]%(message)s')

    def __console(self, level, message):
        # 创建一个FileHandler，用于写到本地
        fh = logging.FileHandler(self.logname, 'a', encoding="utf-8")  # 追加模式
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)

        # 创建一个StreamHandler,用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)

        self.loger.removeHandler(ch)
        self.loger.removeHandler(fh)

        # print(self.loger.handlers)
        if not self.loger.handlers:
            # print(' 创建一个FileHandler，用于写到本地')
            self.loger.addHandler(fh)
            # print(' 创建一个StreamHandler,用于输出到控制台')
            self.loger.addHandler(ch)
        # print(self.loger.handlers)

        if level == 'info':
            self.loger.info(message)
            # pass

        elif level == 'debug':
            # pass
            self.loger.debug(message)
        elif level == 'warning':
            self.loger.warning(message)
            # pass

        elif level == 'error':
            self.loger.error(message)
            # pass
        # 这两行代码是为了避免日志输出重复问题

        self.loger.removeHandler(ch)
        self.loger.removeHandler(fh)
        # 关闭打开的文件
        fh.close()
        ch.close()

    def debug(self, message):
        # print("调用这个函数的函数名",sys_getframe(1).f_code.co_bame)
        # print("调用这个函数的文件名",sys_getframe(1).f_code.co_filename)
        # print("调用这个函数的语句所在的行数",sys._getframe(1).f_lineno)

        fuc_name = sys._getframe(1).f_code.co_name
        file_name = sys._getframe(1).f_code.co_filename
        line_nu = str(sys._getframe(1).f_lineno)
        if len(file_name.split("/")) >= 4 and len(file_name) > 47:
            file_name = file_name[47:]
        message = file_name + "-" + fuc_name + "[lien:" + line_nu + "]-" + message

        self.__console('debug', message)

    def info(self, message):
        fuc_name = sys._getframe(1).f_code.co_name
        file_name = sys._getframe(1).f_code.co_filename
        line_nu = str(sys._getframe(1).f_lineno)
        if (len(file_name.split("/")) >= 4 or len(file_name.split("\\")) >= 4 )and len(file_name) > 28:
            file_name = file_name[28:]
        message = file_name + "-" + fuc_name + "[lien:" + line_nu + "]-" + message
        # print(message)
        self.__console('info', message)

    def warning(self, message):
        fuc_name = sys._getframe(1).f_code.co_name
        file_name = sys._getframe(1).f_code.co_filename
        line_nu = str(sys._getframe(1).f_lineno)
        if (len(file_name.split("/")) >= 4 or len(file_name.split("\\")) >= 4) and len(file_name) > 28:
            file_name = file_name[28:]
        message = file_name + "-" + fuc_name + "[lien:" + line_nu + "]-" + message
        self.__console('warning', message)

    def error(self, message):
        fuc_name = sys._getframe(1).f_code.co_name
        file_name = sys._getframe(1).f_code.co_filename
        line_nu = str(sys._getframe(1).f_lineno)
        if (len(file_name.split("/")) >= 4 or len(file_name.split("\\")) >= 4) and len(file_name) > 28:
            file_name = file_name[28:]
        message = file_name + "-" + fuc_name + "[lien:" + line_nu + "]-" + message
        self.__console('error', message)
loger = Log()
# print(loger)

if __name__ == '__main__':
    loger = Log()
    loger.error("---测试开始----")
    # loger.info("输入密码")
    # loger.info("----测试结束----")






















