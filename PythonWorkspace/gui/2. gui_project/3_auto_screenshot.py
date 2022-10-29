import time
from tkinter import Image
from PIL import ImageGrab # pip install Pillow 다운로드 필요

time.sleep(5) # 5초 대기 : 사용자가 준비하는 시간

# 2초 간격으로 10개 이미지 저장하기
for i in range(1, 11):
    img = ImageGrab.grab() # 현재 스크린의 이미지를 가져옴
    img.save("image{}.png".format(i)) # 파일로 저장 (image1.png ~ image10.png)
    time.sleep(2) # 2초 단위

# 실행하면 컴퓨터 화면이 2초 간격으로 10장 스크린샷됨