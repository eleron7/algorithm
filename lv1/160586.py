# 대충 만든 자판
# https://school.programmers.co.kr/learn/courses/30/lessons/160586
def solution(keymap, targets):
    answer = []
    
    for target in targets:
        sum = 0#해당 문자열을 입력하기 위해 필요한 최소 누름 횟수
        for t in target:
            minVal = 1e9#해당 문자를 입력하기 위해 필요한 최소 누름 횟수
            complete = False#완성가능한 문자열인지 판별하는 변수
            for key in keymap:
                if t in key:
                    complete = True#keymap 안에 들어있다면 완성가능
                    minVal = min(list(key).index(t)+1, minVal)
            sum += minVal
            
            if not complete:#문자열을 완성할 수 있는 문자를 찾지 못했다면
                sum = -1#-1을 반환하고 종료
                break
                
        answer.append(sum)
    return answer