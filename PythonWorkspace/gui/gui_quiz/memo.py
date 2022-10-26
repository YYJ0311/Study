from tkinter import *
import pickle

root = Tk()
root.title("제목 없음 - Windows 메모장") # 프로그램 이름
root.geometry("640x480") # 가로x세로 크기지정

# 상하 스크롤
frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

# 텍스트 entry
txt = Text(frame, width=640, height=480, yscrollcommand=scrollbar.set)
txt.pack(side="left")

scrollbar.config(command=txt.yview)

# 파일 저장
def save():
    with open("mynote.txt", "w", encoding="utf-8") as note_file:
        print(txt.get("1.0", END))
        note_file.write(txt.get("1.0", END))

# 파일 읽기
def read():
    with open("mynote.txt", "r", encoding="utf-8") as note_file:
        print(note_file.read())
        txt.insert(END, note_file.read())

# 파일 메뉴
menu = Menu(root)

menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="열기", command=read()) # 텍스트 호출
menu_file.add_separator()
menu_file.add_command(label="저장", command=save()) # 텍스트 저장
menu_file.add_separator()
menu_file.add_command(label="끝내기", comman=root.quit) # 프로그램 종료

menu.add_cascade(label="파일", menu=menu_file)

# 편집 메뉴
menu.add_cascade(label="편집")
# 서식 메뉴
menu.add_cascade(label="서식")
# 보기 메뉴
menu.add_cascade(label="보기")
# 도움말 메뉴
menu.add_cascade(label="도움말")

root.resizable(True, True) # x(너비), y(높이) 값 변경 가능

root.config(menu=menu) # menu 추가
root.mainloop() # 창이 닫히지 않게 만듦