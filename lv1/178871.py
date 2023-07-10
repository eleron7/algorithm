# 달리기 경주
# https://school.programmers.co.kr/learn/courses/30/lessons/178871
def solution(players, callings):
    answer = []
    
    i = 0
    
    playerSetKV = {}
    playerSetVK = {}
    
    # KV와 VK 딕셔너리를 players 리스트 순서대로 초기화
    for player in players:
        playerSetKV[player] = i
        playerSetVK[i] = player
        i += 1

    for calling in callings:
        #앞지르는 선수(player1)의 value(등수)
        player1V = playerSetKV.get(calling)
        #앞질러지는 선수(player2)의 key(이름)
        player1K = calling

        #앞질러지는 선수(player2)의 value(등수)
        player2V = player1V - 1
        #앞질러지는 선수(player2)의 key(이름)
        player2K = playerSetVK.get(player2V)

        #순위 바꾸기
        playerSetKV[player1K], playerSetKV[player2K] = player2V, player1V
        playerSetVK[player1V], playerSetVK[player2V] = player2K, player1K
    
    for item in sorted(playerSetKV.items(), key = lambda x : x[1]):
        answer.append(item[0])

    return answer