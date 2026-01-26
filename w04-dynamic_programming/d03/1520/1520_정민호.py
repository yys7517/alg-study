import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

# M: 지도 세로 길이(<= 500)
# N: 지도 가로 길이(<= 500)
M, N = map(int, input().split())


MAP = [list(map(int, input().split())) for _ in range(M)]

# (0, 0)에서 출발하여 (M-1, N-1)까지 도달해야 한다.
# 이 때 현재 위치보다 더 낮은 구역으로만 이동할 수 있다.

# 1. 도착 지점에서부터 이동 로직의 역순으로 깊이 우선 탐색을 진행한다.
# 2. 

# 하, 우, 좌, 상
DIRS = [
    (1, 0),
    (0, 1),
    (0, -1),
    (-1, 0),
]

dp = [[-1] * N for _ in range(M)]

def dfs(y, x):
    if x == M - 1 and y == N-1:
        return 1

    if dp[y][x] != -1:
        return dp[y][x]

    dp[y][x] = 0

    for dy, dx in DIRS:
        ny, nx = y+dy, x+dx
        if (0 <= nx < M and 0 <= ny < N and (MAP[ny][nx] < MAP[y][x])):
            dp[y][x] += dfs(ny, nx)

    return dp[y][x]

print(dfs(0, 0))
            