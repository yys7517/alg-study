# 최단 이동 횟수이므로 bfs
# 1. 파싱 - 테케 개수 /// 첫째 줄(한 변의 길이) / 둘째 줄(현재 칸) / 셋째 줄(이동하려는 칸)
# 2. 체스판 정의
# 3. 나이트 이동 정의
# 4. bfs 큐 생성 & 구현

import sys
from collections import deque

# 입력
input = sys.stdin.readline

# 나이트 이동 방향 (8개)
moves = [
    (-2, -1), (-2, 1),
    (-1, -2), (-1, 2),
    (1, -2), (1, 2),
    (2, -1), (2, 1),
]

def chess(input):
    # 파싱
    # 테스트 케이스 개수 t
    # 테케 결과 저장 result
    t = int(input().strip())
    results = []

    for _ in range(t):
        length = int(input().strip())
        start_x, start_y = map(int, input().split())
        target_x, target_y = map(int, input().split())

        # 시작 지점과 목표 지점이 같은 경우
        if start_x == target_x and start_y == target_y:
            results.append(0) # 이동 횟수 0

        # 방문 여부, 거리 저장
        # 체스판 만들기 (length x length 만큼) 방문 안 했다고 가정하여 -1
        distance = [[-1] * length for _ in range(length)]

        # BFS
        q = deque()
        q.append((start_x, start_y))
        distance[start_x][start_y] = 0

        while q:
            x, y = q.popleft() # 현재 위치
            for dx, dy in moves: # 방향별 시도
                new_x, new_y = x + dx, y + dy # 이동 결과 좌표

                # 체스판 범위 체크하기. 넘어가지 않은 경우만.
                # 그때 방문한 적이 없다면 업데이트
                if 0 <= new_x < length and 0 <= new_y < length:
                    if distance[new_x][new_y] == -1:
                        distance[new_x][new_y] = distance[x][y] + 1

                        # 목표에 도착했으면
                        if new_x == target_x and new_y == target_y:
                            results.append(distance[new_x][new_y])
                            q.clear()
                            break
                        
                        # 안 했으면
                        q.append((new_x, new_y))
    return results


print(chess(input))