# 가장 가까운 같은 글자
# https://school.programmers.co.kr/learn/courses/30/lessons/142086?language=python3

def solution(s):
    answer = []
    alphabetIndex = [-1] * 27#가장 최근에 등장했던 문자의 인덱스를 저장하는 배열
    
    for i, a in enumerate(s):
        idx = ord(a) - 97
        if alphabetIndex[idx] == -1:#해당 문자가 처음 등장 했을 때
            answer.append(alphabetIndex[idx])    
        else:
            answer.append(i - alphabetIndex[idx])#이전 등장했던 인덱스와 현재 인덱스와의 차
        
        alphabetIndex[idx] = i#인덱스 갱신
            
    return answer