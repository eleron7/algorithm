# 연속된 부분 수열의 합
# https://school.programmers.co.kr/learn/courses/30/lessons/178870

def solution(sequence, k):
    length = len(sequence)
    
    start = 1
    end = 1
    res = []#합이 k가 나오는 부분수열(start, end)인덱스들을 담는 배열
    
    #누적합 배열이 들어갈 공간 (target 배열 길이 + 1) 
    prefixSum = [0] * (length + 1)
    
    #누적합 배열을 만드는 과정
    for i in range(1, length + 1):
        prefixSum[i] = prefixSum[i - 1] + sequence[i - 1]
    
    while start <= end < length + 1:
        start2endSum = prefixSum[end] - prefixSum[start - 1]#start 부터 end 까지의 합
        
        if start2endSum < k:#작을 경우
            end += 1

        elif start2endSum == k:#찾을 경우
            res.append([start, end])
            end += 1
        
        else:#클 경우
            start += 1
        
    #문제가 원하는 조건대로 우선순위를 정함
    res = sorted(res, key = lambda x : (x[1]-x[0], x[0]))[0]
    
    #prefixSum index 이기 때문에 한칸 씩 줄여야 함 
    return [res[0] - 1, res[1]  - 1]