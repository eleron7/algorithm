# 공원 산책
# https://school.programmers.co.kr/learn/courses/30/lessons/172928

def solution(park, routes):
    answer = []
    current = None
    
    #공원의 세로 가로 최대 길이
    max_height = len(park)
    max_width = len(park[0])

    dInfo = ["S", "N", "E", "W"]
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1 , -1]

    for i, row in enumerate(park):
        for j, value in enumerate(row):
            if value == 'S':#시작 점 좌표를 찾아서 추가
                current = [i, j]
                break
        
    for route in routes:
        #시작점의 세로좌표, 가로 좌표
        x, y = current
        direction, dist = route.split(" ")
        didx = dInfo.index(direction)

        #이동할 좌표
        nx, ny = x + int(dist)*dx[didx], y + int(dist)*dy[didx]

        #이동가능한 위치인가?
        if 0 <= nx < max_height and 0 <= ny < max_width:
            #경로에 장애물이 있는가?
            if (x != nx and "X" in [park[i][ny] for i in range(min(x, nx), max(x, nx)+1)]) or (y != ny and "X" in park[nx][min(y, ny):max(y, ny)+1]):
                None
            else:   
                current = [nx, ny]
            
    answer = current
    
    return answer
