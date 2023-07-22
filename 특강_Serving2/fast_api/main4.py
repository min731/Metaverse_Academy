# uvicorn main4:app --reload

from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

from transformers import pipeline

# conda install pytorch torchvision torchaudio pytorch-cuda=11.7 -c pytorch -c nvidia
# pip install transformers

classifier = pipeline("sentiment-analysis", model="stevhliu/my_awesome_model")

app = FastAPI()

@app.post("/predict")
def read_root(text: str):
    result = classifier(text)
    print(f"{result}")
    return result