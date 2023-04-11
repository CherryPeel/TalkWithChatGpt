#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @PROJECTNAME :duihuajiqiren 
# @FileName    :myazure.py
# @Time        :2023/4/11 16:21
# @Author      :CherryPeel
# @Email       :CherryPeel@mewpaz.com
# @Description :A new project.
import os
import azure.cognitiveservices.speech as speechsdk


def azure_tts(content_='你怎么这么不讲道理？'):
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
            # print(">> 合成完毕")
            pass
        elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = speech_synthesis_result.cancellation_details
            print("Speech synthesis canceled: {}".format(cancellation_details.reason))
            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                if cancellation_details.error_details:
                    print("Error details: {}".format(cancellation_details.error_details))
                    print("Did you set the speech resource key and region values?")
    except Exception as e:
        # logger = sl(logger_name=sys._getframe(0).f_code.co_name).save_log()
        # logger.error(__file__ + str(sys._getframe(0).f_lineno) + ' ' + str(e))
        print(e)
