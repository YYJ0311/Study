# 공과 무기가 충돌했을 때 문제 발생
    # 1. 큰 공이 없어지지 않고 그대로 남아있음
    # 2. 큰 공이 나뉘어서 생겨야 할 공 2개 중 1개가 충돌처리로 지워짐

# 기존 코드 진행방식
# balls = [1, 2, 3, 4]
# weapons = [11, 22, 3, 44]
# for ball_idx, ball_val in enumerate(balls):
#     print("ball", ball_val)
#     for weapon_idx, weapon_val in enumerate(weapons):
#         print("weapons :", weapon_val)
#         if ball_val == weapon_val:
#             print("공과 무기가 충돌")
#             break
#             # ball이 3일 때 weapon for문이 멈추길 의도 했지만 
#             # 두번째 for문만 break되고 밖의 for문으로 돌아가서 ball이 4인 경우가 실행됨
#             # => 오류발생

balls = [1, 2, 3, 4]
weapons = [11, 22, 3, 44]
for ball_idx, ball_val in enumerate(balls):
    print("ball", ball_val)
    for weapon_idx, weapon_val in enumerate(weapons):
        print("weapons :", weapon_val)
        if ball_val == weapon_val:
            print("공과 무기가 충돌")
            break # for/else를 모두 좋료하고 바깥으로 나감 => 아래 break로 연결됨
    else: # for에서 순회할 값이 없다면 else로 들어옴
        continue # 안쪽 for문을 다 돌면 여기로 연결돼서 바깥 for문으로 올라간다.
    break # 안쪽 for문의 break와 연결된다.