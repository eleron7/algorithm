# 바탕화면 정리
# https://school.programmers.co.kr/learn/courses/30/lessons/161990
def solution(wallpaper):
    answer = []
    
    min_x, min_y = 1e9, 1e9#드래그 시작점(최소 좌표)
    max_x, max_y = 0, 0#드래그 끝점(최대 좌표)
    
    row = len(wallpaper[0])
    col = len(wallpaper)
    
    for c in range(col):
        for r in range(row):
            if wallpaper[c][r] == "#":
                min_x = min(min_x, r)
                min_y = min(min_y, c)
                max_x = max(max_x, r)
                max_y = max(max_y, c)

    answer = [min_y, min_x, max_y+1, max_x+1]
    
    return answer