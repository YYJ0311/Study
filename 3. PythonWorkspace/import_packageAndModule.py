# from ~ import *: 모듈 import
# import ~ : 패키지 import
# 패키지 = 모듈을 모아놓은 집합

# 사용 예시
from random import *
print(randint(1,6))

import random
print(random.randint(1,6))

# random 패키지 자체를 import하면 randint 함수에 대해서 random으로 접근해야 한다.
# randome의 모듈을 import하면 random 접근 필요 없이 바로 randint 함수 사용이 가능하다.