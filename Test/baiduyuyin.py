from aip import AipSpeech
import os
import time

def baidu_voice(voice):
    """ 你的 APPID AK SK """
    APP_ID = '19350850'
    API_KEY = 'KUw17i18HhbqEQ8RgbrYNFoL'
    SECRET_KEY = '1dxOFr8hu9MbATZWoTE6yobRISMYFl9r'

    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
    result  = client.synthesis(voice, 'zh', 1, {
        'vol': 8,'per':0
    })
    # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
    if not isinstance(result, dict):
        with open('./audio.mp3', 'wb') as f:
            f.write(result)
if __name__=="__main__" :
    baidu_voice("识别正确")
    os.system('rhythmbox ./audio.mp3')
