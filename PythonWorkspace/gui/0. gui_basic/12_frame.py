from tkinter import *

root = Tk()
root.title("Start GUI") # 프로그램 이름
root.geometry("640x480") # 가로x세로 크기지정

Label(root, text="메뉴를 선택해 주세요").pack(side="top")

Button(root, text="주문하기").pack(side="bottom")

frame_burger = Frame(root, relief="solid", bd=1) # relief : 테두리 모양, bd : 외곽선
frame_burger.pack(side="left", fill="both", expand=True) # side : 위치, fill : 위아래 채움, expand : 좌우 확장

Button(frame_burger, text="햄버거").pack() # frame_burger 프레임 안에 버튼 생성
Button(frame_burger, text="치즈버거").pack()
Button(frame_burger, text="치킨버거").pack()

frame_drink = LabelFrame(root, text="음료") # 제목이 있는 프레임
frame_drink.pack(side="right", fill="both", expand=True)

Button(frame_drink, text="콜라").pack()
Button(frame_drink, text="사이다").pack()

root.mainloop() # 창이 닫히지 않게 만듦