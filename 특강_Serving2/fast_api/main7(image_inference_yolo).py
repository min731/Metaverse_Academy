from fastapi import FastAPI,Form,File,UploadFile
from PIL import Image
import io
import numpy as np

from transformers import YolosFeatureExtractor, YolosForObjectDetection

feature_extractor = YolosFeatureExtractor.from_pretrained('hustvl/yolos-small')
model = YolosForObjectDetection.from_pretrained('hustvl/yolos-small')


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
@app.post("/uploadfile2/")
async def create_upload_file(file: UploadFile):
    print("file.name : ",file.filename)
    print("file.name : ",file.content_type)

    # 스트리밍으로 파일 읽기
    contents = await file.read()
    
    # 자주 뜨는 오류: 'utf-8' codec can't decode byte 0x89 in position 0: invalid start byte
    # img = Image.open(contents)

    # bytes를 이미지로 변환하기
    img = Image.open(io.BytesIO(contents))
    print(img.size)
    img = np.array(img)
    print(img.shape)


    inputs = feature_extractor(images=img, return_tensors="pt")
    outputs = model(**inputs)

    logits = outputs.logits
    bboxes = outputs.pred_boxes
    print(logits.shape)
    print(bboxes.shape)

    # return {"logits":logits[0].detach().numpy(),"bboxes":bboxes[0].detach().numpy()}
    return {"bboxes":bboxes[0][0].detach().numpy()}
    # return None