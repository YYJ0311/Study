from genericpath import isfile
from tkinter import *
import pickle
import os # 파일 존재 여부 체크

root = Tk()
root.title("제목 없음 - Windows 메모장") # 프로그램 이름
root.geometry("640x480") # 가로x세로 크기지정

# 상하 스크롤
scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")

# 텍스트 entry
txt = Text(root, width=640, height=480, yscrollcommand=scrollbar.set) # 스크롤바 매핑
txt.pack(fill="both", expand=True, side="left")

scrollbar.config(command=txt.yview) # 스크롤바 매핑

# 열기, 저장
filename = "mynote.txt"

def save():
    with open("mynote.txt", "w", encoding="utf8") as file:
        file.write(txt.get("1.0", END)) # 입력한 텍스트를 파일에 쓰기

def read():
    if os.path.isfile(filename): # 파일이 있으면, True 없으면 False
        with open("mynote.txt", "r", encoding="utf8") as file:
            txt.delete("1.0", END) # 불러오기 전 내용 초기화
            txt.insert(END, file.read()) # 불러오기
    else:
        print("파일이 없습니다.")

# 파일 메뉴
menu = Menu(root)

menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="열기", command=read) # 텍스트 호출
menu_file.add_command(label="저장", command=save) # 텍스트 저장
menu_file.add_separator()
menu_file.add_command(label="끝내기", comman=root.quit) # 프로그램 종료

menu.add_cascade(label="파일", menu=menu_file)

# 편집, 서식, 보기, 도움말 메뉴
menu.add_cascade(label="편집")
menu.add_cascade(label="서식")
menu.add_cascade(label="보기")
menu.add_cascade(label="도움말")

root.resizable(True, True) # x(너비), y(높이) 값 변경 가능

root.config(menu=menu) # menu 추가
root.mainloop() # 창이 닫히지 않게 만듦