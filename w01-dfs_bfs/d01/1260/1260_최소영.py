from collections import deque

# DFS 풀이
def DFS(v):
    visited1[v] = 1
    print(v, end=' ')

    for i in range(1, n+1):
        if visited1[i] == 0 and board[v][i] == 1:
            DFS(i)

# 입력 처리
n, m, v = map(int, input().split())
board = [[0] * (n+1) for _ in range(n+1)]
visited1 = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    board[a][b] = 1
    board[b][a] = 1

DFS(v)
print()


# BFS 풀이
visited2 = [0] * (n+1)
Q = deque()
Q.append(v)
visited2[v] = 1

while Q:
    node = Q.popleft()
    print(node, end=' ')

    for i in range(1, n+1):
        if visited2[i] == 0 and board[node][i] == 1:
            Q.append(i)
            visited2[i] = 1