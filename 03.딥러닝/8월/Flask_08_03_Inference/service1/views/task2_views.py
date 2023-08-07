from flask import Blueprint
from flask import request

# 추론하기 위해 동일한 학습할 때와 전처리 과정이 필요함
import torch
from torchvision import transforms
from PIL import Image

bp = Blueprint('task2',__name__,url_prefix='/task2')

# 학습시킬 때 cpu or gpu에 학습시킨 모델이 있을 수 있음
# 현재 gpu에서 학습시킨 모델임
# cpu에서 추론하고 싶을 때는 map_location = torch.device('cpu')

# 만약 가중치를 불러온다면 모델 객체를 만들고 가중치를 넣으면됌
model = torch.load('model.pt',map_location = torch.device('cpu'))



# 이미지,음성 등 데이터를 받을 때 POST
# method default는 GET
# postaman 'POST'로 바꾼 후 url 입력
@bp.route('/mds_karina',methods=['POST'])
def task2_mds_karina_lkj():
    print("체크 request.form : ", request.form)

    # requerst.files로 안들어오면 안받아진 것임
    print("체크 request.files : ", request.files)
    f = request.files['image']

    # 확장자로 .png 확장자 거를 수도 있음
    print("체크 f : ",f)
    print("체크 f.filename : ", f.filename)

    # 클라이언트에서 보낸 이미지를 저장
    # 저장하지 않아도 추론할 수 있지만 DB에 기록할 수 있음
    # 데이터 수집을 통해서 재학습할 수 있음
    f.save('image.jpg')

    img = Image.open('image.jpg')
    # img = 

    transform_test = transforms.Compose(
        [
            transforms.Resize((224,224)),
            # transforms.RandomHorizontalFlip(p=0.5),
            transforms.ToTensor(),
            # R,G,B 중 한가지 색상에 가중치가 지나치게 부여되는 것을 방지
            # ex) 빨간색이면 사과로 분류하는 것 방지
            transforms.Normalize([0.485,0.456,0.406],[0.229,0.224,0.225])
        ]
    )

    # transforms로 전처리함
    img = transform_test(img)
    print(img.shape)

    # 배치 사이즈 차원 추가함
    img = img.unsqueeze(0)
    print(img.shape)

    # cpu에 세팅
    img = img.to('cpu')

    model.eval()
    class_names = ['마동석','이국주','카리나']

    with torch.no_grad():

        preds = model(img)
        print("체크 preds : ",preds)
        
        # idx,값 
        _, pred = torch.max(preds,1)
        print("체크 _ : ", _)
        print("체크 pred : ",pred)

        print(f'예측결과 : {class_names[pred[0]]}')

    return f'예측결과 : {class_names[pred[0]]}'

# 전이학습 이유
# normalize
# model.eval()