### 숫자형
print(5)
print(-10)
print(3.14)
print(2*8) # 16
print(2**3) # 2^3 = 8
print(5%3) # 2 (나머지)
print(5//3) # 1 (몫)


### 문자열 자료형
print('풍선')
print("나비")
print("ㅎ"*5) # ㅎㅎㅎㅎㅎ


### 참/거짓 판단 Boolean형
print(5 > 10) # False
print(5 < 10) # True
print(not True) # False
print(not (5>10)) # True
print(1 != 3) # True
print(not(1 != 3)) # False

print((3 > 0) and (3 < 5)) # True
print((3 > 0) & (3 < 5)) # True
print((3 > 0) or (3 > 5)) # True
print((3 > 0) | (3 > 5)) # True


### 변수
animal = "강아지"
age = 4
is_old = age > 3
print(animal+"는"+str(age)+"살 입니다.")
print(animal+" 나이가 많은가요?"+str(is_old))


### 숫자처리 함수
print(abs(-5)) # 절대값 5
print(pow(4, 2)) # 4^2 = 16
print(max(5, 12)) # 최대값 12
print(round(3.14)) # 반올림 3

from math import *
import site
from this import d
from tkinter import Misc
from typing import final

from travel import vietnam # 파이썬에서 제공하는 math 라이브러리 사용
print(floor(4.99)) # 내림 4
print(ceil(3.14)) # 올림 4
print(sqrt(16)) # 제곱근 4


### 랜덤함수 
from random import *
print(random()) # 0.0 ~ 1.0 임의의 값 생성
print(random() * 10) # 0.0 ~ 10.0 임의의 값
print(int(random() * 10)) # 0 ~ 10
print(int(random() * 10) + 1) # 1 ~ 10


### 로또 수 뽑기
print(int(random() * 45) + 1) # 1 ~ 45
print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성
print(randint(1, 45)) # 1 ~ 45 이하


##### Quiz) 코딩 스터디 모임을 새로 만들었습니다.
# 월 4회 스터디를 하는데 3번은 온라인으로 하고 1번은 오프라인으로 하기로 했습니다.
# 아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오.
# 조건
#     1. 랜덤으로 날짜를 뽑아야 함
#     2. 월별 날짜는 다름을 감안하여 최소 일수인 28 이내로 정함
#     3. 매월 1~3일은 스터디 준비를 해야하므로 제외
from random import *
날짜 = randint(4,28)
print("오프라인 스터디 모임 날짜는 매월 "+str(날짜)+"일로 선정되었습니다.")

### 문자열
sentence = '나는 나비'
print(sentence)
sentence2 = """
나는 나비
너는 나방
"""
print(sentence2) # """은 줄바꿈도 포함해서 출력한다.


### 슬라이싱
jumin = "990110-1234567"
print("성별 : " + jumin[7]) # index는 0부터 시작
print("연 : " + jumin[0:2]) # 0번째 부터 2번째 직전(1번째 까지)
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])
print("생년월일 : " + jumin[:6]) # 처음부터 6번째 직전까지
print("뒤 7자리 : " + jumin[7:]) # 7번째부터 끝까지
print("뒤 7자리(뒤에서부터) : " + jumin[-7:]) # 맨 뒤에서 7번째부터 끝까지


### 문자열 처리 함수
python = "Python is Apple n"
print(python.lower()) # 소문자 변환
print(python.upper()) # 대문자 변환
print(python[0].isupper()) # 0번째가 대문자인지? True
print(len(python)) # 길이
print(python.replace("Python", "Java")) # 문자 변환

index = python.index("n") # n이 몇번째에 있는지, 5
print(index)
print(python.find("n")) # 5
    # find와 index의 차이
    # print(python.find("Java")) # 값이 없는 경우 -1 반환
    # print(python.index("Java")) # 에러출력
print(python.count("n")) # n이 몇번 사용됐는지, 2


### 문자열 포맷
print("a" + "b")# ab
print("a", "b") # a b
    # 방법 1
print("나는 %d살입니다." % 20) # d : 정수값
print("나는 %s을 좋아해요." % "파이썬") # s : 스트링
print("Apple 은 %c로 시작해요." % "A") # c : character, 한 글자만 받음
    # %s
print("나는 %s살입니다." % 20) # %s는 정수나 문자 상관없이 사용 가능
print("나는 %s색과 %s색을 좋아해요." % ("파란","빨간")) # () 통해서 값을 순서대로 넣어줌
    # 방법 2
print("나는 {}살입니다.".format(20)) # 나는 20살입니다.
print("나는 {}색과 {}색을 좋아해요.".format("파란","빨간"))
print("나는 {1}색과 {0}색을 좋아해요.".format("파란","빨간")) #0번째, 1번째 지정도 가능
    # 방법 3
print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color="빨간")) #변수처럼 사용가능
    # 방법 4
age = 20 
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.") #문장을 f로 시작


### 탈출문자
print("백문이 불여일견\n백견이 불여일타") # \n:줄바꿈
    # 저는 "유영준" 입니다. 를 출력하는 방법
    # print("저는 '유영준' 입니다.")
    # print('저는 "유영준" 입니다.')
    # 탈출문자 \", \' 를 사용하여 문장내에서 따옴표를 사용할 수 있다.
print("저는 \"유영준\" 입니다.")
print("저는 \'유영준\' 입니다.")
    # \\ : 문장 내에서 하나의 \ 로 표시됨
#print("C:\Users\Joon\Desktop\연습\Study>") <= 문장 내에서 \ 하나만 존재하면 뒤의 문자와 합쳐져서 사용이 됨. \U가 없기 때문에 에러 발생.
print("C:\\Users\\Joon\\Desktop\\연습\\Study") # C:\Users\Joon\Desktop\연습\Study
    # \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine") # PineApple
    # \b : 백스페이스(한 글자 삭제)
print("Redd\bApple") # RedApple
    # \t : 탭 역할
print("Red\tApple") # Red     Apple


