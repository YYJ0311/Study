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
from tkinter import Misc # 파이썬에서 제공하는 math 라이브러리 사용
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
