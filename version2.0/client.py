#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @PROJECTNAME :duihuajiqiren
# @FileName    :client.py
# @Time        :2023/4/11 15:20
# @Author      :CherryPeel
# @Email       :CherryPeel@mewpaz.com
# @Description :A new project.
import socket
from openai import cg_answer
from myazure import azure_tts


def client(host_, port_):
    c = socket.socket()
    c.connect((host_, port_))
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
        azure_tts(cg_content)
        print("接收到的消息：{} \n发送的消息：{}".format(recv_msg, cg_content))
        print("*" * 50)
        # send_msg = cg_content
        # c.close()


if __name__ == '__main__':
    host = socket.gethostname()
    host = '172.30.52.11'
    port = 8080
    print("客户端已启动")
    client(host, port)
