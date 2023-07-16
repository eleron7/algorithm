# 크기가 작은 부분문자열
# https://school.programmers.co.kr/learn/courses/30/lessons/147355?language=python3

def solution(t, p):
    answer = 0
    numLen = len(p)#p의 길이
    
    for i in range(len(t) - numLen + 1):#t에서 p의 길이만큼의 부분문자열을 (t-p+1) 개가 발생할 수 있음
        if t[i:i+numLen] <= p:#슬라이싱으로 만든 부분 문자열과 p를 비교했을때 작거나 같아면 
            answer += 1#그 수를 셈

    return answer