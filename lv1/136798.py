# 기사단원의 무기
# https://school.programmers.co.kr/learn/courses/30/lessons/136798?language=python3

def solution(number, limit, power):
    answer = 0
    
    def cntMeasure(n):
        cnt = 0
        for i in range(1, int(n ** (1/2)) + 1):#제곱근 까지만 반복
            if n % i == 0:
                cnt += 1
                if (i**2) != n:#제곱과 같은경우는 수가 중복되기 때문에 아닌경우만 +1 더 해줌
                    cnt += 1
        
        if cnt > limit:
            return power
        return cnt
    
    
    for n in range(1, number + 1):
        k = cntMeasure(n)
        answer += k
    
    return answer 