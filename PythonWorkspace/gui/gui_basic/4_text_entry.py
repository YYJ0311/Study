from tkinter import *

root = Tk()
root.title("Start GUI") # 프로그램 이름
root.geometry("640x480") # 가로x세로 크기지정

txt = Text(root, width=30, height=5)
txt.pack()
txt.insert(END, "글자를 입력하세요") # 텍스트 기본값

e = Entry(root, width=30) # 엔터 입력 불가. 한 줄로만 입력 가능.
e.pack()
e.insert(0, "한 줄만 입력해요")

def btncmd():
    # 내용 출력
    print(txt.get("1.0", END)) # 1 : 첫번째 라인, 0 : 컬럼 위치. 1.0, END : 처음부터 끝까지
    print(e.get())

    # 내용 삭제
    txt.delete("1.0", END)
    e.delete(0, END)

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop() # 창이 닫히지 않게 만듦