### Quiz) 사이트 별로 비밀번호를 만들어 주는 프로그램을 작성하시오
# 예) http://naver.com
# 규칙1 : http:// 부분은 제외 => naver.com
# 규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!" 로 구성
#                 (nav)               (5)             (1)         (!)
# 예) 생성된 비밀번호 : nav51!
url = "http://naver.com"
site = url.replace("http://","")
index = site.find(".") # 첫 .의 위치
site = site[0:index] 
    # 위의 2줄을 site[:site.find(".")] 으로 간단히 표현할 수도 있다. find 대신 index를 써도 됨.
first3 = site[0:3] # 남은 글자 중 처음 세자리
countAll = len(site) # 글자 갯수
countE = site.count("e") # e 갯수
password = f"{first3}{countAll}{countE}!"
print(password)
    # 선생님은 다음처럼 표시함
password = site[:3] + str(len(site)) + str(site.count("e")) + "!"
print("{0} 의 비밀번호는 {1} 입니다".format(url, password))
    # url만 바꿔주면서 사용 가능함


### 리스트[]
    # 지하철 칸별로 10명, 20명, 30명
subway1 = 10
subway2 = 20
subway3 = 30
    # 를 리스트로 다음과 같이 표현할 수 있다.
subway = [10, 20, 30]
    # 20이 몇번째인지 확인
print(subway.index(20)) # 1
    # 숫자가 추가됨
subway.append(40)
print(subway) # [10, 20, 30, 40]
    # 50을 10과 20 사이에 넣기
subway.insert(1, 50) # 50을 1번째에 넣는다
print(subway) # [10, 50, 20, 30, 40]
    # 뒤에서부터 한개씩 제거
print(subway.pop()) # 뒤부터 한개씩 꺼내는 함수
print(subway) # [10, 50, 20, 30]
subway.pop()
subway.pop()
print(subway) # [10, 50]
    # 같은 숫자가 몇개 있는지
subway.append(10)
print(subway.count(10)) # 2
    # 정렬하기
num_list = [5,2,4,3,1]
num_list.sort()
print(num_list) # [1, 2, 3, 4, 5] 순서대로 정렬됨
    # 역 정렬
num_list.reverse()
print(num_list) # [5, 4, 3, 2, 1]
    # 모두 지우기
num_list.clear()
print(num_list) # [] 빈 리스트가 됨
    # 리스틑 다양한 자료형과 함께 사용 가능
mix_list = ["조세호", 20, True]
print(mix_list)
    # 리스트 합치기
num_list = [5,2,4,3,1]
num_list.extend(mix_list)
print(num_list) # [5, 2, 4, 3, 1, '조세호', 20, True]


### 사전(dictionary)
cabinet = {3:"유재석", 100:"김태호"} # key:value 형식
print(cabinet[3]) # 유재석. key로 조회함
print(cabinet.get(3)) # 유재석
# print(cabinet[5]) # 오류와 동시에 프로그램 종료됨
# print(cabinet.get(5)) # 값이 없어서 None으로 출력되고 프로그램 계속됨
# print(cabinet.get(5, "사용가능")) # 값이 없으면 None 대신에 사용가능이 출력됨
print(3 in cabinet) # True
print(5 in cabinet) # False
cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])
    # 새 key와 value 추가
cabinet["C-20"] = "조세호"
print(cabinet) # {'A-3': '유재석', 'B-100': '김태호', 'C-20': '조세호'}
cabinet["A-3"] = "김종국"
print(cabinet) # {'A-3': '김종국', 'B-100': '김태호', 'C-20': '조세호'} 유재석이 김종국으로 업데이트됨
    # key와 value 제거
del cabinet["A-3"]
print(cabinet) # {'B-100': '김태호', 'C-20': '조세호'}
    # key만 출력
print(cabinet.keys()) # dict_keys(['B-100', 'C-20'])
    # value만 출력
print(cabinet.values()) # dict_values(['김태호', '조세호'])
    # key와 value 모두 출력
print(cabinet.items()) # dict_items([('B-100', '김태호'), ('C-20', '조세호')])
    # 모두 제거
cabinet.clear()
print(cabinet) # {}
print(cabinet.clear()) # None. 위와 다르게 나옴..


### 튜플
# 리스트와 다르게 내용 변경이나 추가를 할 수 없다. 하지만 속도가 리스트보다 빠르다. 따라서 변경되지 않는 목록을 사용할 때 사용함
menu = ("돈까스", "치즈까스")
print(menu[0]) # 돈까스
# menu.add("생선까스") # 오류. add 불가
name = "김종국"
age= "20"
hobby = "코딩"
print(name, age, hobby)
    # 위를 튜플로 만들면 다음과 같음
(name,age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)


### 집합 (set)
# 중복 안 됨, 순서 없음
my_set = {1,2,3,3,3}
print(my_set) # {1, 2, 3} 중복을 허용하지 않음
java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])
    # 교집합
print(java & python) # {'유재석'}
print(java.intersection(python)) # {'유재석'}
    # 합집합
print(java | python) # {'박명수', '김태호', '양세형', '유재석'}
print(java.union(python)) # {'박명수', '김태호', '양세형', '유재석'}
    # 차집합 (java는 할 수 있지만 python은 할 줄 모르는 개발자)
print(java - python) # {'양세형', '김태호'}
print(java.difference(python)) # {'양세형', '김태호'}
    # python 할 줄 아는 사람이 늘어남
python.add("김태호")
print(python) # {'유재석', '박명수', '김태호'}
    # java를 까먹은 사람이 생김
java.remove("김태호")
print(java) # {'유재석', '양세형'}


### 자료구조의 변경
menu = {"커피", "우유", "주스"}
print(menu, type(menu)) # {'커피', '우유', '주스'} <class 'set'>. set으로 만들어졌다고 보여줌
menu = list(menu)
print(menu, type(menu)) # ['우유', '커피', '주스'] <class 'list'>
menu = tuple(menu)
print(menu, type(menu)) # ('커피', '우유', '주스') <class 'tuple'>
menu = set(menu)
print(menu, type(menu)) # 다시 set으로 돌아 옴\


