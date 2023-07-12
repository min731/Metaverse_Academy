import speech_recognition as sr
from gtts import gTTS
import playsound
import time
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import random
import os
import sys
import urllib.request
import numpy as np


#tts = gTTS(text = '인공지능반 지니입니다.')
#tts.save('test.mp3')
#time.sleep(2)
#playsound.playsound('test.mp3')
df1 = pd.read_csv('embeding.csv',header=None)
df = pd.read_csv('ChatbotData.csv')

#한국어 모델 불러오기
model = SentenceTransformer('sentence-transformers/xlm-r-100langs-bert-base-nli-stsb-mean-tokens')


#챗봇 함수 입력받은 텍스트와 embeding 유사도 체크후 원본 챗봇에 cos컬럼 만든후 상위 정렬
def chatbot_text(text):
    em_result = model.encode(text)
    co_result = []
    for temp in range(len(df1)):
        data = df1.iloc[temp]
        co_result.append( cosine_similarity([em_result],[data])[0][0] )
    df['cos'] = co_result
    df_result = df.sort_values('cos',ascending=False)
    r = random.randint(0,5)
    return df_result.iloc[r]

def naver():
    client_id = "YOUR_CLIENT_ID"
    client_secret = "YOUR_CLIENT_SECRET"

    encText = urllib.parse.quote("반갑습니다 네이버")
    data = "speaker=mijin&speed=0&text=" + encText

    url = "https://openapi.naver.com/v1/voice/tts.bin"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request, data=data.encode('utf-8'))
    rescode = response.getcode()

    if (rescode == 200):
        print("TTS mp3 저장")
        response_body = response.read()
        with open('1111.mp3', 'wb') as f:
            f.write(response_body)
    else:
        print("Error Code:" + rescode)

try:
    while True:
        r = sr.Recognizer()

        with sr.Microphone() as source:
            print('음성을 입력하세요')
            audio = r.listen(source)
            try:
                result = r.recognize_google(audio, language='ko')

                #result = r.recognize_whisper(audio_data=audio, model="medium", language="ko")
                print('음성 : ' + result)
                chat_result = chatbot_text(result)

                print('응답 : ',chat_result['A'])

                tts = gTTS(text = chat_result['A'])
                tts.save('test.mp3')
                time.sleep(3)
                playsound.playsound(tts)
            except sr.UnknownValueError:
                print('다시 입력해주세요')
            except:
                print('알수없는 오류')

except :
    pass