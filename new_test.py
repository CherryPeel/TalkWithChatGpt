#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @PROJECTNAME :talkwithchatgpt
# @FileName    :new_test.py
# @Time        :2023/3/11 21:56
# @Author      :CherryPeel
# @Email       :CherryPeel@mewpaz.com
# @Description :A new project.
import sounddevice as sd
import soundfile as sf


def record_from_microphone():
    """
    录音并保存到文件
    :return:
    """
    print(">> 录音中...")
    fs = 16000
    seconds = 5
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
    sd.wait()
    sf.write('output.wav', myrecording, fs)
    print(">> 录音结束，已保存到output.wav")
    return 'output.wav'


if __name__ == '__main__':
    record_from_microphone()
