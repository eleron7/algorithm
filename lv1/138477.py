# 명예의 전당 (1)
# https://school.programmers.co.kr/learn/courses/30/lessons/138477?language=python3

def solution(k, score):
    answer = []
    
    set = []
    
    for s in score:
        set.append(s)
        set = sorted(set, reverse = True)#내림차순 정렬
        if len(set) < k:#전체 개수가 k보다 작을 때 길이-1 번째 인덱스 값을 입력
            answer.append(set[len(set) - 1])
        else:#k-1 번째 인덱스 값을 입력
            answer.append(set[k-1])
        
    return answer