##### Quiz) 학교에서는 파이썬 코딩 대회를 주최합니다.
# 참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
# 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
# 추첨 프로그램을 작성하시오.
# 조건1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20 이라고 가정
# 조건2 : 댓글 내용과 상관없이 무작위로 추첨하되 중복 불가
# 조건3 : random 모듈의 shuffle과 sample 활용
# (출력예제)
# -- 당첨자 발표 --
# 치킨 당첨자 : 1
# 커피 당첨자 : [2, 3, 4]
# -- 축하합니다 --
# (활용예제)
# from random import *
# list = [1,2,3,4,5]
# print(list)
# shuffle(list) # 랜덤으로 섞음
# print(list)
# print(sample(list, 1)) # 섞인 리스트에서 1개 출력
from random import *
users = range(1,21) # 1부터 21 전까지 = 1~20
# print(users) # 이 때 출력을 해보면 숫자가 나오는게 아닌 range(1,21)로 나온다. 타입이 range이기 때문.
print(type(users)) # <class 'range'>. 따라서 list 함수를 사용할 수 없기 때문에 타입을 바꿔준다
users = list(users)
print(users) # 1부터 20까지 숫자로 출력됨
shuffle(users)
winner = sample(users, 4)
print("-- 당첨자 발표 -- \n치킨당첨자 : "+str(winner[0])+"\n커피 당첨자 : "+str(winner[1:])+"\n-- 축하합니다 --")
    # 다음처럼도 같이 출력 가능
print(" -- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(winner[0]))
print("커피 당첨자 : {0}".format(winner[1:]))
print(" -- 축하합니다 --")


### if
# weather = input("오늘 날씨는 어때요? ") # input으로 사용자 입력 받을 수 있음
#     # if 조건:
#     #     실행 명령문
# if weather == "비"or weather == "눈":
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("오늘은 준비물이 필요 없어요")

# temp = int(input("기온은 어때요? ")) # 기온은 숫자이므로 int로 감싸줌
# if 30 <= temp:
#     print("너무 더워요. 나가지 마세요!")
# elif 10 <= temp and temp < 30:
#     print("괜찮은 날씨에요.")
# elif 0 <= temp < 10: # and를 한번에 표시하는 것도 가능
#     print("외투를 챙기세요.")
# else:
#     print("너무 추워요. 나가지 마세요!")


### for
print("대기번호 : 1") # 대기번호를 1부터 프린트 해야 함
for waiting_no in [1, 2, 3, 4, 5]:
    print("대기번호 : {0}".format(waiting_no)) # 대기번호 1부터 5까지 나옴

    # 순차적으로 커지는 수에 대해서
for waiting_no in range(5): # 0 ~ 4까지 나옴. range(1, 6)라고 쓰면 1부터 5까지 출력됨.
    print("{0}".format(waiting_no))

starbucks =["아이언맨", "토르", "그루트"]
for customer in starbucks:
    print("{0} 님, 커피가 준비되었습니다.".format(customer))


### while
customer = "토르"
index = 5
while index >= 1:
    print("{0} 님, 커피가 준비되었습니다. {1}번 남았습니다.".format(customer, index))
    index -= 1
    if index == 0:
        print("커피는 폐기처분되었습니다.")

# customer = "아이언맨"
# index = 1
# while True: # 무한루프. 계속 반복됨.
#     print("{0} 님, 커피가 준비되었습니다. 호출 {1}회".format(customer, index))
#     index += 1
#     # 콘솔창 클릭하고 ctrl + c 로 강제종료

    # 맞는 손님이 입력될 때까지 계속해서 안내문을 출력하는 로직
# customer = "토르"
# person ="Unknown"
# while person != customer:
#     print("{0} 님, 커피가 준비되었습니다.".format(customer))
#     person = input("이름이 어떻게 되세요? ") # 토르라고 입력하면 while문에서 나오게 됨


### continue와 break
absent = [2, 5] # 결석한 번호
no_book = [7] # 7번 학생이 책을 안 갖고 옴
for student in range(1, 11): # 1부터 10번까지
    if student in absent:
        continue # for문으로 올라가서 이어가게됨(continue)
    elif student in no_book:
        print("오늘 수업 여기까지. {0}는 교무실로 와".format(student))
        break
    print("{0}야, 책을 읽어봐".format(student)) # 1~10 에서 2와 5을 제외하고 출력되다가, 7에서 break로 중단돼서 이후 출력되지 않음


### 한 줄 for
    # 출석번호 1 2 3 4 5가 있는데, 앞에 100을 붙이기로 함.
students = [1,2,3,4,5]
students = [i+100 for i in students]
print(students) # [101, 102, 103, 104, 105]

    # 학생 이름을 길이로 변환
students = ["Iron man", "Thor", "Groot"]
students = [len(i) for i in students]
print(students) # [8, 4, 5]

    # 학생 이름을 대문자로 변환
students = ["Iron man", "Thor", "Groot"]
students = [i.upper() for i in students]
print(students) # ['IRON MAN', 'THOR', 'GROOT']


##### Quiz) 당신은 Cocoa 서비스를 이용하는 택시 기사입니다.
# 50명의 승객과 매칭기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.
# 조건1 : 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해집니다.
# 조건2 : 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.
# 
# (출력문 예제)
# [O] 1번째 손님 (소요시간 : 15분)
# [ ] 2번째 손님 (소요시간 : 50분)
# [O] 3번째 손님 (소요시간 : 5분)
# ...
# [ ] 50번째 손님 (소요시간 : 16분)
# 
# 총 탑승 승객 : 2분
from random import *
count = 0 # 총 탑승 승객 수
for passenger in range(1, 51): # 50명의 승객에 대해서
    totalMatchingTime = int(random()*46)+5
    matchingTime = range(5, 16) # 매칭할 운행소요시간
    if totalMatchingTime in matchingTime:
        print("[O]" + str(passenger) + "번째 손님 (소요시간 : " + str(totalMatchingTime) + ")")
        count += 1
    else:
        print("[ ]" + str(passenger) + "번째 손님 (소요시간 : " + str(totalMatchingTime) + ")")
print("총 탑승 승객 : " + str(count) + " 분")

    # 선생님 풀이
from random import *
cnt = 0
for i in range(1, 51):
    time = randrange(5,51) # 5 ~ 50 무작위 뽑기
    if 5 <= time <= 15: # 매칭 성공
        print("[0] {0}번쨰 손님 (소요시간 : {1}분)".format(i, time))
        cnt += 1
    else: # 매칭 실패
        print("[ ] {0}번쨰 손님 (소요시간 : {1}분)".format(i, time))
print("총 탑승 승객 : {0} 분".format(cnt))


### 함수
def open_account():
    print("새로운 계좌가 생성되었습니다.")
open_account() # 함수 실행


### 전달값과 반환값
def deposit(balance, money): # balance와 money를 전달받음
    print("입금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance + money))
    return balance + money # 반환

def withdraw(balance, money): #출금
    if balance >= money: # 잔액이 출금보다 많으면
        print("출금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance - money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0}원 입니다.".format(balance))
        return balance

def withdraw_night(balance, money): # 저녁에 출금하면 수수료가 생김
    commission = 100 # 수수료 100원
    return commission, balance - money - commission # 튜플 형식으로 2개의 값을 ,로 구분하여 보내줌

balance = 0 # 잔액
balance = deposit(balance, 1000) # balance + money가 balance에 저장됨
print(balance) # 1000

balance = withdraw(balance, 2000) # 출금이 완료되지 않았습니다. 잔액은 1000원 입니다.
balance = withdraw(balance, 500) # 출금이 완료되었습니다. 잔액은 500원 입니다.

commission, balance = withdraw_night(balance, 400)
print("수수료 {0}원 이며, 잔액은 {1}원 입니다.".format(commission, balance))


### 기본값
# def profile(name, age, main_lang):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}".format(name, age, main_lang))
# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "자바")

    # 같은 학교, 반, 수업인 경우 기본값을 사용함
def profile(name, age=17, main_lang="파이썬"): # 17과 파이썬이 기본값
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}".format(name, age, main_lang))
profile("유재석")
profile("김태호")


### 키워드값
def profile(name, age, main_lang):
    print(name, age, main_lang)

profile(name="유재석", main_lang="파이썬", age=20)
profile(main_lang="자바", age=25, name="김태호") # 순서가 바뀌어도 상관없다


### 가변인자
# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t나이 : {1}\t".format(name,age), end="") # end="" : print문이 끝날 때 줄바꿈을 하지 않고 끝냄
#     print(lang1, lang2, lang3, lang4, lang5)
# profile("유재석", 20, "Python", "Java", "C", "C++", "C#")
# profile("김태호", 25, "Kotlin", "Swift", "", "", "") # 빈 값을 안 넣어주면 에러 발생. 매번 이렇게 빈 값을 넣어줘야 하는가? => 가변인자를 사용하면 됨

def profile(name, age, *language): # *로 시작하는 가변인자를 사용
    print("이름 : {0}\t나이 : {1}\t".format(name,age), end="") # end="" : print문이 끝날 때 줄바꿈을 하지 않고 끝냄
    for lang in language:
        print(lang, end="")
    print() # 마지막 줄바꿈
profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "JavaScript")
profile("김태호", 25, "Kotlin", "Swift")


