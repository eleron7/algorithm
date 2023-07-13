# 카드 뭉치
# https://school.programmers.co.kr/learn/courses/30/lessons/159994

# 두 카드 뭉치들로 목표 카드 뭉치를 만들 수 있는지 체크하는 함수
def checkPossible(cards1, cards2, goal, idx1, idx2, make):
    if len(make) == len(goal):# 목표 카드뭉치와 장수가 동일하다면
        if make == goal:# 목표 카드뭉치와 같을 때
            return True
        else:# 목표 카드뭉치와 다를 때
            return False
        
    else:# 목표 카드뭉치와 장수가 동일하지 않다면 카드를 더 채움
        if idx1 < len(cards1):# 카드뭉치1 인덱스 범위 안이라면
            # 해당 인덱스의 카드를 카드뭉치에 추가하는 경우의 수 중 목표 카드뭉치를 완성할 수 있는 경우의 수가 있다면
            if (checkPossible(cards1, cards2, goal, idx1 + 1, idx2, make + [cards1[idx1]])):
                return True

        if idx2 < len(cards2):# 카드뭉치2 인덱스 범위 안이라면
            # 해당 인덱스의 카드를 카드뭉치에 추가하는 경우의 수 중 목표 카드뭉치를 완성할 수 있는 경우의 수가 있다면
            if (checkPossible(cards1, cards2, goal, idx1, idx2 + 1, make + [cards2[idx2]])):
                return True

        return False

def solution(cards1, cards2, goal):
    answer = 'Yes' if checkPossible(cards1, cards2, goal, 0, 0, []) else 'No'
    return answer