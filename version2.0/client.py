#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @PROJECTNAME :duihuajiqiren 
# @FileName    :client.py
# @Time        :2023/4/11 15:20
# @Author      :CherryPeel
# @Email       :CherryPeel@mewpaz.com
# @Description :A new project.
import socket


def client(host_, port_):
    while True:
        s = socket.socket()

        s.connect((host_, port_))

        recv_msg = s.recv(1024).decode('utf-8')
        print("接收到的消息：", recv_msg)

        send_msg = input("请输入要发送的消息：")
        s.send(send_msg.encode('utf-8'))
        # s.close()


if __name__ == '__main__':
    host = socket.gethostname()
    print("host:", host)
    port = 8080
    client(host, port)
