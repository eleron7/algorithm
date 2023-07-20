# 햄버거 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/133502?language=python3

def solution(ingredient):
    answer = 0
    
    hambuger = [1, 2, 3, 1]
    hambugerStack = []
    
    for i in ingredient:
        hambugerStack.append(i)
        if hambuger == hambugerStack[-4:]:#끝에서부터 4개 확인
            answer += 1
            for i in range(4):#햄버거 재료개수(4번) 만큼 pop 
                hambugerStack.pop()
            
    return answer