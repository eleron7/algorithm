# 3진법 뒤집기
# https://school.programmers.co.kr/learn/courses/30/lessons/68935?language=python3
def solution(n):
    answer = 0
    log = []
    
    while n > 0:
        log.append(str(n % 3))#아랫자리 부터 들어가서 반전을 할 필요 없음
        n = n // 3
    
    temp =''.join(log)
    l = len(temp)
    for i, t in enumerate(temp):
        answer += (int(t) * 3 ** (l - i - 1))#3진법을 다시 10진법으로
    return answer