#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @PROJECTNAME :talkwithchatgpt
# @FileName    :azure_sts.py
# @Time        :2023/3/11 16:10
# @Author      :CherryPeel
# @Email       :CherryPeel@mewpaz.com
# @Description :A new project.
import os
import sys

import azure.cognitiveservices.speech as speechsdk
from savelogging import SaveLogger as sl


def sts(content_='你怎么这么不讲道理？'):
    try:
        speech_config = speechsdk.SpeechConfig(subscription=os.environ.get('SPEECH_KEY'),
                                               region=os.environ.get('SPEECH_REGION'))
        speech_config.set_property(property_id=speechsdk.PropertyId.SpeechServiceResponse_RequestSentenceBoundary,
                                   value='true')

        audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
        speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
        # speech_synthesis_voice_name = 'zh-CN-XiaochenNeural'

        ssml = """
        <speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis"
               xmlns:mstts="https://www.w3.org/2001/mstts" xml:lang="zh-CN">
            <voice name="zh-CN-XiaoxiaoNeural">
                <mstts:express-as style="affectionate" styledegree="2" role="Girl">
                    {}
                </mstts:express-as>
            </voice>
        </speak>
        """.format(content_)

        speech_synthesis_result = speech_synthesizer.speak_ssml_async(ssml).get()

        if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
            print(">> 合成完毕")
        elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = speech_synthesis_result.cancellation_details
            print("Speech synthesis canceled: {}".format(cancellation_details.reason))
            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                if cancellation_details.error_details:
                    print("Error details: {}".format(cancellation_details.error_details))
                    print("Did you set the speech resource key and region values?")
    except Exception as e:
        logger = sl(logger_name=sys._getframe(0).f_code.co_name).save_log()
        logger.error(__file__ + str(sys._getframe(0).f_lineno) + ' ' + str(e))


def recognize_from_microphone():
    try:
        speech_config = speechsdk.SpeechConfig(subscription=os.environ.get('SPEECH_KEY'),
                                               region=os.environ.get('SPEECH_REGION'))
        speech_config.speech_recognition_language = "zh-CN"
        audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
        speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)
        # print("Speak into your microphone.")
        speech_recognition_result = speech_recognizer.recognize_once_async().get()
        if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
            # print("Recognized: {}".format(speech_recognition_result.text))
            return speech_recognition_result.text
        elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
            # print(">> 太安静了: {}".format(speech_recognition_result.no_match_details))
            print(">> 那么久不理我，我先去睡觉了...")
        elif speech_recognition_result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = speech_recognition_result.cancellation_details
            print("Speech Recognition canceled: {}".format(cancellation_details.reason))
            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                print("Error details: {}".format(cancellation_details.error_details))
                print("Did you set the speech resource key and region values?")
        return ""
    except Exception as e:
        logger = sl(logger_name=sys._getframe(0).f_code.co_name).save_log()
        logger.error(__file__ + str(sys._getframe(0).f_lineno) + ' ' + str(e))


def recognize_from_wave_file(path_):
    try:
        # This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
        speech_config = speechsdk.SpeechConfig(subscription=os.environ.get('SPEECH_KEY'),
                                               region=os.environ.get('SPEECH_REGION'))
        speech_config.speech_recognition_language = "zh-CN"
        audio_config = speechsdk.audio.AudioConfig(filename=path_)
        speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)
        speech_recognition_result = speech_recognizer.recognize_once_async().get()
        if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
            # print("Recognized: {}".format(speech_recognition_result.text))
            return speech_recognition_result.text
        elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
            print("No speech could be recognized: {}".format(speech_recognition_result.no_match_details))
        elif speech_recognition_result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = speech_recognition_result.cancellation_details
            print("Speech Recognition canceled: {}".format(cancellation_details.reason))
            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                print("Error details: {}".format(cancellation_details.error_details))
                print("Did you set the speech resource key and region values?")
    except Exception as e:
        logger = sl(logger_name=sys._getframe(0).f_code.co_name).save_log()
        logger.error(__file__ + str(sys._getframe(0).f_lineno) + ' ' + str(e))


if __name__ == '__main__':
#     print(os.environ.get('SPEECH_KEY'))
    pass
