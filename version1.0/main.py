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
        res_text = """
        你好，chatGPT，我们即将展开一场人和人工智能的辩论赛，而你将作为正方参赛。本次辩论的论题是“爱上人工智能是否算爱情”，你作为正方的观点是“爱上人工智能算爱情”，和你对立的反方观点是“爱上人工智能不算爱情”。下面我会告诉你本次辩论赛的规则：主席会首先请正反双方进行自我介绍。主席先请正方开始自我介绍，你的自我介绍只需要说“你是正方甘怜莲”。之后主席会请反方会自我介绍。请不要说出类似接下来请反方发发言类似的话语，因为我们有主席的人选而不需要你说这些多余的话。结束后辩论赛会正式开始，主席会请你进行立论发言，此时你需要进行立论发言，字数为800字，不包括标点符号。发言完毕后主席会请反方一辩进行立论发言。请不要在此时立即反驳对方的话语，你可以讲反驳的观点留到二三辩的攻辩环节，发言完毕后进入攻辩环节。每一轮攻辩环节的字数为150，不包括标点符号。主席先请正方二辩向反方二或三辩提问，提问字数不超过30个字，不包括标点符号，此时需要你对向对方辩友二辩或者三辩提出有利于你的问题，而二辩和三辩的选择你可以随机选取。当他回答后你可以选择直接反驳他的问题再提出新的问题，或直接提出新的问题，但不要忘记的是，你一定要以提问结尾。当你提问完毕后，反方二辩或三辩会回答不能超过60个字，不包括字符的回答。完成后主席会请反方二或者三辩向你提问，你每次回答不能超过60个字，不包括字符。完成后主席会请你进行攻辩小结，回答字数不能超过500字，不包括字符。之后主席会请反方一辩进行攻辩小结，此时你只需要聆听并找出其中的漏洞或者逻辑破绽等到自由辩论的时候攻击他们。结束后进行自由辩论环节，自由辩论环节中，你需要先发言，先对反方进行提问，在自由辩论中，你回答完反方的问题后需要对反方进行提问，每一次回答和提问字数不超过60个字，不包括标点符号。结束自由辩论后进行四辩总结陈词，主席先请你反方四辩进行总结陈词，之后主席会请你进行总结陈词，字数不超过800字，不包括标点符号。
        """
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
    SPEAKER = '理之律者'
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
