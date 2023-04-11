#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @PROJECTNAME :duihuajiqiren 
# @FileName    :test.py.py
# @Time        :2023/3/26 16:38
# @Author      :CherryPeel
# @Email       :CherryPeel@mewpaz.com
# @Description :A new project.
# import libraries

import requests
import json
from playsound import playsound
from openai import cg_answer
from azure_sts import sts, recognize_from_microphone, recognize_from_wave_file

API_KEY = "90Np7562uqGE9fEPopArTxwb"
SECRET_KEY = "g755V1db8DfT9mVDVaZn7MoY3IOfrxc9"


def test(text_):
    url = "https://aip.baidubce.com/rpc/2.0/nlp/v1/txt_monet?charset=UTF-8&access_token=" + get_access_token()

    payload = json.dumps({
        "content_list": [
            {
                "content": text_,
                # "content": "请反方二辩向正方二辩提问",
                "query_list": [
                    {
                        "query": "提问者"
                    },
                    {
                        "query": "提问对象"
                    },
                    {
                        "query": "自我介绍"
                    },
                    {
                        "query": "立论"
                    }
                ]
            }
        ]
    })
    headers = {
        'Content-Type': 'application/json',
        # 'Accept': 'application/json'
    }

    response = requests.post(url, headers=headers, data=payload).json()

    print(response["results_list"][0]["results"])
    # print(response)
    return response["results_list"][0]["results"]


def get_access_token():
    """
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    return str(requests.post(url, params=params).json().get("access_token"))


def ding():
    try:
        playsound('./static/music/ding.mp3')
    except Exception as e:
        print(e)


if __name__ == '__main__':
    conid = ''
    parid = ''

    # cg_res = cg_answer("", conid, parid)
    with open('rule.txt', 'r') as f:
        rule = f.read()
        # print(rule)
        cg_res = cg_answer(rule, conid, parid)
        # sts(cg_res[0])
        print(cg_res[0])
        conid = cg_res[1]
        parid = cg_res[2]

    while True:
        # break
        text = recognize_from_microphone()
        print(text)

        # res = test("首先请正方进行自我介绍")
        res = test(text)
        try:
            res__ = res[2]["items"][0]["text"]
            print(res__)
            if res__ == '正方':
                print(">> 正方  " + res__)
                cg_res = cg_answer("请正方一辩进行自我介绍", conid, parid)
                sts(cg_res[0])
                conid = cg_res[1]
                parid = cg_res[2]
                ding()
                continue
        except Exception as e:
            print(e)

        # res = test("首先请正方一辩进行立论和发言")
        # res = test(text)
        try:
            res__ = res[3]["items"][0]["text"]
            if res__ == '正方一辩':
                print(">> 正方一辩  " + res__)
                cg_res = cg_answer("请正方一辩进行立论和发言", conid, parid)
                sts(cg_res[0])
                conid = cg_res[1]
                parid = cg_res[2]
                ding()
                continue
        except Exception as e:
            print(e)

        # res = test(text)
        try:
            res__ = res[0]["items"][0]["text"]
            if res__ == '正方二辩':
                print(">> 正方二辩  " + res__)
                cg_res = cg_answer("请你向正方二或三辩提问（提问时请言简意赅并指定其中的一名辩手）", conid, parid)
                sts(cg_res[0])
                conid = cg_res[1]
                parid = cg_res[2]
                ding()
                continue
            # for i in res:
            #     print(i)
            #     item = i["items"][0]["text"]
            #     if item == "正方一辩":
            #         cg_res = cg_answer(
            #             "请你向正方二或三辩提问（提问时请言简意赅并指定其中的一名辩手），辩题是：人工智能对人类的爱算是爱嘛",
            #             conid, parid)
            #         sts(cg_res[0])
            #         conid = cg_res[1]
            #         parid = cg_res[2]
            #         ding()
            #         print("ok" + item)
            #         break
            #     elif item == "正方二辩":
            #         cg_res = cg_answer(
            #             "请你向反方二或三辩提问（提问时请言简意赅并指定其中的一名辩手），辩题是：人工智能对人类的爱算是爱嘛",
            #             conid, parid)
            #         sts(cg_res[0])
            #         ding()
            #         conid = cg_res[1]
            #         parid = cg_res[2]
            #         print("not ok" + item)
            #         break
        except Exception as e:
            print(e)