### 지역변수와 전역변수
gun = 10
def checkpoint(soldiers): # 경계근무 나가는 군인 수
    gun = 20
    gun = gun - soldiers # checkpoint 안에서 gun을 초기화 시켜주지 않아서 오류발생. 바로 위에 gun을 새로 지정해줘야 한다.
    print("[함수 내] 남은 총 : {0}".format(gun))
print("전체 총 : {0}".format(gun))
checkpoint(2) # 2명이 경계 근무 나감
print("남은 총 : {0}".format(gun)) # 여전히 10개 남았다고 나옴

gun = 10
def checkpoint(soldiers):
    global gun # 전역 공간에 있는 gun 사용!
    gun = gun - soldiers 
    print("[함수 내] 남은 총 : {0}".format(gun)) # 10
print("전체 총 : {0}".format(gun)) # 8
checkpoint(2) # 2명이 경계 근무 나감
print("남은 총 : {0}".format(gun)) # 8

gun = 10
def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun # return을 함으로써 밖에 있는 gun에 영향을 줄 수 있음
print("전체 총 : {0}".format(gun)) # 8
gun = checkpoint_ret(gun, 2) # 2명이 경계 근무 나감
print("남은 총 : {0}".format(gun)) # 8


##### Quiz) 표준 체중을 구하는 프로그램을 작성하시오
# * 표준 체중 : 각 개인의 키에 적당한 체중
# (성별에 따른 공식)
# 남자 : 키(m) X 키(m) X 22
# 여자 : 키(m) X 키(m) X 21
# 조건1 : 표준 체중은 별도의 함수 내에서 계산
#     * 함수명 : std_weight
#     * 전달값 : 키(height), 성별(gender)
# 조건2 : 표준 체중은 소수점 둘째자리까지 표시
# (출력 예제)
# 키 175cm 남자의 표준 체중은 67.38kg 입니다.

    # 선생님 풀이
def std_weight(height, gender): # 키는 m 단위(실수), 성별은 "남자"/"여자"
    if gender == "남자":
        return height * height * 22
    else:
        return height * height * 21

height = 175 # cm 단위
gender = "남자"
weight = round(std_weight(height / 100, gender), 2) # round(반올림하는 값, 나타내는 소수점 자리 수)
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))


### 표준 입출력
print("Python", "Java", "JavaScript", sep=" vs ") # sep를 써서 파이썬과 자바 그리고 자바스크립트 사이에 " vs "를 넣음

print("Python", "Java", sep=",", end="? ") # end : 문장의 끝 부분을 변경
print("무엇이 더 재밌을까요?") # end를 사용함으로써 두 줄이 한 줄로 출력됨

import sys
print("Python", "Java", file=sys.stdout) # stdout : 표준출력
print("Python", "Java", file=sys.stderr) # stderr : 표준에러. 에러를 따로 처리할 때 사용

    # 시험 성적
