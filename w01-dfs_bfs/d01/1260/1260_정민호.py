# 입력
# N, M, V
    # N: 정점의 개수    
    # M: 간선의 개수
    # V: 탐색을 시작할 정점의 번호
# s, e: M개의 줄에 걸쳐 간선이 연결하는 두 정점의 번호가 주어짐
# 해당 간선은 "양방향"이다 -> s에서 e로, e에서 s로 둘 다 이동 가능하다.

# 출력
# 첫째 줄에 DFS를 수행한 결과
# 둘째 줄에 BFS를 수행한 결과
# ! V부터 방문된 점을 순서대로 출력하면 된다.

# 고찰
# Q1. M개의 줄에 걸쳐 s, e를 얻으면 어떻게 저장해야 할까?
# A1. defaultdict을 사용하여 예외처리에 신경을 쓰지 않게 해보자.
# 
# Q2. 처음부터 고립된 정점이 주어지면 어떻게 해야 할까?
# A2. defaultdict에 해당 키값이 존재하는 지 확인하고, 없다면 출력을 건너 뛰자

# 주의 사항
# 1. 방문 가능한 정점이 여러 개인 경우 정점 번호가 작은 것을 먼저 방문해야 한다.
# 2. 정점 번호는 1번부터 N번까지이다.

# 구현
# 1. N, M, V를 초기화한다.
# 2. M번동안 s, e를 입력 받고 defaultdict에 넣는다.
# 3. defaultdict를 순회하며 "정점 번호가 작은 것이 먼저 오도록" 정렬한다.
# 4. dfs를 먼저 수행하며 list를 업데이트 한다.
# 5. bfs를 수행하여 list를 업데이트 한다.
# 6. 두 탐색 결과 리스트를 각각 순서대로 출력한다.

from collections import deque, defaultdict

# 1. N, M, V 초기화
N, M, V = map(int, input().split())

# 2. defaultdict 초기화
dd = defaultdict(list)
for _ in range(M):
    s, e = map(int, input().split())

    # 양방향 간선임을 고려했다.
    dd[s].append(e)
    dd[e].append(s)

# 3. defaultdict 정렬
for key in dd.keys():
    dd[key].sort()

# 4. dfs를 수행하여 결과 리스트에 저장한다.
dfs_result = []
dfs_visited = [False for _ in range(N+1)]
dfs_visited[V] = True
stack = [V]
while stack:
    v = stack.pop()
    if dfs_visited[v]:
        continue
    dfs_visited[v] = True
    for n in dd[v]:
        if not dfs_visited[n]:
            stack.append(n)

# 5. bfs를 수행하여 list를 업데이트한다.
q = deque([V])
bfs_result = []
bfs_visited = [False for _ in range(N+1)]
bfs_visited[V] = True
while q:
    v = q.popleft()
    for n in dd[v]:
        if not bfs_visited[n]:
            bfs_visited[n] = True
            q.append(n)
            bfs_result.append(n)

# 6. 결과 출력
print(" ".join(dfs_result))
print(" ".join(bfs_result))