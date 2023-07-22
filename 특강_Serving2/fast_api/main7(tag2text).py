from fastapi import FastAPI,Form,File,UploadFile
from typing import Optional
from PIL import Image
import io

# https://github.com/xinyu1205/recognize-anything
# Code - download zip
# 경로에 ram이라고 저장
# requirements 버전 수정
# inference_tag2text.py 코드 다 가져와서 튜닝

import numpy as np
import torch

# ram 상위폴더를 따로 만듬
from PIL import Image
from ram.ram.models import tag2text
from ram.ram import inference_tag2text as inference
from ram.ram import get_transform

# argument 변수를 변수명으로, 값은 default 값으로
pretrained = '../models/tag2text_swin_14m.pth'
img_size = 384
thre = 0.68
delete_tag_index = [127,2961, 3351, 3265, 3338, 3355, 3359]
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')


model = tag2text(pretrained=pretrained,
                        image_size=img_size,
                        vit='swin_b',
                        delete_tag_index=delete_tag_index)
model.threshold = thre
model.eval()
model = model.to(device)

app = FastAPI()

# https://fastapi.tiangolo.com/ko/tutorial/request-files/
# byte or uploadFile

# bytes는 길이만 알 수 있음
@app.post("/files/")
async def create_file(file: bytes = File()):
    return {"file_size": len(file)}

# UploadFile : 비동기 처리 가능, 파일 이름/포맷을 알 수 있음
# ~파일을 보낼지 먼저 알려주고 파일을 보냄
@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    # jpg,png인지 식별해서 몇채널인지 구분
    print("file.name : ",file.filename)
    print("file.name : ",file.content_type)
    return {"filename": file.filename}

# 비동기로 읽음
@app.post("/uploadfile2/")                              # Form(...) 입력해도 되고 안해도됌
async def create_upload_file(file: UploadFile, 
                             tags: Optional[str] = Form(default='None')):
    
    print("file.name : ",file.filename)
    print("file.name : ",file.content_type)

    # 스트리밍으로 파일 읽기
    contents = await file.read()

    # argument 변수를 변수명으로, 값은 default 값으로
    specified_tags = tags
    transform = get_transform(image_size=img_size)
    image = transform(Image.open(io.BytesIO(contents))).unsqueeze(0).to(device)

    res = inference(image, model,specified_tags)
    print("Model Identified Tags: ", res[0])
    print("User Specified Tags: ", res[1])
    print("Image Caption: ", res[2])

    return {"Model Identified Tags: ", res[0],"User Specified Tags: ", res[1],"Image Caption: ", res[2]}
