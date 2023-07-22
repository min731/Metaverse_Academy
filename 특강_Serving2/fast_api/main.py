from typing import Union
from fastapi import FastAPI

app = FastAPI()

# get,post만 사용
# 딥러닝은 post만 사용
# uvicorn main:app --reload 실행(main이라는 파일안의 app을 실행한다, --reload: 자동으로 업데이트한다.)
# http://127.0.0.1:8000 주소에서 확인

@app.get('/')
def read_root():
    return {"Hello":"World"}

# http://127.0.0.1:8000/items/2

# query로 넣을 수도 있음
@app.get("/items/{item_id}") # q라는 값에 어떠한 것이든 입력될 수 있음
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


# http://127.0.0.1:8000/items/5?q=somequery url로 입력가능  
# http://127.0.0.1:8000/docs swagger에서 테스트 가능
# Pydantic을 통해 통신할 때 데이터 타입을 구조화해줌, request<->response 

