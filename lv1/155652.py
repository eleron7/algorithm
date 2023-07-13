# 둘만의 암호
# https://school.programmers.co.kr/learn/courses/30/lessons/155652?language=python3

def solution(s, skip, index):
    answer = ''
    word = list(s)#문자열을 리스트로 변환

    for i in range(len(word)):
        j = 0#점프한 횟수
        find = 0#스킵 문자를 찾은 횟수
        
        while j - find < index:#점프 횟수 + 스킵 횟수가 이동 인덱스보다 크거나 같을 때까지 반복
            if ord('z') < ord(word[i]) + 1:#문자 z보다 뒤로 점프했다면 a로 이동
                word[i] = 'a'
            else:
                word[i] = chr(ord(word[i]) + 1)
            
            j += 1#점프 카운트
            
            if word[i] in skip:#skip에 있는 문자를 찾은 경우
                find += 1
        
        answer += word[i]#결과를 정담 문자열에 더함
    return answer