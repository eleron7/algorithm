# 부족한 금액 계산하기
# https://school.programmers.co.kr/learn/courses/30/lessons/82612?language=python3
def solution(price, money, count):
    # 1번 탈때마다 요금이 count * money 만큼 비싸짐(count는 매번 1씩 증가)
    # (1 * money) + (2 * money) + (3 * money) + ... (count * money)
    # money * (1 + 2 + 3 ... + count) 
    # 1부터 n까지 합 n*(n + 1) / 2 ''
    answer = money - (price * (count + 1) * count // 2)
    if answer >= 0:
        return 0
    else:
        return -answer