import tkinter.ttk as ttk # combobox 사용하기 위한 import
from tkinter import *
from typing import List

root = Tk()
root.title("Start GUI") # 프로그램 이름
root.geometry("640x480") # 가로x세로 크기지정

values = [str(i) + "일" for i in range(1, 32)] # 1 ~ 31 까지의 숫자
combobox = ttk.Combobox(root, height=5, values=values)
combobox.pack()
combobox.set("카드 결제일") # 최초 목록의 제목 & 버튼 클릭을 통한 값 설정

readonly_combobox = ttk.Combobox(root, height=10, values=values, state="readonly") # 선택만 가능, 입력 불가
readonly_combobox.current(0) # 0번째 인덱스 값 선택
readonly_combobox.pack()

def btncmd():
    print(combobox.get())
    print(readonly_combobox.get())

btn = Button(root, text="선택", command=btncmd)
btn.pack()

root.mainloop() # 창이 닫히지 않게 만듦