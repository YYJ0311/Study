# 숫자형
print(5)
print(-10)
print(3.14)
print(2*8) # 16
print(2**3) # 2^3 = 8
print(5%3) # 2 (나머지)
print(5//3) # 1 (몫)

# 문자열 자료형
print('풍선')
print("나비")
print("ㅎ"*5) # ㅎㅎㅎㅎㅎ

# 참/거짓 판단 Boolean형
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

# 변수
animal = "강아지"
age = 4
is_old = age > 3
print(animal+"는"+str(age)+"살 입니다.")
print(animal+" 나이가 많은가요?"+str(is_old))

# 숫자처리 함수
print(abs(-5)) # 절대값 5
print(pow(4, 2)) # 4^2 = 16
print(max(5, 12)) # 최대값 12
print(round(3.14)) # 반올림 3

from math import * # 파이썬에서 제공하는 math 라이브러리 사용
print(floor(4.99)) # 내림 4
print(ceil(3.14)) # 올림 4
print(sqrt(16)) # 제곱근 4

# 랜덤함수 
from random import *
print(random()) # 0.0 ~ 1.0 임의의 값 생성
print(random() * 10) # 0.0 ~ 10.0 임의의 값
print(int(random() * 10)) # 0 ~ 10
print(int(random() * 10) + 1) # 1 ~ 10

# 로또 수 뽑기
print(int(random() * 45) + 1) # 1 ~ 45
print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성
print(randint(1, 45)) # 1 ~ 45 이하

# Quiz) 코딩 스터디 모임을 새로 만들었습니다.
# 월 4회 스터디를 하는데 3번은 온라인으로 하고 1번은 오프라인으로 하기로 했습니다.
# 아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오.
# 조건
#     1. 랜덤으로 날짜를 뽑아야 함
#     2. 월별 날짜는 다름을 감안하여 최소 일수인 28 이내로 정함
#     3. 매월 1~3일은 스터디 준비를 해야하므로 제외
from random import *
날짜 = randint(4,28)
print("오프라인 스터디 모임 날짜는 매월 "+str(날짜)+"일로 선정되었습니다.")

# 문자열
sentence = '나는 나비'
print(sentence)
sentence2 = """
나는 나비
너는 나방
"""
print(sentence2) # """은 줄바꿈도 포함해서 출력한다.

# 슬라이싱
jumin = "990110-1234567"
print("성별 : " + jumin[7]) # index는 0부터 시작
print("연 : " + jumin[0:2]) # 0번째 부터 2번째 직전(1번째 까지)
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])
print("생년월일 : " + jumin[:6]) # 처음부터 6번째 직전까지
print("뒤 7자리 : " + jumin[7:]) # 7번째부터 끝까지
print("뒤 7자리(뒤에서부터) : " + jumin[-7:]) # 맨 뒤에서 7번째부터 끝까지

# 문자열 처리 함수
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

# 문자열 포맷
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
print(f"나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color="빨간")) #문장을 f로 시작

# 탈출문자
