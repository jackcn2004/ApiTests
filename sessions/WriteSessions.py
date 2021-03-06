#!/usr/bin/evn python
# -*- coding:utf-8 -*-

# FileName WriteSessions.py
# Author: HeyNiu
# Created Time: 20160728
"""
把请求session相关信息写入文件
包含
request url
request header
request body
response code
response body
"""

import os
import threading

import utils.GlobalList


class WriteSessions(threading.Thread):

    def __init__(self, threading_id, threading_name, threading_queue, session, error_path):
        threading.Thread.__init__(self)
        self.threading_id = threading_id
        self.threading_name = threading_name
        self.threading_queue = threading_queue
        self.session = session
        self.error_path = error_path
        self.path = ""

    def run(self):
        self.__write_session()

    def __write_session(self):
        """
        把请求写入文件，一个请求一个文件
        :return:
        """
        dir1 = '%s%s' % (utils.GlobalList.SESSIONS_PATH, "\\Sessions\\")
        if not os.path.exists(dir1):
            try:
                os.mkdir(dir1)
            except FileExistsError:
                print("")
        if len(self.error_path) == 0:
            self.path = '%s%s%s' % (dir1, self.session[0], ".txt")
        else:
            if not os.path.exists('%s%s' % (dir1, "Check\\")):
                os.mkdir('%s%s' % (dir1, "Check\\"))
            self.path = '%s%s%s%s' % (dir1, "Check\\", self.error_path, ".txt")
        with open(self.path, 'a', encoding='utf-8') as f:
            for i in self.session:
                f.write(i)
                f.write("\n")
            f.write("Session end")
            f.write("\n")
            f.write("\n")
