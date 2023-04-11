#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @PROJECTNAME :duihuajiqiren 
# @FileName    :test2.py.py
# @Time        :2023/4/2 14:57
# @Author      :CherryPeel
# @Email       :CherryPeel@mewpaz.com
# @Description :A new project.
import requests
from azure_sts import sts, recognize_from_microphone, recognize_from_wave_file

while True:
    res_ = recognize_from_microphone()
    print(res_)
    if "打开电灯" in res_:
        url = 'http://192.168.31.169/LED=ON'
        res = requests.get(url)
        print(res.status_code)
    elif "关闭电灯" in res_:
        url = 'http://192.168.31.169/LED=OFF'
        res = requests.get(url)
        print(res.status_code)
    elif "打开风扇" in res_:
        url = 'http://192.168.31.169/FAN=ON'
        res = requests.get(url)
        print(res.status_code)
    elif "关闭风扇" in res_:
        url = 'http://192.168.31.169/FAN=OFF'
        res = requests.get(url)
        print(res.status_code)