scores = {"수학":0, "영어":50, "코딩": 100}
for subject, score in scores.items(): # items : key와 value로 표현. 여기서 subject가 key, score가 value
    print(subject.ljust(8), str(score).rjust(4), sep=":") 
    # 수학, 영어, 코딩이 각각 출력됨. 
    # ljust(8) : 8개의 공간을 확보하고 왼쪽 정렬. 
    # rjust(4) : 4칸의 공간을 확보하고 오른쪽 정렬.

    # 은행 대기 순번표 001, 002, 003, ...
for num in range(1, 21): # 1부터 20까지
    print("대기번호 : " + str(num).zfill(3)) # zfill(3) : 3개만큼의 공간을 확보하고 값이 없는 곳은 0으로 채움

# answer = input("아무 값이나 입력하세요 : ") # 사용자 입력을 통해서 값을 받게 되면 항상 "문자열" 형태로 저장된다.
# # answer = 10 # answer에 숫자를 넣고 타입 확인을 하면 int로 나옴
# print(type(answer)) # 10을 입력하든, "나는" 을 입력하든 str 타입으로 나온다.
# print("입력하신 값은 " + answer + "입니다.")


### 다양한 출력 포맷
    # 빈 자리는 빈 공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print("{0: >10}".format(500))

    # 양수일 땐 +로 표시, 음수일 땐 -로 표시
print("{0: >+10}".format(+500)) # +500
print("{0: >+10}".format(-500)) # -500

    # 왼쪽 정렬, 빈칸을 _로 채움
print("{0:_<+10}".format(500)) # 위와 부등호 방향 바뀜

    # 3자리마다 , 찍기
print("{0:,}".format(1000000000))

    # 3자리마다 ,를 찍고 +- 부호 붙이기
print("{0:+,}".format(1000000000))
print("{0:+,}".format(-1000000000))

    # 3자리마다 ,를 찍고 부호 붙이고, 자릿수 확보, 빈 자리는 ^로 채우기
print("{0:^<+30,}".format(100000000000)) # 30만큼 자리 확보하고 빈 자리는 ^로 채워짐

    # 소수점
print("{0:f}".format(5/3)) # 1.666667

    # 소수점을 특정 자리수 까지만 표시
print("{0:.2f}".format(5/3)) # 소수점 2번째 자리까지만 표시(3번째 자리에서 반올림)


### 파일 입출력
score_file = open("score.txt", "w", encoding="utf8") # 파일이름, w: write(쓰기 위함), 한글을 사용하기 위한 인코딩 정보
print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)
score_file.close() # 파일을 열었을 땐 항상 닫아줘야 함
# => 같은 경로에 수학과 영어 점수를 보여주는 score.txt 파일이 생긴 걸 볼 수 있다.

score_file = open("score.txt", "a", encoding="utf8") # a : append
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100") # print와 다르게 줄바꿈을 위해 \n 추가
score_file.close()
# => 수학 영어 아래에 과학 코딩 점수가 생김

score_file = open("score.txt", "r", encoding="utf8") # r : read
print(score_file.read()) # 모든 내용이 출력됨
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline(), end="") # 한 줄을 읽고 커서를 다음 줄로 이동. print의 자동 줄바꿈을 없애기 위해 end 사용.
print(score_file.readline(), end="")
print(score_file.readline(), end="")
print(score_file.readline(), end="")
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline()
    if not line: # line이 없으면 break
        break
    print(line, end="") # line이 있으면 print
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines() # list 형태로 저장
for line in lines:
    print(line, end="")
score_file.close()


### pickle
# 사용하고 있는 데이터를 파일 형태로 저장하는 것
import pickle
profile_file = open("profile.pickle", "wb") # wb : binary로 write. encoding 설정 안 함.
profile = {"이름":"박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
print(profile)
pickle.dump(profile, profile_file) # profile에 있는 정보를 file에 저장함. profile.pickle 파일이 생성됨.
profile_file.close()

profile_file = open("profile.pickle", "rb") # rb : binary 읽기
profile = pickle.load(profile_file) # 파일에 있는 정보를 profile에 불러오기
print(profile)
profile_file.close()


### with
import pickle
with open("profile.pickle", "rb") as profile_file: # profile.pickle 을 열어서 profile_file 에 저장
    print(pickle.load(profile_file)) # profile_file에 저장한 pickle 파일 열기. close가 필요없다

with open("study.txt", "w", encoding="utf8") as study_file: # study_file 파일 생성
    study_file.write("파이썬을 열심히 공부하고 있어요")
with open("study.txt", "r", encoding="utf8") as study_file: # 파일 읽기
    print(study_file.read()) # 파이썬을 열심히 공부하고 있어요


##### Quiz ) 당신의 회사에서는 매주 1회 작성해야 하는 보고서가 있습니다.
# 보고서는 항상 아래와 같은 형태로 출력되어야 합니다.
#
# - X 주차 주간보고 -
# 부서 : 
# 이름 : 
# 업무 요약 : 
# 
# 1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오.
# 조건 : 파일명은 '1주차.txt', '2주차.txt', ... 와 같이 만듦
import pickle
# for num in range(1, 3): # 1, 2주차 파일만 생성
#     with open(str(num)+"주차.txt", "w", encoding="utf8") as report_file:
#         report_file.write("- "+str(num)+" 주차 주간 보고 -\n부서 : \n이름 : \n업무 요약 : ")

    # 선생님 풀이
# for i in range(1, 3):
#     with open(str(i) + "주차.txt", "w", encoding="utf8") as report_file:
#         report_file.write("- {0} 주차 주간보고 -".format(i))
#         report_file.write("\n부서 : ")
#         report_file.write("\n이름 : ")
#         report_file.write("\n업무 요약 : ")


### 클래스
# name = "마린"
# hp = 40
# damage = 5 # 유닛의 공격력
# print("{} 유닛이 생성되었습니다.".format(name))
# print("체력 {0}, 공격력 {1}\n".format(hp, damage))

# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35

# print("{0} 유닛이 생성되었습니다.".format(tank_name))
# print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))

#     # 탱크 추가
# tank2_name = "탱크"
# tank2_hp = 150
# tank2_damage = 35

# print("{0} 유닛이 생성되었습니다.".format(tank2_name))
# print("체력 {0}, 공격력 {1}\n".format(tank2_hp, tank2_damage))

# def attack(name, location, damage):
#     print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(\
#         name, location, damage))

# attack(name, "1시", damage)
# attack(tank_name, "1시", tank_damage)
# attack(tank2_name, "1시", tank_damage)

    # 탱크가 많아지면 관리 힘듦. => class 사용
class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)


