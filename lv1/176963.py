#추억 점수
#https://school.programmers.co.kr/learn/courses/30/lessons/176963
def solution(name, yearning, photos):
    answer = []
    
    #여려 사진들 중 한 장
    for photo in photos:
        #해당 사진의 그리움 점수
        yearningScore = 0
        
        #여려 사람들 중 한 명
        for who in photo:
            #name or yearning 리스트 안에 있을 때
            if who in name:
                i = name.index(who)
                yearningScore += yearning[i]
        
        #각 사진에 대한 그리움 합을 저장
        answer.append(yearningScore)
    
    return answer