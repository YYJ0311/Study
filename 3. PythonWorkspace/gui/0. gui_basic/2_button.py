from tkinter import *

root = Tk()
root.title("Start GUI") # 프로그램 이름

btn1 = Button(root, text="버튼1") 
btn1.pack() # pack을 통해서 mainloop에 추가시킴

btn2 = Button(root, padx=5, pady=10, text="버튼2") # x, y축으로 padding 줌
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text="버튼3")
btn3.pack()

btn4 = Button(root, width=10, height=3, text="버튼4") # 버튼 크기 자체를 설정
btn4.pack()

btn4b = Button(root, width=10, height=3, text="버튼4bbbbbbbbbbbbbbbb") # 버튼 내용이 많아지면 짤림
btn4b.pack()

btn5 = Button(root, fg="red", bg="yellow", text="버튼5") # forground = 글자색, background = 배경색
btn5.pack()

photo = PhotoImage(file="gui/gui_basic/img.png")
btn6 = Button(root, image=photo)
btn6.pack()

def btncmd():
    print("버튼이 클릭되었어요")

btn7 = Button(root, text="동작하는 버튼", command=btncmd)
btn7.pack()

root.mainloop() # 창이 닫히지 않게 만듦