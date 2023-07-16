# 개인정보 수집 유효기간
# https://school.programmers.co.kr/learn/courses/30/lessons/150370?language=python3

def solution(today, terms, privacies):
    answer = []
    today = today.replace('.', '')
    termsSet = {}
    
    for term in terms:
        type, month = term.split(' ')
        termsSet[type] = int(month)
    
    for idx, privacie in enumerate(privacies):
        startDate, term = privacie.split(' ')
        year, month, day = startDate.split('.')
        year = int(year)
        month = int(month)
        day = int(day)

        if (month + termsSet[term]) > 12:#현재 월 + 유효기간이 12 넘는 경우
            if (month + termsSet[term]) % 12 == 0:#나누어 떨어지는 경우
                year += (((month + termsSet[term])//12) - 1)#마지막으로 나누어지는 월은 남겨야하기 때문에 - 1
                month = 12#마지막으로 나누어지는 월을 실제 월로 표시
            else:#나누어 떨어지지 않는 경우
                year += ((month + termsSet[term])//12) 
                month = (month + termsSet[term]) % 12
        else:#넘지 않는 경우
            month = month + termsSet[term]
        
        if day == 1:
            day = 28
            month -= 1
        else:
            day -= 1

        if int(str(year) + str(month).zfill(2) + str(day).zfill(2)) < int(today):
            answer.append(idx + 1)#만료
            
    return answer