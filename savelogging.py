#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @PROJECTNAME :talkwithchatgpt
# @FileName    :savelogging.py
# @Time        :2023/3/14 22:03
# @Author      :CherryPeel
# @Email       :CherryPeel@mewpaz.com
# @Description :A new project.
import logging
import time
import sys


class SaveLogger():
    def __init__(self, log_path='./logs', log_file_name=time.strftime("%Y-%m-%d", time.localtime()),
                 logger_name=sys._getframe(0).f_code.co_name,
                 log_format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', log_level=logging.INFO):
        self.log_path = log_path
        self.log_file_name = log_file_name
        self.log_name = logger_name
        self.log_format = log_format
        self.log_level = log_level

    # @staticmethod
    def save_log(self, ):
        logger = logging.getLogger(self.log_name)
        logging.basicConfig(level=logging.INFO)
        file_handler = logging.FileHandler(str(self.log_path) + '/' + str(self.log_file_name) + ".log",
                                           encoding="utf-8")
        file_handler.setLevel(self.log_level)
        file_handler.setFormatter(logging.Formatter(self.log_format))
        logger.addHandler(file_handler)
        return logger


# def test():
#     logger.info("test")
#
#
# if __name__ == '__main__':
#     logger = SaveLogger().save_log()
#     logger.info("test")
#     test()
