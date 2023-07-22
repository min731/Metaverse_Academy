# uvicorn main4:app --reload

from typing import Union

# https://fastapi.tiangolo.com/ko/tutorial/request-forms/
# html의 form 형태로 받을 수 있음
# pip install python-multipart
# pip install xformers

from fastapi import FastAPI,Form
from pydantic import BaseModel

from transformers import pipeline


# 1) 모델 로드
# https://huggingface.co/eenzeenee/t5-base-korean-summarization
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# 2) 서버 생성
app = FastAPI()

# 3) 응답 받기
@app.post("/predict")
def read_root(text: str):
    result = summarizer(text)
    print(f"{result}")
    return result