### __init__
# marine3 = Unit("마린") # 내용 부족으로 오류
# marine3 = Unit("마린", 40) # 내용 부족으로 오류
# init 함수에 정의된 self를 제외한 갯수만큼 보내줘야 객체를 만들 수 있다.


### 멤버 변수
wraith1 = Unit("레이스", 80, 5)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage)) # .으로 멤버 변수를 외부에서 사용 가능

wraith2 = Unit("빼앗은 레이스", 80, 5)
wraith2.clocking = True # 외부에서 변수 clocking 추가로 할당
if wraith2.clocking == True:
    print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))
# if wraith1.clocking == True: # 1에서는 해당 변수가 존재하지 않아서 오류 발생
#     print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))


### 메소드
print("---메소드---")
class AttackUnit: # attack, damaged 메소드를 만듦
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
            .format(self.name, location, self.damage))
    
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))

        if self.hp <= 0:
            print("{0} : 파괴었습니다.".format(self.name))
    
firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")
firebat1.damaged(25) # 파괴를 위해 공격 2번 받는다고 가정
firebat1.damaged(25) # 파괴되었습니다


### 상속
print("---상속---")
class NormalUnit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
            .format(self.name, location, self.speed))

class AttackUnit(NormalUnit): # NormalUnit 클래스를 상속받음
    def __init__(self, name, hp, speed, damage):
        NormalUnit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
            .format(self.name, location, self.damage))
    
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))

        if self.hp <= 0:
            print("{0} : 파괴었습니다.".format(self.name))
            
firebat1 = AttackUnit("파이어뱃", 50, 10, 16) # 스피드 10
firebat1.attack("5시")
firebat1.damaged(25)
firebat1.damaged(25) # 상속으로 인해 같은 결과 출력됨


### 다중상속
print("---다중상속---")
class Flyable: # 날 수 있는 기능
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    
    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
            .format(name, location, self.flying_speed))

class FlyableAttackUnit(AttackUnit, Flyable): # ,로 다중상속. 공중 공격 유닛
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # flying_speed가 있기 때문에 지상 speed는 0으로 줌
        Flyable.__init__(self, flying_speed)

valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")


### 메소드 오버라이딩
print("---메소드 오버라이딩---")
# class UnitAddingSpeed:
#     def __init__(self, name, hp, damage, speed):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         self.speed = speed
#         print("{0} 유닛이 생성되었습니다.".format(self.name))
#         print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))
    
#     def move(self, location):
#         print("[지상 유닛 이동]")
#         print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
#             .foramt(self.name, location, self.speed))

vulture = AttackUnit("벌쳐", 80, 10, 20)
battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

vulture.move("11시")
battlecruiser.fly(battlecruiser.name, "9시") # 지상유닛과 공중유닛의 이동 메소드가 다름 => 메소드 오버라이딩 이용

class ModifiedFlyableAttackUnit(AttackUnit, Flyable): # FlyableAttackUnit을 다음과 같이 수정
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # flying_speed가 있기 때문에 지상 speed는 0으로 줌
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

battlecruiser = ModifiedFlyableAttackUnit("배틀크루저", 500, 25, 3)
battlecruiser.move("10시")


### pass
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        pass # 아무것도 안 하고 일단 넘어가게 함. 완성된 것처럼 실행됨.
supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")
def game_over():
    pass
game_start() # 문구가 출력됨
game_over() # 아무것도 나오지 않고 pass 됨


### super
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        # Unit.__init__(self, name, hp, 0) # speed 0
        super().__init__(name, hp, 0) # 위와 같음. 대신 self를 빼고 사용.
        self.location = location

class Unit:
    def __init__(self):
        print("Unit 생성자")
class Flyable:
    def __init__(self):
        print("Flyable 생성자")
class FlyableUnit(Unit, Flyable):
    def __init__(self):
        super().__init__()
dropshop = FlyableUnit() # 2개를 상속받았지만 Unit 생성자만 출력됨. 2개 이상의 부모 클래스를 다중 상속받을 때, super()를 사용하면 같은 함수에 대하여 맨 처음에 상속받는 클래스만 상속된다.

class modifiedFlyableUnit(Unit, Flyable):
    def __init__(self):
        # 같은 이름의 함수에 대해 super를 사용하기보단 부모의 클래스를 각각 상속받아서 사용한다.
        Unit.__init__(self)
        Flyable.__init__(self)
dropshop = modifiedFlyableUnit() # Unit과 Flyable 모두 출력됨


### 스타크래프트
# 다른 파이썬 파일의 스크립트는 open으로 불러올 수 없고, import를 사용해야 한다.
# startcraft = open("starcraft.py", "r", encoding="utf8")
# print(startcraft)
# startcraft.close()
print("---스타크래프트---")
import starcraft


##### Quiz ) 주어진 코드를 활용하여 부동산 프로그램을 작성하시오.
# (출력 예제)
# 총 3채의 매물이 있습니다.
# 강남 아파트 매매 10억 2010년
# 마포 오피스텔 전세 5억 2007년
# 송파 빌라 월세 500/50 2000년
#
# [코드]
# class House:
#     # 매물 초기화
#     def __init__(self, location, house_type, deal_type, price, completion_year):
#         pass
#   
#     # 매물 정보 표시
#     def show_detail(self):
#         pass

class House:
    # 매물 초기화
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year
  
    # 매물 정보 표시
    def show_detail(self):
        print("위치 : {0}, 주거타입 : {1}, 매물종류 : {2}, 가격 : {3}, 준공일 : {4}"\
            .format(self.location, self.house_type, self.deal_type, self.price, self.completion_year))

    # 강남 아파트
class Gangnam_apt(House):
    def __init__(self):
        House.__init__(self, "강남", "아파트", "매매", "10억", "2010년")

    # 마포 오피스텔
