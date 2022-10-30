# 정규식 : re(Regular Expression)

import re

p = re.compile("ca.e") 
# . (ca.e) : 하나의 문자. care, cafe, case, cave 가능 / caffe 불가능
# ^ (^de) : 문자열의 시작. desk, destiantion 가능 / fade 불가능
# $ (se$) : 문자열의 끝. case, base 가능 / face 불가능

m = p.match("case")
print(m.group()) # case. 위의 p와 case 매치가 돼서 출력됨
# t = p.match("caffe")
# print(t.group()) # 에러

def print_match(a):
    if a:
        print("a.group()", a.group()) # 일치하는 문자열 반환
        print("a.string", a.string) # 입력받은 문자열
        print("a.start()", a.start()) # 일치하는 문자열의 시작점 index
        print("a.end()", a.end()) # 일치하는 문자열의 끝 index
        print("a.span()", a.span()) # 일치하는 문자열의 시작과 끝 index 모두
    else:
        print("매칭되지 않음")

# a = p.match("good care")
# print_match(a) # 매칭되지 않음

# a = p.match("careless")
# print_match(a) # care => 주어진 문자열의 앞부터 일치하는지 확인하기 때문에 매치 성공함

a = p.search("good care") # search : 주어진 문자열 중에 일치하는게 있는지 확인
print_match(a) # care
m = p.search("careless")
print_match(m) # care

lst = p.findall("careless") # findall : 일치하는 모든 것을 리스트 형태로 반환
print(lst) # ['care']
lst = p.findall("good care cafe")
print(lst) # ['care', 'cafe']

# python re docs / w3school 참고