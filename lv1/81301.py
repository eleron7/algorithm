# 숫자 문자열과 영단어
# https://school.programmers.co.kr/learn/courses/30/lessons/81301?language=python3

def solution(s):
    answer = ''
    
    i = 0#현재 인덱스
    while i < len(s):#영단어를 찾았다면 숫자에 매칭되는 영단어의 글자 수 만큼 건너 뜀, 숫자를 찾는다면 1만큼 건너뜀
        if s[i] == 'z':
            answer += '0'
            i += 4
        elif s[i] == 'o':
            answer += '1'
            i += 3
        elif s[i] == 't':
            if s[i+1] == 'w':
                answer += '2'
                i += 3
            else:
                answer += '3'
                i += 5
        elif s[i] == 'f':
            if s[i+1] == 'o':
                answer += '4'
                i += 4
            else:
                answer += '5'
                i += 4
        elif s[i] == 's':
            if s[i+1] == 'i':
                answer += '6'
                i += 3
            else:
                answer += '7'
                i += 5
        elif s[i] == 'e':
            answer += '8'
            i += 5
        elif s[i] == 'n':
            answer += '9'
            i += 4
        else:
            answer += s[i]
            i += 1
        
    return int(answer)