# 문자열 나누기
# https://school.programmers.co.kr/learn/courses/30/lessons/140108?language=python3

def solution(s):
    answer = 0

    first = '' #시작문자
    same = 0 #시작문자와 동일한 문자 개수
    diff = 0 #시작문자와 다른 문자 개수
    for i, ch in enumerate(s):
        if first == '' or same == diff:# ''이거나 same과 diff의 개수가 같을 때 문자 초기화
            first = ch
            same = 1
            diff = 0
            answer += 1 # 분해 카운트
        else:
            if first == ch:
                same += 1    
            else:
                diff += 1

    return answer