#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/11 0:11
# @Author  : sakura
# @Site    : 
# @File    : remote.py
# @Software: PyCharm

import time
import socket

import paramiko
from paramiko.ssh_exception import NoValidConnectionsError

import logging

LOG = logging.getLogger(__name__)


class Client(object):
    def __init__(self, host=None, ssh_username=None, ssh_password=None,
                 ssh_port=22, connection_timeout=10, interval=5):
        self.ssh_client = None
        self.sftp_client = None
        self._init_ssh_client(host=host, ssh_username=ssh_username,
                              ssh_password=ssh_password,
                              ssh_port=ssh_port,
                              connection_timeout=connection_timeout,
                              interval=interval)
        self._init_sftp_client(host=host, ssh_username=ssh_username,
                               ssh_password=ssh_password,
                               ssh_port=ssh_port,
                               connection_timeout=connection_timeout,
                               interval=interval)

    def _close(self):
        self.ssh_client.close()
        self.sftp_client.close()

    def _init_ssh_client(self, host=None, ssh_username=None, ssh_password=None,
                         ssh_port=22, connection_timeout=300, interval=5):
        count = connection_timeout / interval
        for i in range(count):
            try:
                client = paramiko.SSHClient()  # 初始化一个客户端用于访问
                client.set_missing_host_key_policy(paramiko.AutoAddPolicy)  # 指定当对方主机没有本机公钥的情况时应该怎么办，
                # AutoAddPolicy表示自动在对方主机保存下本机的秘钥
                client.connect(hostname=host, port=ssh_port, username=ssh_username,
                               password=ssh_password, timeout=interval)
                self.ssh_client = client
                return
            except NoValidConnectionsError as e:
                print("NoValidConnectionsError : %s" % e)
            except socket.error as e:
                print("socket error : %s" % e)

            print("connect error, to retry for %s times(interval:%s)" % (i + 1, 1))

            time.sleep(1)
            continue
        raise e

    def _init_sftp_client(self, host=None, ssh_username=None, ssh_password=None,
                          ssh_port=22, connection_timeout=300, interval=5):

        count = connection_timeout / interval
        for i in range(count):
            try:
                client = paramiko.Transport()  # 初始化一个客户端用于访问
                # client.set_missing_host_key_policy(paramiko.AutoAddPolicy)  # 指定当对方主机没有本机公钥的情况时应该怎么办，
                # AutoAddPolicy表示自动在对方主机保存下本机的秘钥
                client.connect(username=ssh_username,
                               password=ssh_password)
                self.sftp_client = paramiko.SFTPClient.from_transport(client)
                return
            except NoValidConnectionsError as e:
                print("NoValidConnectionsError : %s" % e)
            except socket.error as e:
                print("socket error : %s" % e)

            print("connect error, to retry for %s times(interval:%s)" % (i + 1, 1))

            time.sleep(1)
            continue
        raise e

    def exec_command(self, command):
        stdin, stdout, stderr = self.ssh_client.exec_command(command)
        return stdin, stdout, stderr

    def upload_file(self, local_path, remote_path):
        # 上传本地文件到规程SFTP服务端
        self.sftp_client.put(local_path, remote_path)
