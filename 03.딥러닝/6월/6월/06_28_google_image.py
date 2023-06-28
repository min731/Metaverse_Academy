# 구글 이미지 검색 웹 스크래핑
# 쭉 스크롤 하다가 '결과 더보기' 버튼을 눌러야함
# 이미지 1개씩 누르며 <img> , <src> 안의 이미지의 주소가 들어가 있음
# 이미지의 주소를 알면 다운로드 받을 수 있음 => get attribute로 가져옴
# 단 확장자가 jpg, png, jpeg 인지 알아야함
# src를 가져와서 확장자를 식별해야함

# seleninum 3,4 사용 방법 차이가 큼


from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time, os, urllib
import requests, sys, json


# 드라이버 옵션 설정
chrom_options = webdriver.ChromeOptions() # ChromeOptions 객체 생성
chrom_options.add_experimental_option('detach', True) # 실행이 멈춰도 웹브라우저가 꺼지지 않게 하는 옵션
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrom_options) # webdriver 모듈의 Chrome 객체에 service와 options 값을 넣어 객체 생성)
driver.maximize_window() # 웹브라우저 전체화면


# 검색어 입력 및 검색
query = 'bus'

# 구글 이미지 페이지 주소 : 'https://www.google.com/imghp'

driver.get(f'https://www.google.com/imghp') # 구글 이미지 페이지로 이동

# 인터넷 환경이 원활하지 않을 수 있어 중간중간에 타임슬림
time.sleep(1)
search_bar = driver.find_element(By.NAME,"q") # textarea의 name속성이 q인것 찾기
search_bar.send_keys(query)
search_bar.submit()
time.sleep(1)


# 스크롤 내리기
PAUSE_TIME = 2 #대기시간 설정
last_hegiht = driver.execute_script("return document.body.scrollHeight")
new_height = 0
more_max = 1  #결과 더보기 최대 몇 번 반복할지
more_count = 0 #현재 결과 더보기 몇 번 했는지
while True :
    driver.execute_script("window.scrollBy(0,5000)")
    time.sleep(PAUSE_TIME)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height - last_hegiht > 0 :  #높이가 조금이라도 차이가 있으면 스크롤 다운 진행
        last_hegiht = new_height
        continue

    # 더 이상 스크롤바를 내릴 수 없을 때
    else:
        # 결과 더보기 횟수 비교해서 멈추기
        if more_count < more_max:
            more_count += 1
            # 결과 더보기가 활성화 되어있는지 확인
            element = driver.find_element(By.XPATH, '//*[@id="islmp"]/div/div/div/div/div[1]/div[2]/div[2]')
            attribute_value = element.get_attribute("style")
            if attribute_value == "": # style엘레멘트에 아무것도 없으면 결과 더보기가 활성화 되어있는 것
                element.click() #결과 더보기 클릭
            else: #결과 더보기 없어서 while문 종료
                break
        else:
            break


# 확보한 페이지 정보에서 이미지 요소 확보
img_elements = driver.find_elements(By.CSS_SELECTOR,".rg_i")


# 이미지 이름과 이미지 주소 확보하기
img_rst = []
image_count = 200
for idx, img in enumerate(img_elements[:image_count]):
    print(f"{query} : {idx+1}/{len(img_elements)} proceed...")
    try:
        img.click()
        time.sleep(PAUSE_TIME)

        # copy - XPATH 찾기
        img_element = driver.find_element(By.XPATH,'//*[@id="Sva75c"]/div[2]/div[2]/div[2]/div[2]/c-wiz/div/div/div/div[3]/div[1]/a/img[1]')
        # <src> : 주소
        img_src = img_element.get_attribute('src')
        # <alt> : 이미지 제목
        img_alt = img_element.get_attribute('alt')
        img_rst.append({'alt' : img_alt, 'src' : img_src})
    except:
        pass
driver.close()


# 확보한 정보 저장하기
# 이후에 중복된 요소가 있을 때 DataFrame에서 거를 수도 있음
print(img_rst)
with open('img_rst.txt', 'w') as file:
    file.write(json.dumps(img_rst))


# 파일 저장
# 폴더가 존재하지 않을 경우 폴더 생성

# 폴더명으로 클래스를 정의하면
# tensorflow, pytorch에서 폴더명으로 클래스 주입할 때 용이함
folder_path = 'bus'  #파일이름
if not os.path.exists(folder_path):
        os.makedirs(folder_path)

img_count = 0 #이미지 넘버링
for i, temp in enumerate(img_rst):
    url = temp['src']
    image_name = temp['alt']

    # 이미지 다운로드
    if url[-4:] == ".jpg" or url[-4:] == ".png":
        img_count += 1
        # 이미지 저장(try~except로 오류 회피)
        try:
            urllib.request.urlretrieve(url, f"./{folder_path}/" + str(img_count) + url[-4:])
        except:
            # 보안 설정 때문에 튕길 수도 있음
            pass


