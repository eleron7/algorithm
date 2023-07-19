# 푸드 파이트 대회
# https://school.programmers.co.kr/learn/courses/30/lessons/134240?language=python3

def solution(food):
    answer = ''
    
    for i in range(1, len(food)):
        for _ in range(int(food[i]) // 2):
            answer += str(i)
            
    return answer + '0' + answer[:: -1]