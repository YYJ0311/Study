from tkinter import *
from typing import List

root = Tk()
root.title("Start GUI") # 프로그램 이름
root.geometry("640x480") # 가로x세로 크기지정

listbox = Listbox(root, selectmode="extended", height=0) # 그 외 selectmode="single". height는 보여줄 갯수. 0이면 모두 보여줌
listbox.insert(0, "사과")
listbox.insert(1, "딸기")
listbox.insert(2, "바나나")
listbox.insert(END, "수박") # 마지막 값
listbox.insert(END, "포도")
listbox.pack()

def btncmd():
    # 삭제
    # listbox.delete(END) # 마지막 항목을 삭제함
    # listbox.delete(0) # 처음 항목을 삭제함

    # 갯수 확인
    # print("리스트에는", listbox.size(), "개가 있어요")

    # 항목 확인
    # print("1번째부터 3번째 까지의 항목 : ", listbox.get(0, 2)) # 0부터 2까지

    # 선택된 항목 확인. 현재(current) 선택된(selection) 항목의 인덱스로 보여줌.
    print("선택된 항목 : ", listbox.curselection()) # ctrl+클릭으로 여러개 선택 가능.

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop() # 창이 닫히지 않게 만듦