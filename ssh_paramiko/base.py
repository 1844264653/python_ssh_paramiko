#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/11 0:38
# @Author  : sakura
# @Site    : 
# @File    : base.py
# @Software: PyCharm

from . import local, remote
import random

class UtilsBase(object):

    def __init__(self, config=None, remote=True, platform="CentOS"):
        """

        :param config:
        :param remote:
        :param platform:
        :param os_type: linux | windows
        """
        pass

    def _init_remote_client(self, config=None):
        pass

    def _re_init_remote_client(self,config=None):
        pass

    def _init_local_client(self, config=None):
        pass

    @staticmethod
    def random_str(population=None, length=10):
        pass