from tkinter import *

root = Tk()
root.title("Start GUI") # 프로그램 이름
root.geometry("640x480") # 가로x세로 크기지정
# root.geometry("640x480+300+300") # 프로그램 뜨는 위치 지정. + x좌표 + y좌표

root.resizable(False, False) # x(너비), y(높이) 값 변경 불가. 창 크기 변경 불가

root.mainloop() # 창이 닫히지 않게 만듦