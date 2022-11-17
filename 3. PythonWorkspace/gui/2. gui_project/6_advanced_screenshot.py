import time
import keyboard # pip install keyboard 다운로드 필요
from PIL import ImageGrab

def screenshot():
    curr_time = time.strftime("_%Y%m%d_%H%M%S") # ex)_20221029_102930
    img = ImageGrab.grab()
    img.save("image{}.png".format(curr_time))

keyboard.add_hotkey("F9", screenshot) # 사용자가 f9 키를 누르면 스크린샷 저장
# keyboard.add_hotkey("ctrl+shift+s", screenshot) # 복합키도 가능

keyboard.wait("esc") # 사용자가 esc를 누를 때까지 프로그램 수행