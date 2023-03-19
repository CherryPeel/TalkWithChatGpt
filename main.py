#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @PROJECTNAME :talkwithchatgpt
# @FileName    :savelogging.py
# @Time        :2023/3/14 22:03
# @Author      :CherryPeel
# @Email       :CherryPeel@mewpaz.com
# @Description :A new project.
import time
import os
import logging
import sys
import azure.cognitiveservices.speech as speechsdk
from savelogging import SaveLogger as sl
# from paddle_v2t import v2t
from azure_sts import sts, recognize_from_microphone, recognize_from_wave_file
from openai import cg_answer
from playsound import playsound
from anime_vits import get_wav


def speech_recognize_keyword_locally_from_microphone():
    """runs keyword spotting locally, with direct access to the result audio"""

    # Creates an instance of a keyword recognition model. Update this to
    # point to the location of your keyword recognition model.
    model = speechsdk.KeywordRecognitionModel("model/GanLianLian/059aa79d-ac3d-4ea1-940f-baa209059f38.table")

    # The phrase your keyword recognition model triggers on.
    keyword = '甘怜莲'

    # Create a local keyword recognizer with the default microphone device for input.
    keyword_recognizer = speechsdk.KeywordRecognizer()

    done = False

    def recognized_cb(evt):
        result_ = evt.result
        if result_.reason == speechsdk.ResultReason.RecognizedKeyword:
            print(">> 已唤醒: {}".format(result_.text))
        nonlocal done
        done = True

    def canceled_cb(evt):
        result_ = evt.result
        if result_.reason == speechsdk.ResultReason.Canceled:
            print('CANCELED: {}'.format(result_.cancellation_details.reason))
        nonlocal done
        done = True

    # Connect callbacks to the events fired by the keyword recognizer.
    keyword_recognizer.recognized.connect(recognized_cb)
    keyword_recognizer.canceled.connect(canceled_cb)

    # Start keyword recognition.
    result_future = keyword_recognizer.recognize_once_async(model)
    print('>>  唤醒 "{}" 后，对她说点什么吧 ...'.format(keyword))
    result = result_future.get()

    # Read result audio (incl. the keyword).
    # print('Reading result audio...')
    # print(result.reason)
    if result.reason == speechsdk.ResultReason.RecognizedKeyword:
        # print('Keyword recognized')
        time.sleep(2)  # give some time so the stream is filled
        result_stream = speechsdk.AudioDataStream(result)
        result_stream.detach_input()  # stop any more data from input getting to the stream
        # result_stream.save_to_wav_file("AudioFromRecognizedKeyword.wav")
        # # res_text = v2t("AudioFromRecognizedKeyword.wav")
        # res_text = recognize_from_wave_file("AudioFromRecognizedKeyword.wav")
        # logger.info("user " + res_text)
        res_text = '你好'
        # print(">> ", res_text)
        res_cg_ = cg_answer(text_=str(res_text))
        logger.info("bot " + res_cg_[0] + "-" + res_cg_[1] + "<->" + res_cg_[2])
        # sts(res_cg_[0])
        # get_wav(_text=res_cg_[0], _speaker=SPEAKER)
        if Is_Choose_Anime:
            get_wav(_text=res_cg_[0], _speaker=SPEAKER)
        else:
            sts(res_cg_[0])
    return res_cg_[1], res_cg_[2]


def ding():
    try:
        playsound("./static/music/ding.mp3")
    except Exception as e:
        logger = sl(logger_name=sys._getframe(0).f_code.co_name).save_log()
        logger.error(__file__ + str(sys._getframe(0).f_lineno) + ' ' + str(e))


if __name__ == '__main__':
    # 二次元游戏人物角色,可能非常慢
    SPEAKER = '胡桃'
    Is_Choose_Anime = 0

    if not os.path.exists("logs"):
        os.mkdir("logs")

    logger = logging.getLogger("Bot")
    FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    TODAY = time.strftime("%Y-%m-%d", time.localtime())
    logging.basicConfig(level=logging.INFO)
    file_handler = logging.FileHandler("logs/" + str(TODAY) + ".log", encoding="utf-8")
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(logging.Formatter(FORMAT))
    logger.addHandler(file_handler)

    dis_id, par_id = speech_recognize_keyword_locally_from_microphone()

    while True:
        # path = record_from_microphone()
        # res_text = v2t(path)
        # print(">> ", "录音中...")
        ding()
        # time.sleep(3)
        record_text = recognize_from_microphone()
        if record_text:
            # print(">> ", record_text)
            logger.info("user " + record_text)
            res_cg = cg_answer(str(record_text), dis_id, par_id)
            logger.info("bot " + res_cg[0] + "-" + res_cg[1] + "<->" + res_cg[2])
            # sts(res_cg[0])
            if Is_Choose_Anime:
                get_wav(_text=res_cg[0], _speaker=SPEAKER)
            else:
                sts(res_cg[0])
            dis_id = res_cg[1]
            par_id = res_cg[2]
        else:
            dis_id, par_id = speech_recognize_keyword_locally_from_microphone()
