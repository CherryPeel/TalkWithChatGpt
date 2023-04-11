#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   openai.py
@Time    :   2023/03/05 16:18:33
@Author  :   CherryPeel 
@Version :   1.0
@Email   :   CherryPeel@mewpaz.com
@Website :   https://blog.mewpaz.com
@Desc    :   None
'''

import requests
import json
import sys
from savelogging import SaveLogger as sl


def cg_answer(text_, conversationId_='', parentMessageId_=''):
    """
    调用api获取回复
    """
    api_url = ''
    # print(text_)
    headers = {
        "Content-Type": "application/json",
    }
    try:
        if conversationId_:
            data = {
                "message": text_,
                "conversationId": conversationId_,
                "parentMessageId": parentMessageId_,
            }
        else:
            data = {
                "message": text_,
            }

        api_res = requests.post(api_url, data=json.dumps(data), headers=headers).json()

        # print(api_res)
        response = api_res['response']
        conversationId = api_res['conversationId']
        parentMessageId = api_res['messageId']
    except Exception as e:
        logger = sl(logger_name=sys._getframe(0).f_code.co_name).save_log()
        logger.error(__file__ + str(sys._getframe(0).f_lineno) + ' ' + str(e))
        response = '我不知道你在说什么'
        conversationId = ''
        parentMessageId = ''
    return response, conversationId, parentMessageId


if __name__ == "__main__":
    conid = ''
    parid = ''
    while True:
        print('>>>', conid, parid)
        text = input("请输入：\n")
        if text == 'exit':
            break
        res = cg_answer(text, conid, parid)
        print(res[0])
        conid = res[1]
        parid = res[2]
