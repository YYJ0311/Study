from tkinter import *

root = Tk()
root.title("Start GUI") # 프로그램 이름
root.geometry("640x480") # 가로x세로 크기지정

frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y") # y : 위아래로 꽉 참

# set이 없으면 scroll을 내려도 다시 올라옴. 리스트로 스크롤바 제어
listbox = Listbox(frame, selectmode="extended", height=10, yscrollcommand=scrollbar.set)
for i in range(1, 32): # 1 ~ 31 일
    listbox.insert(END, str(i) + "일") # 맨 뒤에 1일, 2일, ...
    listbox.pack(side="left")

scrollbar.config(command=listbox.yview) # 스크롤바로 리스트 제어

root.mainloop() # 창이 닫히지 않게 만듦