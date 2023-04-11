#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @PROJECTNAME :talkwithchatgpt
# @FileName    :paddle_v2t.py
# @Time        :2023/3/11 21:35
# @Author      :CherryPeel
# @Email       :CherryPeel@mewpaz.com
# @Description :A new project.
from paddlespeech.cli.asr.infer import ASRExecutor


def v2t(file_path_):
    audio = file_path_
    asr = ASRExecutor()
    result = asr(audio_file=audio, model='conformer_online_wenetspeech')
    # print(result)
    return result
