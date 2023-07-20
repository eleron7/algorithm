# 푸드 파이트 대회
# https://school.programmers.co.kr/learn/courses/30/lessons/134240?language=python3

def solution(food):
    answer = ''
    
    for i in range(1, len(food)):
        for _ in range(int(food[i]) // 2):#양쪽 선수 모두 먹을 수 있어야 하기 때문에 해당 음식 수 // 2 만큼 각 선수는 먹을 수 있음
            answer += str(i)
            
    return answer + '0' + answer[:: -1]