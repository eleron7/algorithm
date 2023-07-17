# 과일 장수
# https://school.programmers.co.kr/learn/courses/30/lessons/135808?language=python3

def solution(k, m, score):
    answer = 0
    
    score = sorted(score, reverse = True) #정렬
    num = len(score) #사과 개수
    boxNum = num // m #사과 박스 개수
    
    cnt = 0
    idx = -1
    
    while cnt != boxNum:
        idx += m
        answer = answer + (score[idx]*m) #최저 사과 점수 * 한 상자에 담긴 사과 개수 
        cnt += 1
        
    return answer