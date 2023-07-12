# 음성 챗봇 만들기
import playsound
# STT 패키지 설치
# pip install SpeechRecognition
# pip install pyaudio

# 마이크 활성화 확인
# 윈도우 - 녹음기 (녹음 되는지 확인)
# 소리 설정 - 오디오 향상 체크 해제

# pip install gTTS
# pip install playsound
# pip install pandas
# pip install sentence-trnasformers

# speech_recognition은 예외처리 필수!
import speech_recognition as sr
from gtts import gTTS
import playsound
import time

# 모델 로드
import sentence_transformers
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import random
import numpy as np

# 소숫점 6자리 까지만
np.set_printoptions(precision=6,suppress=True)
# 한국어 모델
model = SentenceTransformer('sentence-transformers/xlm-r-100langs-bert-base-nli-stsb-mean-tokens')
embedding_data = pd.read_csv('C:/Users/user/PycharmProjects/speak_chatbot/data/ChatbotData_embedding.csv',header=None)
df = pd.read_csv('C:/Users/user/PycharmProjects/speak_chatbot/data/ChatbotData.csv')
#
# text = "나 오늘 너무 힘들었어"
#
def chatbot_text(text):
  em_result = model.encode(text)
  cos_result = []
  for tmp in range(len(embedding_data)):
    data = embedding_data.iloc[tmp]
    cos_result.append(cosine_similarity([data],[em_result])[0][0])

  df['cos'] = cos_result
  df_result = df.sort_values('cos',ascending=False)
  r = random.randint(0,5)

  # print("r :",r)
  print(df_result.iloc[r]['A'])

  return df_result.iloc[r]['A']

try:
    while True:
        print("--실행 중--")
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("음성을 입력하세요.")

            # 소스가 오디오로 바뀜
            audio = r.listen(source)

            try:
                # 구글의 stt
                print("음성 받음!")
                print("음성 : "+r.recognize_google(audio,language='ko-KR'))

                tts = gTTS(text=chatbot_text(r.recognize_google(audio,language='ko-KR')))
                tts.save('test3.mp3')
                time.sleep(1)
                playsound.playsound('test3.mp3')

            except sr.UnknownValueError:
                print("다시 입력해주세요.")
            except:
                print("알수없는 오류")


except:
    print("예외!")
    pass