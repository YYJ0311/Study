from tkinter import *

root = Tk()
root.title("Start GUI") # 프로그램 이름
root.geometry("640x480") # 가로x세로 크기지정

# btn1 = Button(root, text="버튼1")
# btn2 = Button(root, text="버튼2")

# # btn1.pack()
# # btn2.pack()
# # btn1.pack(side="left")
# # btn2.pack(side="right")

# btn1.grid(row=0, column=0)
# btn2.grid(row=1, column=1)

# 애플 키보드 만들기
# 맨 윗줄
btn_f16 = Button(root, text="F16", width=5, height=2) # btn에 pad를 주면 글자별로 너비가 달라서 버튼의 크기가 달라짐
btn_f17 = Button(root, text="F17", width=5, height=2) # 따라서 pad 대신 width와 height를 주면 버튼의 크기를 일정하게 할 수 있다.
btn_f18 = Button(root, text="F18", width=5, height=2)
btn_f19 = Button(root, text="F19", width=5, height=2)

btn_f16.grid(row=0,column=0, sticky=N+E+W+S, padx=3, pady=3) # sticky : 지정한 방향으로 늘임
btn_f17.grid(row=0,column=1, sticky=N+E+W+S, padx=3, pady=3) # grid에도 pad를 줌으로써 각 버튼별 간격을 줌
btn_f18.grid(row=0,column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_f19.grid(row=0,column=3, sticky=N+E+W+S, padx=3, pady=3)

# clear 줄
btn_clear = Button(root, text="clear", width=5, height=2)
btn_equal = Button(root, text="=", width=5, height=2)
btn_div = Button(root, text="/", width=5, height=2)
btn_mul = Button(root, text="*", width=5, height=2)

btn_clear.grid(row=1, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_equal.grid(row=1, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_div.grid(row=1, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_mul.grid(row=1, column=3, sticky=N+E+W+S, padx=3, pady=3)

# 7 시작 줄
btn_7 = Button(root, text="7", width=5, height=2)
btn_8 = Button(root, text="8", width=5, height=2)
btn_9 = Button(root, text="9", width=5, height=2)
btn_sub = Button(root, text="-", width=5, height=2)

btn_7.grid(row=2, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_8.grid(row=2, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_9.grid(row=2, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_sub.grid(row=2, column=3, sticky=N+E+W+S, padx=3, pady=3)

# 4 시작 줄
btn_4 = Button(root, text="4", width=5, height=2)
btn_5 = Button(root, text="5", width=5, height=2)
btn_6 = Button(root, text="6", width=5, height=2)
btn_add = Button(root, text="+", width=5, height=2)

btn_4.grid(row=3, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_5.grid(row=3, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_6.grid(row=3, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_add.grid(row=3, column=3, sticky=N+E+W+S, padx=3, pady=3)

# 1 시작 줄
btn_1 = Button(root, text="1", width=5, height=2)
btn_2 = Button(root, text="2", width=5, height=2)
btn_3 = Button(root, text="3", width=5, height=2)
btn_enter = Button(root, text="enter") # 세로로 합쳐짐

btn_1.grid(row=4, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_2.grid(row=4, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_3.grid(row=4, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_enter.grid(row=4, column=3, rowspan=2, sticky=N+E+W+S, padx=3, pady=3) # row 2개를 합침

# 0 시작 줄
btn_0 = Button(root, text="0", width=5, height=2) # 가로로 합쳐짐
btn_point = Button(root, text=".", width=5, height=2)

btn_0.grid(row=5, column=0, columnspan=2, sticky=N+E+W+S, padx=3, pady=3)
btn_point.grid(row=5, column=2, sticky=N+E+W+S, padx=3, pady=3)

root.mainloop() # 창이 닫히지 않게 만듦