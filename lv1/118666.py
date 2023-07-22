# 성격 유형 검사하기
# https://school.programmers.co.kr/learn/courses/30/lessons/118666?language=python3

def solution(survey, choices):
    answer = ''
    n = len(survey)
    
    charactor = [0] * 4
    chScore = [3, 2, 1, 0, -1, -2, -3]#is R, C, J, A
    chScoreReverse = [-3, -2, -1, 0, 1, 2, 3]#is T, F, M, N
    
    #survey 출력 순서 : RT 0, CF 1, JM 2, AN 3
    surveyBase = ['RT', 'CF', 'JM', 'AN']
    surveyList = {'RT': 0, 'CF': 1, 'JM': 2, 'AN': 3}
    surveyListReverse = {'TR': 0, 'FC': 1, 'MJ': 2, 'NA': 3}#반대의 경우
    
    for i in range(n):
        s = survey[i]
        c = choices[i] - 1
        if s in surveyList:
            charactor[surveyList[s]] += chScore[c]
        elif s in surveyListReverse:
            charactor[surveyListReverse[s]] += chScoreReverse[c]
    
    for i, c in enumerate(charactor):
        if c >= 0:
            answer += surveyBase[i][0]
        else:
            answer += surveyBase[i][1]
    
    return answer