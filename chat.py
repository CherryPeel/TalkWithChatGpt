# coding:gbk
from test2 import tts,recognize_from_microphone
from openai import cg_answer
import struct
import pyaudio
import pvporcupine
import pvcobra


def picovoice():
    picovoice_access_key = 'KbgY4RKIZlu3befSN7432P56bajHAYbc0reK3KOpWN2diO3insbCYA=='
    porcupine = pvporcupine.create(
        access_key=picovoice_access_key,
        keyword_paths=['hi-chat_en_windows_v2_1_0.ppn']
    )
    pa = pyaudio.PyAudio()
    cobra = pvcobra.create(picovoice_access_key)
    audio_stream = pa.open(
        rate=porcupine.sample_rate,
        channels=1,
        format=pyaudio.paInt16,
        input=True,
        frames_per_buffer=porcupine.frame_length)
    while True:
        pcm = audio_stream.read(porcupine.frame_length, exception_on_overflow=False)
        #
        _pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)
        keyword_index = porcupine.process(_pcm)
        print("ʶ����")
        if keyword_index >= 0:
            tts("��ã���ʲô������԰�����")
            print("��⵽��˵�˻��Ѵ�")
            return True



if __name__ == '__main__':
    # cg_res_con_id = ''
    # cg_res_par_id = ''
    # r = picovoice()
    # while True:
    #     if r:
    #         if cg_res_con_id:
    #             r_text = recognize_from_microphone()
    #             cg_res = cg_answer(r_text)
    #             cg_res_text = cg_res["response"]
    #             cg_res_con_id = cg_res['conversationId']
    #             cg_res_par_id = cg_res['messageId']
    #             tts(cg_res_text)
    #         else:
    #
    #     else:
    #         cg_res_par_id = ''
    #         cg_res_con_id = ''
    #         picovoice()