class Mapo_opi(House):
    def __init__(self):
        House.__init__(self, "마포", "오피스텔", "전세", "5억", "2007년")

    # 송파 빌라
class Songpa_bill(House):
    def __init__(self):
        House.__init__(self, "송파", "빌라", "월세", "500/50", "2000년")

# 부동산 프로그램
g = Gangnam_apt()
m = Mapo_opi()
s = Songpa_bill()

total_deal = []
total_deal.append(g)
total_deal.append(m)
total_deal.append(s)

print("총 {0}채의 매물이 있습니다.".format(len(total_deal)))
for deal in total_deal:
    deal.show_detail()

    # 선생님 풀이
    # 매물 초기화와 매물 정보표시까지는 동일
houses = []
house1 = House("강남", "아파트", "매매", "10억", "2010년")
house2 = House("마포", "오피스텔", "전세", "5억", "2007년")
house3 = House("송파", "빌라", "월세", "500/50", "2000년")
houses.append(house1)
houses.append(house2)
houses.append(house3)

print("총 {0}채의 매물이 있습니다.".format(len(houses)))
for house in houses:
    house.show_detail()


### 예외처리
# try:
#     print("나누기 전용 계산기입니다.")
#     nums = []
#     nums.append(int(input("첫 번째 숫자를 입력하세요 : "))) # 6
#     nums.append(int(input("두 번째 숫자를 입력하세요 : "))) # 문자 "삼" 입력하면 에러 발생
#     # nums.append(int(nums[0]/nums[1]))
#     print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
# except ValueError: # 문자 입력으로 생긴 에러 처리
#     print("에러! 잘못된 값을 입력하였습니다.")
# except ZeroDivisionError as err: # 0으로 나눴을 때 생긴 에러 처리
#     print(err)
# except Exception as err: # 그 외 에러(리스트에 없는 값 때문에 생긴 에러)를 처리 & 에러 내용 표시
#     print("알 수 없는 에러가 발생하였습니다.")
#     print(err)


### 에러 발생시키기
# try:
#     print("한 자리 숫자 나누기 전용 계산기입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요 : "))
#     num2 = int(input("두 번째 숫자를 입력하세요 : "))
#     if num1 >= 10 or num2 >= 10:
#         raise ValueError # 필요한 상황에 특정 에러를 발생시키기. 아래 except 의 에러로 이어진다.
#     print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
# except ValueError:
#     print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")


### 사용자 정의 예외처리
# class BigNumberError(Exception): # 두 자리 숫자가 입력되었을 때의 에러를 만듦
#     # pass
#     def __init__(self, msg): # 에러에서 보여줄 메세지 정의
#         self.msg = msg

#     def __str__(self): # 에러에서 보여줄 메세지 정의
#         return self.msg
# try:
#     print("한 자리 숫자 나누기 전용 계산기입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요 : "))
#     num2 = int(input("두 번째 숫자를 입력하세요 : "))
#     if num1 >= 10 or num2 >= 10:
#         raise BigNumberError("입력값 : {0}, {1}".format(num1, num2)) # 필요한 상황에 특정 에러를 발생시키기. 아래 except 의 에러로 이어진다.
#     print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
# except ValueError:
#     print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
# except BigNumberError as err:
#     print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요.")
#     print(err)


### finally
    # 예외처리 구문에서 정상적이건 오류건 무조건 실행되는 구문
# class BigNumberError(Exception): # 두 자리 숫자가 입력되었을 때의 에러를 만듦
#     # pass
#     def __init__(self, msg): # 에러에서 보여줄 메세지 정의
#         self.msg = msg

#     def __str__(self): # 에러에서 보여줄 메세지 정의
#         return self.msg
# try:
#     print("한 자리 숫자 나누기 전용 계산기입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요 : "))
#     num2 = int(input("두 번째 숫자를 입력하세요 : "))
#     if num1 >= 10 or num2 >= 10:
#         raise BigNumberError("입력값 : {0}, {1}".format(num1, num2)) # 필요한 상황에 특정 에러를 발생시키기. 아래 except 의 에러로 이어진다.
#     print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
# except ValueError:
#     print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
# except BigNumberError as err:
#     print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요.")
#     print(err)
# finally:
#     print("계산기를 이용해 주셔서 감사합니다.") # 무조건 출력되는 메세지


##### Quiz ) 동네의 치킨집에는 항상 대기 손님이 있습니다.
# 대기 손님의 치킨 요리 시간을 줄이고자 자동 주문 시스템을 제작하였습니다.
# 시스템 코드를 확인하고 적절한 예외처리 구문을 넣으시오.

# 조건1 : 1보다 작거나 숫자가 아닌 입력값이 들어올 때는 ValueError 로 처리
#     출력 메세지 : "잘못된 값을 입력하였습니다."
# 조건2 : 대기 손님이 주문할 수 있는 총 치킨량은 10마리로 한정
#     치킨 소진 시 사용자 정의 에러(SoldOutError)를 발생시키고 프로그램 종료
#     출력 메세지 : "재고가 소진되어 더 이상 주문을 받지 않습니다."

# [기본 코드]
# chicken = 10
# waiting = 1 # 홀은 현재 만석. 대기번호 1부터 시작.
# while(True):
#     print("[남은 치킨 : {0}]".format(chicken))
#     order = int(input("치킨 몇 마리 주문하시겠습니까?"))
#     if order > chicken: # 남은 치킨보다 주문량이 많을 때
#         print("재료가 부족합니다.")
#     else:
#         print("[대기번호 {0}] {1} 마리 주문이 완료되었습니다.")\
#             .format(waiting, order)
#         waiting += 1
#         chicken -= order

# chicken = 10
# waiting = 1 # 홀은 현재 만석. 대기번호 1부터 시작.

# class SoldOutError(Exception):
#     pass

