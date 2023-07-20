# 옹알이 (2)
# https://school.programmers.co.kr/learn/courses/30/lessons/133499?language=python3

def solution(babbling):
    answer = 0

    for b in babbling:
        if go(b, '', ''):
            answer += 1
    return answer

def go(b, current, pre):
    if len(b) <= len(current):#종료 재귀문 조건
        if b == current: 
            return True        
        return False

    for word in ["aya", "ye", "woo", "ma"]:
        if pre != word:#이전 발음과 같은게 연속되지 않는다면
            if go(b, current + word, word):
                return True
    return False
            