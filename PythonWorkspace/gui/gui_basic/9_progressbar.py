import time
import tkinter.ttk as ttk # progressbar 사용하기 위한 import
from tkinter import *

root = Tk()
root.title("Start GUI") # 프로그램 이름
root.geometry("640x480") # 가로x세로 크기지정

# progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate") # indeterminate : 결정되지 않은 상태
# progressbar = ttk.Progressbar(root, maximum=100, mode="determinate") # determinate : 차오르는 모양
# progressbar.start(10) # 10 ms 마다 움직임
# progressbar.pack()

# def btncmd():
#     progressbar.stop() # 중지

# btn = Button(root, text="중지", command=btncmd)
# btn.pack()

p_var2 = DoubleVar() # 퍼센트가 소수점으로도 반영되게끔 Double로 만듦

progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()

def btncmd2():
    for i in range(1, 101): # 1 ~ 100
       time.sleep(0.01) # 0.01초 대기

       p_var2.set(i) # progressbar 의 값 설정
       progressbar2.update() # for문이 돌아갈 때마다 gui에 반영해주기 위함
       print(p_var2.get())

btn = Button(root, text="시작", command=btncmd2)
btn.pack()

root.mainloop() # 창이 닫히지 않게 만듦