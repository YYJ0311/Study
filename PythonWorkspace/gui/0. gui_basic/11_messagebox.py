import tkinter.messagebox as msgbox # messagebox 사용하기 위한 import
from tkinter import *

root = Tk()
root.title("Start GUI") # 프로그램 이름
root.geometry("640x480") # 가로x세로 크기지정

# 기차 예매 시스템
def info():
    msgbox.showinfo("알림", "정상적으로 예매 완료되었습니다.")

def warn():
    msgbox.showwarning("경고", "해당 좌석은 매진되었습니다.")

def error():
    msgbox.showerror("에러", "결제 오류가 발생했습니다.")

def okcancel():
    msgbox.askokcancel("확인 / 취소", "해당 좌석은 유아동반석입니다. 예매하시겠습니까?")

def retrycancel():
    response = msgbox.askretrycancel("재시도 / 취소", "일시적인 오류입니다. 다시 시도하시겠습니까?")
    print("응답:", response) # 다시시도 = True(1), 취소 = False(0)
    if response == 1:
        print("재시도")
    elif response == 0:
        print("취소")

def yesno():
    msgbox.askyesno("예 / 아니오", "해당 좌석은 역방향입니다. 예매하시겠습니까?")

def yesnocancel():
    response = msgbox.askyesnocancel(title=None, message="예매 내역이 저장되지 않았습니다.\n저장 후 프로그램을 종료하시겠습니까?")
    # title을 안 쓰고 싶은 경우 message로 내용 전달
    # 네 : 저장 후 종료
    # 아니오 : 저장하지 않고 종료
    # 취소 : 프로그램 종료 취소(현재 화면에서 계속 작업)
    print("응답:", response) # True(1), False(0), None
    if response == 1:
        print("예")
    elif response == 0:
        print("아니오")
    else:
        print("취소")

Button(root, comman=info, text="알림").pack()
Button(root, comman=warn, text="경고").pack()
Button(root, comman=error, text="에러").pack()

Button(root, comman=okcancel, text="확인 취소").pack() # okcancel : 확인/취소 버튼
Button(root, comman=retrycancel, text="재시도 취소").pack() # retrycancel : 다시시도/취소 버튼
Button(root, comman=yesno, text="예 아니오").pack() # yesno : 예/아니오 버튼
Button(root, comman=yesnocancel, text="예 아니오 취소").pack() # yesnocancel : 예/아니오/취소 버튼


root.mainloop() # 창이 닫히지 않게 만듦