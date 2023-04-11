#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @PROJECTNAME :talkwithchatgpt
# @FileName    :anime_vits.py.py
# @Time        :2023/3/14 20:28
# @Author      :CherryPeel
# @Email       :CherryPeel@mewpaz.com
# @Description :A new project.
import websocket
import json
import requests
import os
import sys
from playsound import playsound
from tqdm import tqdm
from savelogging import SaveLogger as sl


def get_wav(_text='没字我咋说话', _lang='中文', _speaker='八重神子（神子）', _speed=0.6, _pitch=0.668, _volume=1.2):
    url = 'wss://sayashi-vits-uma-genshin-honkai.hf.space/queue/join'

    # 构造伪客户端信息
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Upgrade': 'websocket',
        'Origin': 'https://sayashi-vits-uma-genshin-honkai.hf.space',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'Connection': 'Upgrade',
    }

    ws = websocket.create_connection(url)
    # ws = websockets.connect(url)
    # ws.send(json.dumps(headers))

    ws.send(json.dumps({"session_hash": "8j1nwh4e9wi", "fn_index": 0}))
    ws.send(json.dumps(
        {"fn_index": 0, "data": [_text, _lang, _speaker, _speed, _pitch, _volume], "session_hash": "8j1nwh4e9wi"}))

    while True:
        res = ws.recv()

        if not res:
            break

        # 将unicode转换为str
        res = res.encode('utf-8')
        # 转换为json

        res = json.loads(res)
        # print(res)
        try:
            if res['msg'] == 'process_completed':
                wav = "https://sayashi-vits-uma-genshin-honkai.hf.space/file=" + res['output']['data'][1]['name']

                if not os.path.exists('./static/wav'):
                    os.makedirs('./static/wav')
                # 下载音频
                r = requests.get(wav, stream=True)
                with open('./static/wav/test.wav', 'wb') as f:
                    for chunk in tqdm(r.iter_content(chunk_size=1024)):
                        if chunk:
                            f.write(chunk)

                # print(res)
                # print(wav)
                play_wav()
                return wav
        except Exception as e:
            print(_text, _speaker)
            # print(__name__, e + '-->' + _text + '-->' + _speaker)
            logger = sl(logger_name=sys._getframe(0).f_code.co_name).save_log()
            logger.error(__file__ + str(sys._getframe(0).f_lineno) + ' ' + str(e))
            # return None
            # pass


def play_wav():
    try:
        playsound('./static/wav/test.wav')
        os.remove('./static/wav/test.wav')
    except Exception as e:
        logger = sl(logger_name=sys._getframe(0).f_code.co_name).save_log()
        logger.error(__file__ + str(sys._getframe(0).f_lineno) + ' ' + str(e))

if __name__ == "__main__":
    get_wav(_speaker='理之律者')