# while(True):
#     try:
#         print("[남은 치킨 : {0}]".format(chicken))
#         order = int(input("치킨 몇 마리 주문하시겠습니까?"))
#         if order > chicken: # 남은 치킨보다 주문량이 많을 때
#             print("재료가 부족합니다.")
#         elif order <= 0: # 1보다 작은 숫자가 들어올 때 에러처리. 숫자가 아닌 값은 자동으로 ValueError 처리된다.
#             raise ValueError
#         else:
#             print("[대기번호 {0}] {1} 마리 주문이 완료되었습니다."\
#                 .format(waiting, order))
#             waiting += 1
#             chicken -= order
#         if chicken == 0:
#             raise SoldOutError
            
#     except ValueError:
#         print("잘못된 값을 입력하였습니다.")
#     except SoldOutError:
#         print("재고가 소진되어 더 이상 주문을 받지 않습니다.")
#         break


### 모듈
    # 필요한 것들끼리 부품처럼 만드는 것 = 모듈화
    # 함수 정의나 클래스 등의 파이썬 문장을 담고 있는 것 = 모듈
    # 확장자 : .py
import theater_module
theater_module.price(3) # 3명이서 영화 보러 갔을 때 가격
theater_module.price_morning(4) # 4명 조조영화 가격 # 24000원
theater_module.price_soldier(5) # 군인 5명 영화 가격 # 20000원

import theater_module as mv # 별명으로 부르는 이름 단축
mv.price(3)
mv.price_morning(4)
mv.price_soldier(5)

from theater_module import *
price(3)
price_morning(4)
price_soldier(5)

from theater_module import price, price_morning # 군인 함수 제외
price(5)
price_morning(6)
price_soldier(7) # 오류 발생. 지금은 위에 여러번 import해서 불러올 수 있음.

from theater_module import price_soldier as price
price(1) # 다른 함수의 이름과 같은 별명으로 지어서 사용가능


### 패키지
    # 모듈을 모아놓은 집합
import travel.thailand # 모듈이나 패키지만 import 할 수 있음
    # travel.thailand.ThailandPackage 가 불가능
    # from travel.thailand import ThailandPackage 와 같은 방법은 사용가능
trip_to = travel.thailand.ThailandPackage()
trip_to.detail() # ThailandPackage 클래스의 detail 함수 호출됨

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()


### __all__
from travel import *
trip_to = vietnam.VietnamPackage() # 모든 것을 import 하겠다고 했지만, vietnam이 정의되지 않았다고 오류발생
    # *로 모든 모듈을 불러오겠다고 했지만, 개발자가 문법 상에서 공개 범위를 설정해줘야 함 => travel 폴더의 __init__.py 설정 필요
    # __init__.py에 __all__ = ["vietnam"] 를 입력함으로써 오류없이 호출 가능!
trip_to.detail()
trip_to = thailand.ThailandPackage()
trip_to.detail()


### 모듈 직접 실행
    # thailand.py에서 if문을 활용해서 모듈 내부에서 실행하는 것인지 외부에서 실행하는 것인지 구분할 수 있다.


### 패키지, 모듈 위치
import inspect
import random
print(inspect.getfile(random)) # random 파일의 위치 출력됨
print(inspect.getfile(thailand))
    # random 파일의 위치에 우리가 자주 사용하는 폴더를 넣어놓으면 다른 프로젝트에서도 바로 사용할 수 있다!


### pip install
    # 패키지 설치 방법
    # 구글에 pypi 검색 - pypi.org 페이지 - browse projects 에서 필요한 패키지 찾아 볼 수 있음.
    # 웹 스크래핑을 위한 beautifulsoup 검색 - beautifulsoup4 4.11.1 - 명령어, 설명, 예제를 볼 수 있음.

    # beautifulsoup 사용
    # 1. vsc terminal에 실행 명령어 입력(pip install beautifulsoup4)
    # 2. 예제 코드 복사
from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())


### 내장함수
    # import 필요없이 바로 사용 가능한 함수
    # input
# language = input("무슨 언어를 좋아하세요?")
# print("{0}은 아주 좋은 언어입니다!".format(language))

    #dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
import random # 외장함수
print(dir()) # random이 추가됨
import pickle
print(dir()) # pickle 추가됨. but 지금은 위에서 부터 계속 이어적어와서 여기서 import 하기 전에도 random이나 pickle이 존재함

print(dir(random)) # random 모듈 내에서 쓸 수 있는 것들을 보여줌

lst = [1, 2, 3]
print(dir(lst)) # list에서 사용할 수 있는 것들

name = "Jim"
print(dir(name)) # name에 대해 사용할 수 있는 것들


### 외장함수
    # import해서 사용하는 함수

    # glob : 경로 내의 폴더/파일 목록 조회
import glob
print(glob.glob("*.py")) # PythonWorkspace에서 확장자 py인 모든 파일

    # os : 운영체제에서 제공하는 기본 기능
import os
print(os.getcwd()) # 현재 디렉토리 표시

# folder = "sample_dir"
# if os.path.exists(folder): # folder가 있으면
#     print("이미 존재하는 폴더입니다.")
#     os.rmdir(folder) # rmdir : 폴더 삭제
#     print(folder, "폴더를 삭제하였습니다.")
# else:
#     os.makedirs(folder) # makedirs : folder 생성
#     print(folder, "폴더를 생성하였습니다.")

print(os.listdir()) # glob과 비슷

    # time : 시간 관련
import time
print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S")) # strftime : 시간 포맷 변경

    # datetime
import datetime
print("오늘 날짜는 ", datetime.date.today())

today = datetime.date.today() # 오늘 날짜 저장
td = datetime.timedelta(days=100) # timedelta : 두 날짜 사이의 간격
print("우리가 만난지 100일은", today + td)


##### Quiz ) 프로젝트 내에 나만의 시그니처를 남기는 모듈을 만드시오
# 조건 : 모듈 파일명은 byme.py
# (모듈 사용 예제)
# import byme
# byme.sign()

# (출력 예제)
# 이 프로그램은 유영준에 의해 만들어졌습니다.
# 이메일 : dudwns0311@naver.com

# create_byme = open("byme.py", "w", encoding="utf8")
# create_byme.write("print('이 프로그램은 유영준에 의해 만들어졌습니다.')\n")
# create_byme.write("print('이메일 : dudwns0311@naver.com')")
# create_byme.close()

import byme
byme.sign()