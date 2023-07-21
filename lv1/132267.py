# 콜라 문제
# https://school.programmers.co.kr/learn/courses/30/lessons/132267?language=python3

def solution(a, b, n):
    answer = 0
    bottle = n#현재 빈 병
    
    while True:
        recive = b*(bottle//a)#빈병으로 받은 콜라 개수
        answer += recive
        bottle = recive + (bottle%a)#받은 콜라를 다 마시면 다시 빈병 + 콜라로 바꾸지 못한 빈병
        if bottle < a:#남은 빈병으로 더 이상 교환할 수 없다면 종료
            break
    
    return answer