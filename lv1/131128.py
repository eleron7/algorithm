# 숫자 짝꿍
# https://school.programmers.co.kr/learn/courses/30/lessons/131128?language=python3

def solution(X, Y):
    answer = ''
    pair = []
    check = [0] * 10#0~9까시 숫자가 등장한 횟수를 담는 배열
    zero = 0#0의 등장 횟수를 체크하는 배열
    
    for n in X:
        check[int(n)] += 1
    
    for n in Y:
        if check[int(n)] != 0:
            pair.append(int(n))
            check[int(n)] -= 1
            if int(n) == 0:
                zero += 1
    
    if not pair:#짝이 존재하지 않는경우
        return '-1'
    elif zero == len(pair):#짝이 0으로만 구성된 경우
        return '0'
    
    pair.sort(reverse = True)#내림차순 정렬

    for n in pair:
        answer += str(n)
    
    return answer