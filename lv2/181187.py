# 두 원 사이의 정수 쌍
# https://school.programmers.co.kr/learn/courses/30/lessons/181187?language=python3
from math import floor, ceil

def solution(r1, r2):
    answer = 0

    # 피타고라스 정리를 이용하여 하나의 x좌표에서 발생할 수 있는 y의 개수를 구함
    # r2 또는 r1이 c라고 할 때 a^2 + b^2 = c^2
    # c^2 - a^2 를 통해 b(y)를 구할 수 있음
    # y의 최소값과 y의 최대값을 구하고 그것을 정수로 변환했을 때 차가 해댱 x좌표의 y의 개수
    for x in range(1, r2 + 1):
        max_y = floor((r2**2 - x**2)**(1/2))
        min_y = ceil((r1**2 - x**2)**(1/2)) if x < r1 else 0
        
        answer += (max_y - min_y + 1)
    
    #하나의 사분면에 대해서만 구했기 때문에 * 4
    answer *= 4
        
    return answer