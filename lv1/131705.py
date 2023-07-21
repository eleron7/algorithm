# 삼총사
# https://school.programmers.co.kr/learn/courses/30/lessons/131705?language=python3

answer = 0
def solution(number):
    global answer
    go([], 0, number)
    
    return answer

def go(trio, idx, number):
    global answer
    if len(trio) == 3 or idx >= len(number):
        if sum(trio) == 0 and len(trio) == 3:
            answer += 1
        return
    go(trio, idx + 1, number)#추가하는 경우
    go(trio + [number[idx]], idx + 1, number)#추가하지 않는 경우