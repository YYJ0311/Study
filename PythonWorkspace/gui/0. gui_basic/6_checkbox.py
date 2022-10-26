from tkinter import *
from typing import List

root = Tk()
root.title("Start GUI") # 프로그램 이름
root.geometry("640x480") # 가로x세로 크기지정

chkvar = IntVar() # chkvar에 int형으로 값을 저장한다는 의미
chkbox = Checkbutton(root, text="오늘 하루 보지 않기", variable=chkvar)
# chkbox.select() # 초기 선택된 값으로 지정
# chkbox.deselect() # 초기 선택되지 않은 값으로 지정
chkbox.pack()

chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text="일주일동안 보지 않기", variable=chkvar2)
chkbox2.pack()

def btncmd():
    print(chkvar.get()) # 체크박스의 값을 가져옴. 0 : 체크 해제, 1: 체크
    print(chkvar2.get())

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop() # 창이 닫히지 않게 만듦