from collections import deque

# DFS 풀이
def DFS(v):
    global count
    visited[v] = True

    for x in board[v]:
        if not visited[x]:
            count += 1
            DFS(x)

n = int(input())
pair = int(input())
board = [[] for _ in range(n+1)]
visited = [False] * (n+1)
count = 0

for _ in range(pair):
    a, b = map(int, input().split())
    board[a].append(b)
    board[b].append(a)

DFS(1)
print(count)



# BFS 풀이
count2 = 0
visited2 = [False] * (n+1)

Q = deque()
Q.append(1)
visited2[1] = True

while Q:
    node = Q.popleft()

    for x in board[node]:
        if not visited2[x]:
            Q.append(x)
            visited2[x] = True
            count2 += 1

print(count2)