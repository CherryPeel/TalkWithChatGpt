#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @PROJECTNAME :duihuajiqiren 
# @FileName    :server.py
# @Time        :2023/4/11 15:16
# @Author      :CherryPeel
# @Email       :CherryPeel@mewpaz.com
# @Description :A new project.
import socket
import threading
from openai import cg_answer
from myazure import azure_tts as tts


def server(host_, port_):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 绑定端口
    s.bind((host_, port_))
    # 最大连接数
    s.listen(5)

    c, addr = s.accept()
    print('连接地址：', addr)

    send_msg = input("请输入要发送的消息：")
    tts(send_msg)
    c.send(send_msg.encode('utf-8'))

    conversationId = ''
    parentMessageId = ''

    while True:
        # send_msg = input("请输入要发送的消息：")
        # c.send(send_msg.encode('utf-8'))

        recv_msg = c.recv(1024).decode('utf-8')

        print("思考中...")
        cg_say = cg_answer(recv_msg, conversationId, parentMessageId)
        cg_content = cg_say[0]
        conversationId = cg_say[1]
        parentMessageId = cg_say[2]

        c.send(cg_content.encode('utf-8'))
        tts(cg_content)

        print("接收到的消息：{}\n发送的消息：{}".format(recv_msg, cg_content))
        print("*" * 50)

        # c.close()


if __name__ == '__main__':
    # host = socket.gethostname()
    host = '0.0.0.0'
    print("host:", host)
    port = 8080

    server(host, port)
