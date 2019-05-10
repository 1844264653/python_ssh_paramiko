#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/10 23:52
# @Author  : sakura
# @Site    : 
# @File    : local.py
# @Software: PyCharm

import subprocess


class Client(object):

    def __init__(self, config):
        pass

    def _close(self):
        raise NotImplementedError(
            "the _close is not useful when it is executed in the local"
        )

    def exec_command(self, command):
        status, output = subprocess.getstatusoutput(command)
        stdin = None
        stderr = None
        return stdin, output, stderr

    def upload_file(self, local_path, remote_path):
        raise NotImplementedError(
            "the upload_file is not useful when it is executed in the pool"
        )
