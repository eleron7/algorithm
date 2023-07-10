# 덧칠하기
# https://school.programmers.co.kr/learn/courses/30/lessons/161989
def solution(n, m, section):
    answer = 0
    idx = 0
    
    #내림차순 정렬
    section.sort()
    
    while idx < len(section):
        start = section[idx]#페인트를 칠하는 시작 점
        end = start + m - 1#페인트를 칠하는 끝 점
        for i in range(idx, len(section)):#현재 위치부터 남은 칠해야하는 영역 만큼 반복
            if section[i] <= end:#롤러로 칠했을 때 뒷 영역 까지 칠해졌다면 그 영역의 인덱스 스킵 
                idx += 1
            else:#아니라면 반목문 탈출
                break
        answer += 1
        
        
    return answer