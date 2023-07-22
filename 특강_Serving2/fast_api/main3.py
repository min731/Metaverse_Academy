# 추론

from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# 1) 데이터 받고
# 2) 예측해서 보내기

# 데이터 받기
# Fast-api - 자습서 - request body

## int데이터 받을 때
# get은 body가 없음
# 데이터를 받으려면 post로
# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None

# @app.post("/predict")
# def read_root(item: Item):
#     print(f"{item.name},{item.price}")
#     return item


## 텍스트데이터 받을 때
@app.post("/predict")
def read_root(item: str):
    print(f"{item}")
    return item

# conda install pytorch torchvision torchaudio pytorch-cuda=11.7 -c pytorch -c nvidia
# pip install transformers