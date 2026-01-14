# M = 필요한 나무 길이
# H = 자를 나무의 높이
# N = 나무의 수
# 최소 중 최대

# 나무의 수 N / 나무의 길이 M
# 나무의 높이들 ~

# 가져가는 나무의 길이 = (나무높이 - H) or 0 -> 의 합
# 일단 반절 자르고 가져갈 수 있는 총합 찾고 
# 그 값이 M을 충족하면? 더 높은 높이도 가능한지 left를 올린다. (최소로 자를 거니까)
# 그 값이 M을 충족하지 못하면? 높이를 낮춰서 확인 right를 낮춘다.

import sys

def solution():
    input = sys.stdin.readline
    answer = 0

    # 1. 입력값 파싱
    N, M = map(int, input().split())
    trees = list(map(int, input().split()))

    # 2. 높이의 범위 정하기
    left = 0
    right = max(trees)

    while left <= right:
        mid = (left + right) // 2 # 후보
        total = 0 # 최종 가져갈 나무의 길이

        # 현재 높이인 mid로 잘랐을 때 가져갈 수 있는 나무의 길이를 구한다
        for height in trees:
            if height > mid:
                total += height - mid

        # 그렇게 total 구한 다음에 M에 만족하는지 안 하는지 비교
        if total >= M: # 충족하면 더 높이 잘라도 되는지 left up
            answer = mid
            left = mid + 1
        
        else: # 충족하지 않으면 나무가 부족하므로 낮게 right down
            right = mid - 1

    print(answer)
    return answer

solution()
